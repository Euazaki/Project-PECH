import os
import customtkinter
from customtkinter import CTk, CTkButton, CTkImage, CTkFrame, CTkLabel, CTkEntry
from PIL import Image
import theme_state

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_FILE = os.path.join(BASE_DIR, "..", "Themes", "theme-modes.json")

sample_pass = "67"

customtkinter.set_default_color_theme(THEME_FILE)
customtkinter.set_appearance_mode(theme_state.current_mode)

class gate(CTk):

    # Toggle Theme Function
    def switch_theme(self):
        theme_state.current_mode = (
            "light" if theme_state.current_mode == "dark" else "dark"        )
        customtkinter.set_appearance_mode(theme_state.current_mode)

        enter_color = "#35363a" if theme_state.current_mode == "dark" else "#e2e5e9"
        entry_color = "#3b3d3e" if theme_state.current_mode == "dark" else "#e2e5e9"
        toggle_color = "#252728" if theme_state.current_mode == "dark" else "#e2e5e9"

        self.enter_button.configure(fg_color=enter_color, hover_color=enter_color)
        self.password_entry.configure(fg_color=entry_color)

        self.password_entry.configure(
            fg_color=entry_color
        )
        self.apply_theme()

    def apply_theme(self):
        enter_color = "#35363a" if theme_state.current_mode == "dark" else "#e2e5e9"
        entry_color = "#3b3d3e" if theme_state.current_mode == "dark" else "#e2e5e9"
        toggle_color = "#252728" if theme_state.current_mode == "dark" else "#e2e5e9"

        self.enter_button.configure(fg_color=enter_color, hover_color=enter_color)
        self.password_entry.configure(fg_color=entry_color)
        self.toggle_button.configure(fg_color=toggle_color, hover_color=toggle_color)


    # Get pass Function and Transfer to next file
    def open_main_page(self):
        entered = self.password_entry.get()
        if entered == sample_pass:
            from main_page import Main
            self.destroy()
            app = Main()
            app.mainloop()
        else:
            pass


    def __init__(self):
        super().__init__()



        # Window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("J.A.N.I.T.O.R.")
        self.geometry(f"{screen_width}x{screen_height}+0+0")



        # Background
        self.bg_image = CTkImage(
            dark_image=Image.open("../images/dm_entry_bg.png"),
            light_image=Image.open("../images/lm_entry_bg.png"),
            size=(screen_width - 0, screen_height)
        )
        self.bg = CTkLabel(self, image=self.bg_image, text="")
        self.bg.place(x=0.45, y=-22.5)



        # Password
        self.password_entry = CTkEntry(master=self,
                                   justify="center",
                                   placeholder_text= "Enter the Password",
                                   width=580,
                                   height=88,
                                   font=("Sans", 27),
                                   corner_radius=0,
                                   border_width=0)
        self.password_entry.place(x=670, y=430)



        # Enter Button
        self.enter_button_image = CTkImage(
            dark_image=Image.open("../images/dm_entry_icon.png"),
            light_image=Image.open("../images/lm_entry_icon.png"),
            size=(79.04, 64)
        )

        self.enter_button = CTkButton(self,
                                       text="",
                                       width=100,
                                       height=100,
                                       fg_color="#35363a",
                                       hover_color="#35363a",
                                       image= self.enter_button_image,
                                       command= self.open_main_page)
        self.enter_button.place(x=960, y=695, anchor="center")



        # Theme toggle button
        self.toggle_button_image = CTkImage(
            dark_image=Image.open("../images/dm_toggle_icon.png"),
            light_image=Image.open("../images/lm_toggle_icon.png"),
            size=(62.5, 62.5)
        )

        self.toggle_button = CTkButton(self,
                                       text="",
                                       width=62.7,
                                       height=62.7,
                                       image=self.toggle_button_image,
                                       fg_color="#000000",
                                       hover_color="#000000",
                                       command=self.switch_theme
                                       )
        self.toggle_button.place(x=1850, y=987.3, anchor="center")

        self.apply_theme()

if __name__ == "__main__":
    app = gate()
    app.mainloop()
