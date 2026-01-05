import os
import customtkinter
from customtkinter import CTk, CTkButton, CTkImage, CTkLabel, CTkScrollableFrame, CTkTextbox, CTkFrame
from PIL import Image, ImageTk
from graphviz import Digraph
import theme_state
from tkinter import messagebox


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_FILE = os.path.join(BASE_DIR, "..", "Themes", "theme-modes.json")

customtkinter.set_default_color_theme(THEME_FILE)
customtkinter.set_appearance_mode(theme_state.current_mode)



# Nodes
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ExprNode(BTNode):
    pass

class BSTNode(BTNode):
    pass

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}



# Tree Logic
def build_expr_tree(expression):
    nodes, ops = [], []

    def apply():
        op = ops.pop()
        r = nodes.pop()
        l = nodes.pop()
        n = ExprNode(op)
        n.left, n.right = l, r
        nodes.append(n)

    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isalnum():
            nodes.append(ExprNode(c))
        elif c in PRECEDENCE:
            while ops and ops[-1] in PRECEDENCE and PRECEDENCE[ops[-1]] >= PRECEDENCE[c]:
                apply()
            ops.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                apply()
            ops.pop()
        i += 1

    while ops:
        apply()
    return nodes[0] if nodes else None

def inorder(n, r):
    if n: inorder(n.left, r); r.append(n.val); inorder(n.right, r)

def preorder(n, r):
    if n: r.append(n.val); preorder(n.left, r); preorder(n.right, r)

def postorder(n, r):
    if n: postorder(n.left, r); postorder(n.right, r); r.append(n.val)

def visualize_tree(root, filename):
    dot = Digraph(format="png", graph_attr={"rankdir": "TB"})
    def add(n):
        if not n: return
        dot.node(str(id(n)), str(n.val))
        if n.left:
            dot.edge(str(id(n)), str(id(n.left)))
            add(n.left)
        if n.right:
            dot.edge(str(id(n)), str(id(n.right)))
            add(n.right)
    add(root)
    dot.render(filename, cleanup=True)



class tree_of_life(CTk):
    # Switch Theme
    def switch_theme(self):
        theme_state.current_mode = (
            "light" if theme_state.current_mode == "dark" else "dark")
        customtkinter.set_appearance_mode(theme_state.current_mode)
        self.apply_theme()

    def apply_theme(self):
        if theme_state.current_mode == "dark":
            toggle_color = "#000000"
            option_color = "#252728"
            option_hover = "#3b3d3e"
        else:
            toggle_color = "#ffffff"
            option_color = "#e2e5e9"
            option_hover = "#b7b7b8"

        self.toggle_button.configure(fg_color=toggle_color, hover_color=toggle_color)
        self.back_button.configure(fg_color=toggle_color, hover_color=toggle_color)



    # Switch Page Function
    def back_to_entry(self):
        from main_page import Main
        self.destroy()
        app = Main()
        app.mainloop()



    # The Front End
    def __init__(self):
        super().__init__()

        # Window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("J.A.N.I.T.O.R.")
        self.geometry(f"{screen_width}x{screen_height}+0+0")



        # Background
        self.bg_image = CTkImage(
            dark_image=Image.open("../images/dm_binary_bg.png"),
            light_image=Image.open("../images/lm_binary_bg.png"),
            size=(screen_width, screen_height)
        )
        self.bg = CTkLabel(self, image=self.bg_image, text="")
        self.bg.place(x=0.45, y=-22.5)



        # BST and BT Button
        self.bt_btn = CTkButton(self,
                                text="Binary Tree",
                                font=("Arial", 17, "bold"),
                                width=235,
                                height=60,
                                corner_radius=30,
                                command=lambda: self.switch_mode("BT")
        )
        self.bt_btn.place(x=41, y=228)

        self.bst_btn = CTkButton(self,
                                 text="Binary Search Tree",
                                 font=("Arial", 17, "bold"),
                                 width=235,
                                 height=60,
                                 corner_radius=30,
                                 command=lambda: self.switch_mode("BST")
        )
        self.bst_btn.place(x=306, y=229)



        # Tree
        self.image_frame = CTkFrame(self, width=900, height=600, corner_radius=10)
        self.image_frame.place(x=500, y=100)

        self.image_label = CTkLabel(self.image_frame, text="", width=900, height=600)
        self.image_label.place(x=0, y=0)




        # Frame
        # BT Frame
        self.bt_frame = CTkFrame(self, height=250, width=293, corner_radius=30)
        CTkLabel(self.bt_frame, text="Expression Tree", font=("Arial", 17, "bold")).place(x=150, y=10, anchor="center")
        self.expr = CTkTextbox(self.bt_frame, width=280, height=60)
        self.expr.place(x=10, y=40)
        self.bt_frame.place(x=141, y=359)

        self.bt_gen_btn = CTkButton(
            self,
            text="Generate Expression Tree",
            font=("Arial", 17, "bold"),
            width=293,
            height=60,
            command=self.gen_expr
        )
        self.bt_gen_btn.place(x=139.5, y=674)

        # BST Frame
        self.bst_frame = CTkFrame(self, height=250, width=293, corner_radius=50)
        CTkLabel(self.bst_frame, text="Binary Search Tree", font=("Arial", 17, "bold")).place(x=150, y=10, anchor="center")
        self.bst_input = CTkTextbox(self.bst_frame, width=280, height=60)
        self.bst_input.place(x=10, y=40)
        self.bst_frame.place(x=141, y=359)

        self.bst_gen_btn = CTkButton(
            self,
            text="Generate BST",
            font=("Arial", 17, "bold"),
            width=293,
            height=60,
            corner_radius=30,
            command=self.gen_bst
        )
        self.bst_gen_btn.place(x=139.5, y=674)



        # Toggle button
        self.toggle_button_image = CTkImage(
            dark_image=Image.open("../images/dm_main_toggle.png"),
            light_image=Image.open("../images/lm_main_toggle.png"),
            size=(100, 100)
        )

        toggle_color = "#000000" if theme_state.current_mode == "dark" else "#ffffff"
        self.toggle_button = CTkButton(
            self,
            text="",
            width=100,
            height=100,
            corner_radius=0,
            fg_color=toggle_color,
            hover_color=toggle_color,
            image=self.toggle_button_image,
            command=self.switch_theme
        )
        self.toggle_button.place(x=1850, y=987, anchor="center")

        # Exit button
        self.back_button_image = CTkImage(
            dark_image=Image.open("../images/dm_back_button.png"),
            light_image=Image.open("../images/lm_back_button.png"),
            size=(100, 100)
        )

        back_button_color = "#000000" if theme_state.current_mode == "dark" else "#ffffff"
        self.back_button = CTkButton(
            self,
            text="",
            width=100,
            height=100,
            corner_radius=0,
            fg_color=back_button_color,
            hover_color=back_button_color,
            image=self.back_button_image,
            command=self.back_to_entry
        )
        self.back_button.place(x=1730, y=987, anchor="center")

        # Applies Theme for sure
        self.apply_theme()



    # Switch Function for BT and BST
    def switch_mode(self, mode):
        # Move all to off-screen instead of forgetting
        self.bt_frame.place(x=-1000, y=-1000)
        self.bt_gen_btn.place(x=-1000, y=-1000)
        self.bst_frame.place(x=-1000, y=-1000)
        self.bst_gen_btn.place(x=-1000, y=-1000)

        if mode == "BT":
            self.bt_frame.place(x=141, y=359)
            self.bt_gen_btn.place(x=139.5, y=674)
        else:
            self.bst_frame.place(x=141, y=359)
            self.bst_gen_btn.place(x=140, y=697)

    #Function for BT
    def gen_expr(self):
        expr = self.expr.get("1.0", "end").strip().replace(" ", "")
        if not expr:
            messagebox.showwarning("Input Error", "Enter an expression")
            return

        root = build_expr_tree(expr)
        visualize_tree(root, "tree")

        img = Image.open("tree.png")
        img = img.resize((900, int(900 * img.height / img.width)))
        self.img = CTkImage(light_image=img, size=img.size)
        self.image_label.configure(image=self.img)

        ino, pre, post = [], [], []
        inorder(root, ino)
        preorder(root, pre)
        postorder(root, post)

        self.trav.configure(state="normal")
        self.trav.delete("1.0", "end")
        self.trav.insert("end", f"Inorder: {' '.join(ino)}\n")
        self.trav.insert("end", f"Preorder: {' '.join(pre)}\n")
        self.trav.insert("end", f"Postorder: {' '.join(post)}")
        self.trav.configure(state="disabled")

    #Function for BST
    def gen_bst(self):
        values = self.bst_input.get("1.0", "end").replace(",", " ").split()
        if len(values) < 2:
            messagebox.showwarning("Input Error", "Enter numbers")
            return

        root = None
        for v in values:
            n = BSTNode(int(v))
            if not root:
                root = n
                continue
            cur = root
            while True:
                if n.val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = n; break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = n; break

        visualize_tree(root, "tree")
        img = Image.open("tree.png")
        img = img.resize((900, int(900 * img.height / img.width)))
        self.img = CTkImage(light_image=img, size=img.size)
        self.image_label.configure(image=self.img)


if __name__ == "__main__":
    app = tree_of_life()
    app.mainloop()
