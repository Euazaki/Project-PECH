# ================================================================
#  Project PECH  (read as "PEACH")
#  Full Name : Project for Enhanced Computing Horizons
#  Module Type : Frontend-Only
#  ---------------------------------------------------------------
#  Created by : Euan Sebastian Yco  |  Head of Project PECH
#  Project Members :
#       • Carlos Rafael D. Jocson
#       • Patricia Gwyneth M. Tulagan
#       • Harvy G. Zeta
#       • Euan Sebastian Yco
#  ---------------------------------------------------------------
#  GitHub Repository : https://github.com/Euazaki/Project-PECH.git
# ================================================================

"""Front end-only module for specific functionalities."""


import customtkinter as ctk

def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# === MAIN APP ===
app = ctk.CTk()
app.title("Data Structures and Algorithms Visualizer by Project PECH")

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800
center_window(app, WINDOW_WIDTH, WINDOW_HEIGHT)

# === MAIN GRID CONFIGURATION ===
app.grid_rowconfigure(1, weight=1)   # center content expands
app.grid_columnconfigure(1, weight=1)

# === HEADER ===
header = ctk.CTkFrame(app, height=60, corner_radius=0, fg_color="#1b1b2f")
header.grid(row=0, column=0, columnspan=2, sticky="nsew")
header_label = ctk.CTkLabel(header, text="DSA Visualizer by Project PECH", font=("Arial", 24, "bold"))
header_label.pack(pady=10)

# === SIDEBAR ===
sidebar = ctk.CTkFrame(app, width=220, corner_radius=0, fg_color="#16213e")
sidebar.grid(row=1, column=0, sticky="nsew")
sidebar.grid_propagate(False)

sidebar_label = ctk.CTkLabel(sidebar, text="Algorithms", font=("Arial", 18, "bold"))
sidebar_label.pack(pady=20)

algorithms = ["Stack", "Queue", "Tower of Hanoi", "Sorting", "Coming Soon..."]
for algo in algorithms:
    btn = ctk.CTkButton(sidebar, text=algo, width=180)
    btn.pack(pady=8)

# === MAIN CONTENT AREA ===
main_frame = ctk.CTkFrame(app, fg_color="#0f3460", corner_radius=10)
main_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

content_label = ctk.CTkLabel(main_frame, text="Select an Algorithm to Visualize", font=("Arial", 20))
content_label.pack(pady=40)

# === FOOTER ===
footer = ctk.CTkFrame(app, height=30, corner_radius=0, fg_color="#1b1b2f")
footer.grid(row=2, column=0, columnspan=2, sticky="nsew")
footer_label = ctk.CTkLabel(footer, text="Project PECH © 2025", font=("Arial", 12))
footer_label.pack()

app.mainloop()
