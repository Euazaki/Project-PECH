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
from PIL import Image

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("J.A.N.I.T.O.R. by Project PECH")
        self.WINDOW_WIDTH = 1400
        self.WINDOW_HEIGHT = 800
        self.center_window(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # ===Appearance settings===
        ctk.set_appearance_mode("dark")  # Start with dark mode
        ctk.set_default_color_theme("blue")

        self.FB_BLUE = "#1877F2"
        self.FB_DARK_BG = "#18191A"
        self.LIGHT_BLUE_BG = "#F0F3FA" 
        self.LIGHT_BLUE_HEADER = "#D5DEEF" 
        self.LIGHT_BLUE_BUTTON = "#8AAEE0" 
        self.LIGHT_BLUE_FOOTER = "#B1C9EF"
        self.FB_DARK_TEXT = "#E4E6EA"
        self.DARK_BLUE = "#395886"
        self.FB_LIGHT_TEXT = "#050505"
        self.ORANGE_HOVER = "#FFA500"  # Orange for hover

        self.current_mode = "dark"

        # ===Background images===
        try:
            self.bg_image_dark = ctk.CTkImage(Image.open("Assets/background_gradient_dark.png"), size=(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            self.bg_image_light = ctk.CTkImage(Image.open("Assets/background_gradient_light.png"), size=(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            self.bg_label = ctk.CTkLabel(self, image=self.bg_image_dark, text="")  # Start with dark mode background
            self.bg_label.place(relwidth=1, relheight=1)  # Cover the entire window
        except FileNotFoundError:
            self.bg_label = None  # No background if images not found

        # ===Main grid configuration===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ===Login frame===
        self.login_frame = ctk.CTkFrame(self, fg_color=self.FB_DARK_BG, corner_radius=15, width=500, height=600)
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.login_frame.grid_propagate(False)

        self.login_frame.grid_rowconfigure(0, weight=1)
        self.login_frame.grid_columnconfigure(0, weight=1)

        self.inner_frame = ctk.CTkFrame(self.login_frame, fg_color="transparent")
        self.inner_frame.grid(row=0, column=0)

        self.login_title = ctk.CTkLabel(self.inner_frame, text="J.A.N.I.T.O.R.", font=("Work Sans", 80, "bold"), text_color=self.FB_DARK_TEXT)
        self.login_title.pack(pady=(20, 5))

        self.tagline = ctk.CTkLabel(self.inner_frame, text="Keeping your establishment clean, ordered, and organized", font=("Work Sans", 19), text_color="#65676B")
        self.tagline.pack(pady=(0, 10))

        self.password_entry = ctk.CTkEntry(self.inner_frame, placeholder_text="Enter the Password", show="*", width=350, height=40, fg_color="#3A3B3C", text_color=self.FB_DARK_TEXT)
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            master=self.inner_frame,
            fg_color=self.FB_BLUE, #(translucency not supported)
            font=("Arial", 20, "bold"),
            text_color="#FFFFFF",
            text="→",
            width=50,
            height=50,
            corner_radius=25,
            border_width=0,
            command=self.login,
            hover_color=self.ORANGE_HOVER 
        )
        self.login_button.pack(pady=20)

        self.error_label = ctk.CTkLabel(self.inner_frame, text="", font=("Arial", 14), text_color="#FA383E")
        self.error_label.pack(pady=(0, 20))

        self.login_mode_toggle = ctk.CTkButton(self.login_frame, text="☀️ Light Mode", command=self.toggle_mode, width=120, height=40, fg_color=self.FB_BLUE, hover_color=self.ORANGE_HOVER)
        self.login_mode_toggle.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.bottom_frame = ctk.CTkFrame(self.inner_frame, fg_color="transparent")
        self.bottom_frame.pack(pady=(0, 20))

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)

        self.made_by_label = ctk.CTkLabel(self.bottom_frame, text="Made by", font=("Work Sans", 15), text_color="#65676B", fg_color="transparent")
        self.made_by_label.grid(row=0, column=0, sticky="e", padx=(0,5))

        try:
            logo_image = ctk.CTkImage(Image.open("Assets/ProjectPECH_Logo_DARK-NoBG.png"), size=(150, 150))
            self.logo_label = ctk.CTkLabel(self.bottom_frame, image=logo_image, text="", fg_color="transparent")
        except FileNotFoundError:
            self.logo_label = ctk.CTkLabel(self.bottom_frame, text="[Logo Not Found - Check Path]", font=("Arial", 16), text_color="#65676B", fg_color="transparent")
        self.logo_label.grid(row=0, column=1, sticky="w", padx=(5,0))

    def center_window(self, width, height):
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def toggle_mode(self):
        if self.current_mode == "dark":
            self.current_mode = "light"
            ctk.set_appearance_mode("light")
            self.update_colors_light()
            self.login_mode_toggle.configure(text="🌙 Dark Mode")
        else:
            self.current_mode = "dark"
            ctk.set_appearance_mode("dark")
            self.update_colors_dark()
            self.login_mode_toggle.configure(text="☀️ Light Mode")
        self.error_label.configure(text="")
        self.password_entry.configure(border_color="")

    # ===Dark mode color updates===
    def update_colors_dark(self):
        self.configure(bg=self.FB_DARK_BG)
        self.login_frame.configure(fg_color=self.FB_DARK_BG)
        self.login_title.configure(text_color=self.FB_DARK_TEXT)
        self.tagline.configure(text_color="#65676B")
        self.error_label.configure(text_color="#FA383E")
        self.made_by_label.configure(text_color="#65676B")
        
        self.login_button.configure(fg_color=self.FB_BLUE, hover_color=self.ORANGE_HOVER) #(translucency not supported in CTkButton)
        self.login_mode_toggle.configure(fg_color=self.FB_BLUE, hover_color=self.ORANGE_HOVER)

        try:
            logo_image = ctk.CTkImage(Image.open("Assets/ProjectPECH_Logo_DARK-NoBG.png"), size=(150, 150))
            self.logo_label.configure(image=logo_image, text="")
        except FileNotFoundError:
            self.logo_label.configure(image="", text="[Logo Not Found - Check Path]", text_color="#65676B")

        if self.bg_label:
            self.bg_label.configure(image=self.bg_image_dark)
            
    # ===Light mode color updates===
    def update_colors_light(self):
        LIGHT_BG = self.LIGHT_BLUE_BG

        self.configure(bg=LIGHT_BG)
        self.login_frame.configure(fg_color=LIGHT_BG)
        self.login_title.configure(text_color=self.FB_LIGHT_TEXT)
        self.tagline.configure(text_color=self.DARK_BLUE)
        self.error_label.configure(text_color="#FA383E")
        self.made_by_label.configure(text_color=self.FB_LIGHT_TEXT)

        self.login_button.configure(fg_color=self.LIGHT_BLUE_BUTTON, hover_color="#628ECB")
        self.login_mode_toggle.configure(fg_color=self.LIGHT_BLUE_BUTTON, hover_color="#628ECB")

        try:
            logo_image = ctk.CTkImage(Image.open("Assets/ProjectPECH_Logo-NoBG.png"), size=(150, 150))
            self.logo_label.configure(image=logo_image, text="")
        except FileNotFoundError:
            self.logo_label.configure(image="", text="[Logo Not Found - Check Path]", text_color=self.DARK_BLUE)

        if self.bg_label:
            self.bg_label.configure(image=self.bg_image_light)

    def login(self):
        password = self.password_entry.get()
        # FOR BACKEND INTEGRATION, REPLACE THE FOLLOWING LINES WITH ACTUAL AUTHENTICATION LOGIC
        if password == "admin":
            print("Login successful!")
            self.error_label.configure(text="")
            self.password_entry.configure(border_color="")
            # self.login_frame.grid_forget()  # Uncomment to hide login if adding menu later
        else:
            self.error_label.configure(text="Invalid password. Please try again.")
            self.password_entry.configure(border_color="#FA383E")
            self.password_entry.delete(0, 'end')
            self.after(3000, lambda: [self.error_label.configure(text=""), self.password_entry.configure(border_color="")])

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()