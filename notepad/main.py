import flet as ft
from flet import (UserControl, ControlEvent, TextField, InputBorder, AppBar)

class TextEditor(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = ft.TextField(
                                    multiline=True, 
                                    autofocus = True, 
                                    border=ft.InputBorder.NONE, 
                                    min_lines=40, 
                                    on_change=save_text, 
                                    content_padding=30,
                                    cursor_color='yellow'
                                )

def save_text(self, e: ft.ControlEvent) -> None:
    with open('save.txt', 'w') as f:
        f.write(self.textfield.value)

def read_text(self) -> str | None:
    try:
        with open('save.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        self.texfield.hind_text = 'Welcome to the Turbo Editor'

def build(self) -> TextField:
    self.textfield.value = self.read_text()
    return self.textfield

def main(page: ft.Page):
    page.title = "Turbo notepad"
    page.scroll = True
    appbar_text_ref = ft.Ref[ft.Text]()

    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        appbar_text_ref.current.value = e.control.content.value
        page.update()

    def handle_on_open(e):
        print(f"{e.control.content.value}.on_open")

    def handle_on_close(e):
        print(f"{e.control.content.value}.on_close")

    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")

    textField = ft.TextField(
                                    multiline=True, 
                                    autofocus = True, 
                                    border=ft.InputBorder.NONE, 
                                    min_lines=40,
                                    content_padding=30,
                                    cursor_color='yellow'
                                )

    menubar = AppBar(
        leading_width=40,
        title=ft.Text("Turbo notepad", color="#262626", font_family="Consolas"),
        bgcolor= "#ACBFA4",
        actions=[
            ft.IconButton(ft.icons.SEARCH, icon_color=ft.colors.PRIMARY),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="About"),
                    ft.PopupMenuItem(text="Settings"),
                ]
            ),
        ],
    )

    page.add(menubar, textField)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, bgcolor="#ACBFA4"
    )
    page.update()

ft.app(main)