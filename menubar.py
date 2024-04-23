from customtkinter import *
from CTkMenuBar import *
from tkinter import filedialog

def openFileSystem():
    file_path = filedialog.asksaveasfilename(
        title="Save the file",
        initialfile='New text file',
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
    )
    if file_path:
        try:
            with open(file_path, 'w') as f:
                text_to_save = text.get(1.0, END)
                f.write(text_to_save)
        except Exception as e:
            print(f.close)

def build_menubar(window):
    menu = CTkMenuBar(master=window, bg_color="#3864b5")
    button_1 = menu.add_cascade("File")
    button_2 = menu.add_cascade("Options")

    dropdown1 = CustomDropdownMenu(widget=button_1, hover_color="#3864b5")
    dropdown1.add_option(option="Open", command=lambda: print("Open"))
    dropdown1.add_option(option="Save", command=lambda: openFileSystem())
    dropdown1.add_separator()


