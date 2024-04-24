import flet as ft

def main(page: ft.Page):
    page.title = "Turbo notepad"
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

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor="#ACBFA4",
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File", color="#262626", font_family="Consolas"),
                on_open=handle_on_open,
                on_close=handle_on_close,
                on_hover=handle_on_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About", font_family="Consolas"),
                        leading=ft.Icon(ft.icons.INFO, color="#ACBFA4"),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}, color={ft.MaterialState.DEFAULT: "#ffffff" ,ft.MaterialState.HOVERED: "#262626"}),
                        on_click=handle_menu_item_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Save", font_family="Consolas"),
                        leading=ft.Icon(ft.icons.SAVE, color="#ACBFA4"),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}, color={ft.MaterialState.DEFAULT: "#ffffff" ,ft.MaterialState.HOVERED: "#262626"}),
                        on_click=handle_menu_item_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Quit", font_family="Consolas"),
                        leading=ft.Icon(ft.icons.CLOSE, color="#ACBFA4"),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}, color={ft.MaterialState.DEFAULT: "#ffffff" ,ft.MaterialState.HOVERED: "#262626"}),
                        on_click=handle_menu_item_click
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("View", color="#262626", font_family="Consolas"),
                on_open=handle_on_open,
                on_close=handle_on_close,
                on_hover=handle_on_hover,
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom", font_family="Consolas"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magnify", font_family="Consolas"),
                                leading=ft.Icon(ft.icons.ZOOM_IN, color="#ACBFA4"),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}, color={ft.MaterialState.DEFAULT: "#ffffff" ,ft.MaterialState.HOVERED: "#262626"}),
                                on_click=handle_menu_item_click
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minify", font_family="Consolas"),
                                leading=ft.Icon(ft.icons.ZOOM_OUT, color="#ACBFA4"),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}, color={ft.MaterialState.DEFAULT: "#ffffff" ,ft.MaterialState.HOVERED: "#262626"}),
                                on_click=handle_menu_item_click
                            )
                        ]
                    )
                ]
            ),
        ]
    )

    page.add(
        ft.Row([menubar]),
    )
    page.update()

ft.app(main)