import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from graphviz import Digraph
from PIL import Image, ImageTk
import os

# ------------------ GRAPHVIZ ------------------
def visualize_tree(root, filename):
    dot = Digraph(
        format="png",
        graph_attr={"rankdir": "TB"},
        node_attr={"shape": "circle", "style": "filled", "fillcolor": "lightblue", "fontname": "Arial"}
    )

    def add(node):
        if not node:
            return
        dot.node(str(id(node)), str(node.val))
        if getattr(node, 'left', None):
            dot.edge(str(id(node)), str(id(node.left)), label="L")
            add(node.left)
        if getattr(node, 'right', None):
            dot.edge(str(id(node)), str(id(node.right)), label="R")
            add(node.right)

    add(root)
    dot.render(filename, cleanup=True)

# ------------------ BINARY TREE NODE ------------------
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ------------------ EXPRESSION TREE (for reference, but we'll modify BT) ------------------
class ExprNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def build_expr_tree(expression):
    """Convert infix expression to a binary expression tree using a stack."""
    def is_operator(c):
        return c in PRECEDENCE

    nodes = []
    ops = []

    def apply_op():
        op = ops.pop()
        right = nodes.pop()
        left = nodes.pop()
        n = ExprNode(op)
        n.left = left
        n.right = right
        nodes.append(n)

    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isalnum():
            nodes.append(ExprNode(c))
            i += 1
        elif is_operator(c):
            while ops and ops[-1] in PRECEDENCE and PRECEDENCE[ops[-1]] >= PRECEDENCE[c]:
                apply_op()
            ops.append(c)
            i += 1
        elif c == '(':
            ops.append(c)
            i += 1
        elif c == ')':
            while ops[-1] != '(':
                apply_op()
            ops.pop()  # remove '('
            i += 1
        else:
            i += 1  # skip spaces

    while ops:
        apply_op()

    return nodes[0] if nodes else None

# Traversals
def inorder(node, res):
    if node:
        inorder(node.left, res)
        res.append(node.val)
        inorder(node.right, res)

def preorder(node, res):
    if node:
        res.append(node.val)
        preorder(node.left, res)
        preorder(node.right, res)

def postorder(node, res):
    if node:
        postorder(node.left, res)
        postorder(node.right, res)
        res.append(node.val)

# ------------------ BST ------------------
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)

# ------------------ CTk GUI ------------------
class TreeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Binary Tree & BST Visualizer")
        self.geometry("1300x750")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Mode selection
        self.mode = "BT"  # Default to Binary Tree
        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(side="top", fill="x", padx=10, pady=10)
        self.bt_button = ctk.CTkButton(self.mode_frame, text="Binary Tree", command=lambda: self.switch_mode("BT"))
        self.bt_button.pack(side="left", padx=5)
        self.bst_button = ctk.CTkButton(self.mode_frame, text="Binary Search Tree", command=lambda: self.switch_mode("BST"))
        self.bst_button.pack(side="left", padx=5)

        # Frames
        self.left_frame = ctk.CTkFrame(self, width=450)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Right frame: Canvas for image with scrollbar
        self.canvas = tk.Canvas(self.right_frame, bg="white")
        self.v_scrollbar = tk.Scrollbar(self.right_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.v_scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel for scrolling
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)

        self.traversal_text = ctk.CTkTextbox(self.right_frame, height=180, undo=True)  # Enabled undo for Ctrl+Z
        self.traversal_text.pack(fill="x", pady=10)

        # Buttons
        self.button_frame = ctk.CTkFrame(self.right_frame)
        self.button_frame.pack(pady=5)
        self.download_btn = ctk.CTkButton(self.button_frame, text="Download Tree", command=self.download_tree)
        self.download_btn.pack(side="left", padx=5)
        self.clear_btn = ctk.CTkButton(self.button_frame, text="Clear/Reset", command=self.clear_all)
        self.clear_btn.pack(side="left", padx=5)

        # Sections
        self.create_binary_tree_section()
        self.create_bst_section()
        self.switch_mode("BT")  # Start with BT

    def _on_mousewheel(self, event):
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:  # Windows
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def switch_mode(self, mode):
        self.mode = mode
        if mode == "BT":
            self.bt_frame.pack(fill="both", expand=True)
            self.bst_frame.pack_forget()
        else:
            self.bst_frame.pack(fill="both", expand=True)
            self.bt_frame.pack_forget()

    # ------------------ Binary Tree Section ------------------
    def create_binary_tree_section(self):
        self.bt_frame = ctk.CTkFrame(self.left_frame)
        
        # Expression Tree Option
        ctk.CTkLabel(self.bt_frame, text="Option 1: Expression Tree").pack(pady=2)
        ctk.CTkLabel(self.bt_frame, text="Enter expression (e.g. A+B-C*D, spaces/commas allowed, supports ^):").pack(pady=2)
        self.bt_expr_textbox = ctk.CTkTextbox(self.bt_frame, height=60, undo=True)  # Enabled undo
        self.bt_expr_textbox.pack(pady=5)
        self.bt_generate_expr_tree_btn = ctk.CTkButton(self.bt_frame, text="Generate Expression Tree", command=self.generate_expr_tree)
        self.bt_generate_expr_tree_btn.pack(pady=5)
        
        # Complete Binary Tree Option
        ctk.CTkLabel(self.bt_frame, text="Option 2: Complete Binary Tree").pack(pady=2)
        ctk.CTkLabel(self.bt_frame, text="Enter level number (1-5):").pack(pady=2)
        self.bt_level_entry = ctk.CTkEntry(self.bt_frame)
        self.bt_level_entry.pack(pady=5)
        self.bt_generate_inputs_btn = ctk.CTkButton(self.bt_frame, text="Generate Node Inputs", command=self.generate_bt_inputs)
        self.bt_generate_inputs_btn.pack(pady=5)
        self.bt_nodes_frame = ctk.CTkScrollableFrame(self.bt_frame, height=300)
        self.bt_nodes_frame.pack(pady=5, fill="both", expand=True)
        self.bt_generate_tree_btn = ctk.CTkButton(self.bt_frame, text="Generate Binary Tree", command=self.generate_bt_tree)
        self.bt_generate_tree_btn.pack(pady=5)

    def generate_expr_tree(self):
        expr = self.bt_expr_textbox.get("1.0", tk.END).strip().replace(" ", "").replace(",", "")
        if not expr:
            messagebox.showerror("Error", "Enter a valid expression")
            return

        try:
            root = build_expr_tree(expr)
            if not root:
                raise ValueError("Invalid expression")
            visualize_tree(root, "binary_tree_gui")
            self.display_image("binary_tree_gui.png")

            inorder_res, preorder_res, postorder_res = [], [], []
            inorder(root, inorder_res)
            preorder(root, preorder_res)
            postorder(root, postorder_res)
            self.display_traversals(inorder_res, preorder_res, postorder_res)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to parse expression: {str(e)}")

    def generate_bt_inputs(self):
        for widget in self.bt_nodes_frame.winfo_children():
            widget.destroy()
        try:
            level = int(self.bt_level_entry.get())
            if not (1 <= level <= 5):
                raise ValueError
        except:
            messagebox.showerror("Error", "Enter level between 1 and 5")
            return
        self.bt_entries = []
        total_nodes = 2**level - 1
        for i in range(total_nodes):
            label = ctk.CTkLabel(self.bt_nodes_frame, text=f"Node {i+1}:")
            label.grid(row=i, column=0, padx=2, pady=2)
            entry = ctk.CTkEntry(self.bt_nodes_frame, placeholder_text="Value (leave empty to skip)")
            entry.grid(row=i, column=1, padx=2, pady=2)
            self.bt_entries.append(entry)

    def generate_bt_tree(self):
        if not hasattr(self, 'bt_entries'):
            messagebox.showerror("Error", "Generate inputs first")
            return
        values = []
        for entry in self.bt_entries:
            val = entry.get().strip()
            values.append(val if val else None)
        root = self.build_complete_bt(values, 0)
        visualize_tree(root, "binary_tree_gui")
        self.display_image("binary_tree_gui.png")
        inorder_res, preorder_res, postorder_res = [], [], []
        inorder(root, inorder_res)
        preorder(root, preorder_res)
        postorder(root, postorder_res)
        self.display_traversals(inorder_res, preorder_res, postorder_res)

    def build_complete_bt(self, values, index):
        if index >= len(values) or values[index] is None:
            return None
        node = BTNode(values[index])
        node.left = self.build_complete_bt(values, 2*index + 1)
        node.right = self.build_complete_bt(values, 2*index + 2)
        return node

    # ------------------ BST Section ------------------
    def create_bst_section(self):
        self.bst_frame = ctk.CTkFrame(self.left_frame)
        ctk.CTkLabel(self.bst_frame, text="Binary Search Tree", font=("Arial", 18)).pack(pady=10)

        # Textbox option
        ctk.CTkLabel(self.bst_frame, text="Enter all numbers in one line (space or comma-separated, 10-30 integers):").pack(pady=2)
        self.bst_textbox = ctk.CTkTextbox(self.bst_frame, height=60, undo=True)  # Enabled undo
        self.bst_textbox.pack(pady=5)

        self.bst_generate_tree_btn = ctk.CTkButton(self.bst_frame, text="Generate BST", command=self.generate_bst_tree)
        self.bst_generate_tree_btn.pack(pady=5)

    def generate_bst_tree(self):
        textbox_content = self.bst_textbox.get("1.0", tk.END).strip()
        if not textbox_content:
            messagebox.showerror("Error", "Enter numbers in the textbox")
            return
        # Replace commas with spaces and split
        values = textbox_content.replace(",", " ").split()
        if not (10 <= len(values) <= 30):
            messagebox.showerror("Error", "Enter between 10 and 30 numbers")
            return
        bst = BST()
        for val in values:
            try:
                bst.insert(int(val))
            except ValueError:
                messagebox.showerror("Error", f"Invalid number: {val}")
                return
        visualize_tree(bst.root, "bst_tree_gui")
        self.display_image("bst_tree_gui.png")
        inorder_res = []
        bst.inorder(bst.root, inorder_res)
        self.display_traversals(inorder_res, [], [])

    # ------------------ Helpers ------------------
    def display_image(self, path):
        img = Image.open(path)
        # Resize to fit the canvas width, keeping aspect ratio
        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:  # If not yet rendered, use a default
            canvas_width = 700
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width
        new_width = canvas_width - 20  # Margin
        new_height = int(new_width * aspect_ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.delete("all")  # Clear previous image
        self.canvas.create_image(0, 0, anchor="nw", image=self.img_tk)
        self.canvas.config(scrollregion=(0, 0, new_width, new_height))

    def display_traversals(self, inorder_res, preorder_res, postorder_res):
        self.traversal_text.configure(state="normal")
        self.traversal_text.delete("1.0", tk.END)
        if inorder_res:
            self.traversal_text.insert(tk.END, f"LTR (In-order): {' '.join(map(str, inorder_res))}\n")
        if preorder_res:
            self.traversal_text.insert(tk.END, f"TLR (Pre-order): {' '.join(map(str, preorder_res))}\n")
        if postorder_res:
            self.traversal_text.insert(tk.END, f"LRT (Post-order): {' '.join(map(str, postorder_res))}\n")
        self.traversal_text.configure(state="disabled")  # Disable editing to prevent typing, but allow copy-paste

    def download_tree(self):
        if not hasattr(self, 'img_tk'):
            messagebox.showerror("Error", "Generate a tree first")
            return
        folder = "binary_tree images"
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialdir=folder)
        if filename:
            # Copy the current image to the selected path
            img = Image.open("binary_tree_gui.png" if self.mode == "BT" else "bst_tree_gui.png")
            img.save(filename)

    def clear_all(self):
        # Clear image
        self.canvas.delete("all")
        if hasattr(self, 'img_tk'):
            del self.img_tk
        # Clear traversals
        self.traversal_text.configure(state="normal")
        self.traversal_text.delete("1.0", tk.END)
        self.traversal_text.configure(state="disabled")
        # Clear inputs based on mode
        if self.mode == "BT":
            self.bt_expr_textbox.delete("1.0", tk.END)
            self.bt_level_entry.delete(0, tk.END)
            for widget in self.bt_nodes_frame.winfo_children():
                widget.destroy()
            if hasattr(self, 'bt_entries'):
                del self.bt_entries
        else:
            self.bst_textbox.delete("1.0", tk.END)

# ------------------ RUN ------------------
if __name__ == "__main__":
    app = TreeApp()
    app.mainloop()