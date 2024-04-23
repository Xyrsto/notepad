from customtkinter import *
from CTkMenuBar import *
from menubar import build_menubar

def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

window = CTk()
window.configure(bg="#32292F")
window.title("Turbo Notepad")
window.iconbitmap("notepad_icon_131797.ico")
window.geometry(CenterWindowToDisplay(window, 1000, 800, -0.000001))

build_menubar(window)

text = CTkTextbox(window, bg_color="#32292F", fg_color="#32292F", font=("Consolas", 25))
text.pack(expand=True, fill="both")

set_appearance_mode('dark')
window.mainloop()