import flet as ft
from anyio import value


class Verification(ft.View):
    def __init__(self):
        super().__init__(
            route="/verif",
            padding=0,
        )
        self.expand = True

        self.__icon_verif = ft.Image(src="check.png", height=32, width=32)

        self.__email_verif = ft.Text(
            value="Email Verification!",
            color=ft.colors.BLACK,
            size=15,
            weight=ft.FontWeight.BOLD,
            font_family="Arial",
        )

        self.__text = ft.Text(
            value=" Please check your email inbox to \nconfirm and complete your details\n after logging in the application, \n                  thank you",
            color=ft.colors.BLACK,
            size=12

        )

        self.__btn = ft.ElevatedButton(
            content=ft.Text("OK", color=ft.colors.WHITE, size=12),
            color=ft.colors.WHITE,
            bgcolor="#F4B742",
            width=70,
            height=27,
            on_click=lambda e: e.page.go("/")

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
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=290, height=270,
                            margin=ft.margin.only(top=150),
                            padding=ft.padding.only(left=20, right=20, top=40),
                            border_radius=15,
                            bgcolor=ft.colors.WHITE,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    self.__icon_verif,
                                    self.__email_verif,
                                    self.__text,
                                    ft.Divider(color=ft.colors.TRANSPARENT, height=15),
                                    self.__btn
                                ]
                            )
                        )
                    ]
                )
            )
        ]

