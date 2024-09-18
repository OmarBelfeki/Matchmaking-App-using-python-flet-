import flet as ft


class Login(ft.View):
    def __init__(self):
        super().__init__(
            route="/login",
            padding=0,
        )
        self.expand = True

        self.text = ft.Text(
            value="    Login",
            color=ft.colors.WHITE,
            size=25,
            weight=ft.FontWeight.BOLD,
            font_family="Arial",
        )

        self.text_hello = ft.Text(
            value="    Hello, Welcome back",
            color="#E9C8F1",
            size=11,
        )

        self.controls = [
            ft.Container(
                padding=20,
                width=290, height=637,
                gradient=ft.LinearGradient(
                    colors=["#8C2581", "#272662"],
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right
                ),
                content=ft.Column(
                    #horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Container(
                            content=ft.Column([self.text, self.text_hello]),
                            padding=ft.padding.only(top=77)
                        ),
                        ft.Divider(height=30, color=ft.colors.TRANSPARENT),
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            border=ft.border.all(width=1, color=ft.colors.WHITE),
                            border_radius=11,
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Text(value="Username", color=ft.colors.BLACK38),
                                    self.__text_field(),
                                    ft.Text(value="Password", color=ft.colors.BLACK38),
                                    self.__text_field(password=True),
                                    ft.Divider(color=ft.colors.TRANSPARENT, height=15),
                                    ft.Container(
                                        content=ft.CupertinoButton(
                                            content=ft.Text(value="Continue", color=ft.colors.WHITE, size=13,
                                                            weight=ft.FontWeight.BOLD),
                                            height=43,
                                            width=250,
                                            bgcolor="#50BF9E",
                                            on_click=lambda e: e.page.go("/verif"),
                                            expand=True,
                                            border_radius=11,
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=-5,
                                    controls=[
                                        ft.Checkbox(),
                                        ft.Text(value="Remember Me ?", size=9)
                                    ]
                                ),
                                ft.TextButton(
                                    content=ft.Text("Forgot Password", size=9),
                                    style=ft.ButtonStyle(
                                        overlay_color=ft.colors.TRANSPARENT,
                                        color=ft.colors.WHITE
                                    ),
                                    on_click=lambda e: e.page.go("/reg")
                                ),
                            ]
                        ),
                        ft.Divider(color=ft.colors.TRANSPARENT, height=9),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=0,
                            controls=[
                                ft.Text(value="Not member yet?", size=9),
                                ft.TextButton(
                                    content=ft.Text("Join Now", color=ft.colors.YELLOW, size=9),
                                    on_click=lambda e: e.page.go("/reg")
                                )
                            ]
                        )
                    ]
                )
            )
        ]

    @staticmethod
    def __text_field(password: bool = False) -> ft.TextField:
        return ft.TextField(
            height=35,
            border_radius=11,
            border_color=ft.colors.GREY,
            border_width=2,
            cursor_height=22,
            text_style=ft.TextStyle(
                color=ft.colors.BLACK38,
            ),
            text_vertical_align=ft.VerticalAlignment.START,
            password=password,
            can_reveal_password=password
        )