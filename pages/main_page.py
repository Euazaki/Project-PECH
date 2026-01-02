import os
import customtkinter
from customtkinter import CTk, CTkButton, CTkImage, CTkLabel
from PIL import Image
import theme_state

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_FILE = os.path.join(BASE_DIR, "..", "Themes", "theme-modes.json")

customtkinter.set_default_color_theme(THEME_FILE)
customtkinter.set_appearance_mode(theme_state.current_mode)



class Main(CTk):
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
        self.garage_button.configure(fg_color=option_color, hover_color=option_hover)
        self.binary_button.configure(fg_color=option_color, hover_color=option_hover)
        self.storage_button.configure(fg_color=option_color, hover_color=option_hover)



    # Switch Page Function
    def back_to_entry(self):
        from entry import gate
        self.destroy()
        app = gate()
        app.mainloop()

    def go_to_garage(self):
        from garage import parking_spaces
        self.destroy()
        app = parking_spaces()
        app.mainloop()

    def go_to_binary(self):
        from binary_tree import tree_of_life
        self.destroy()
        app = tree_of_life()
        app.mainloop()

    def go_to_storage(self):
        from storage import storage_room
        self.destroy()
        app = storage_room()
        app.mainloop()



    # The Front End
    def __init__(self):
        super().__init__()

        # Window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("J.A.N.I.T.O.R.")
        self.geometry(f"{screen_width}x{screen_height}+0+0")



        # Title
        self.title_image = CTkImage(
            dark_image=Image.open("../images/dm_title.png"),
            light_image=Image.open("../images/lm_title.png"),
            size=(695, 135.5)
        )
        self.title_label = CTkLabel(
            self,
            text="",
            height=95.5,
            width=655,
            image=self.title_image,
        )
        self.title_label.place(x=90, y=65)



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



        # Option buttons
        self.garage_option_image = CTkImage(
            dark_image=Image.open("../images/dm_garage_option.png"),
            light_image=Image.open("../images/lm_garage_option.png"),
            size=(137, 123)
        )
        self.binary_option_image = CTkImage(
            dark_image=Image.open("../images/dm_binary_icon.png"),
            light_image=Image.open("../images/lm_binary_icon.png"),
            size=(120, 120)
        )
        self.storage_option_image = CTkImage(
            dark_image=Image.open("../images/dm_storage_icon.png"),
            light_image=Image.open("../images/lm_storage_icon.png"),
            size=(120, 120)
        )

        option_color = "#252728" if theme_state.current_mode == "dark" else "#e2e5e9"
        option_hover = "#3b3d3e" if theme_state.current_mode == "dark" else "#b7b7b8"

        self.garage_button = CTkButton(
            self,
            image=self.garage_option_image,
            text="   Garage",
            width=720,
            height=190,
            corner_radius=54,
            compound="left",
            anchor="w",
            font=("Helvetica World", 55),
            fg_color=option_color,
            hover_color=option_hover,
            command=self.go_to_garage
        )
        self.garage_button.place(x=108, y=265.8)

        self.binary_button = CTkButton(
            self,
            image=self.binary_option_image,
            text="    Binary Tree",
            width=720,
            height=190,
            corner_radius=54,
            compound="left",
            anchor="w",
            font=("Helvetica World", 55),
            fg_color=option_color,
            hover_color=option_hover,
            command=self.go_to_binary
        )
        self.binary_button.place(x=108, y=514.9)

        self.storage_button = CTkButton(
            self,
            image=self.storage_option_image,
            text="    Storage",
            width=720,
            height=190,
            corner_radius=54,
            compound="left",
            anchor="w",
            font=("Helvetica World", 55),
            fg_color=option_color,
            hover_color=option_hover,
            command=self.go_to_storage
        )
        self.storage_button.place(x=108, y=764)

        self.apply_theme()

if __name__ == "__main__":
    app = Main()
    app.mainloop()
