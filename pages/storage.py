import os
import customtkinter
from customtkinter import CTk, CTkButton, CTkImage, CTkLabel
from PIL import Image
import theme_state

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_FILE = os.path.join(BASE_DIR, "..", "Themes", "theme-modes.json")

customtkinter.set_default_color_theme(THEME_FILE)
customtkinter.set_appearance_mode(theme_state.current_mode)


class storage_room(CTk):
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
            dark_image=Image.open("../images/dm_storage_bg.png"),
            light_image=Image.open("../images/lm_storage_bg.png"),
            size=(screen_width, screen_height)
        )
        self.bg = CTkLabel(self, image=self.bg_image, text="")
        self.bg.place(x=0.45, y=-22.5)



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

if __name__ == "__main__":
    app = storage_room()
    app.mainloop()
