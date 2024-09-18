from typing import Callable

import flet as ft


class Splash(ft.View):
    def __init__(self):
        super().__init__(
            route="/",
            padding=0,
        )
        self.expand = True

        self.text = ft.Text(
            value="welcome to the \nmatchmaking \napplication".title(),
            color=ft.colors.WHITE,
            size=25,
            weight=ft.FontWeight.BOLD,
            font_family="Arial"
        )

        self.controls = [
            ft.Container(
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
                            content=self.text,
                            padding=ft.padding.only(top=88)
                        ),
                        ft.Divider(height=165, color=ft.colors.TRANSPARENT),
                        ft.Container(
                            content=ft.CupertinoButton(
                                content=ft.Text(value="LOGIN", color=ft.colors.WHITE, size=15,  weight=ft.FontWeight.BOLD),
                                height=45,
                                width=250,
                                bgcolor="#50BF9E",
                                on_click=lambda e: e.page.go("/login"),
                                expand=True,
                                border_radius=11,
                            )
                        ),
                        ft.Container(
                            border=ft.border.all(color=ft.colors.WHITE, width=1),
                            border_radius=11,
                            content=ft.CupertinoButton(
                                content=ft.Text(value="REGISTER", color=ft.colors.WHITE, size=15, weight=ft.FontWeight.BOLD),
                                height=45,
                                width=250,
                                bgcolor=ft.colors.TRANSPARENT,
                                on_click=lambda e: e.page.go("/reg"),
                                expand=True,
                                border_radius=11,
                            )
                        ),
                        ft.Divider(height=7, color=ft.colors.TRANSPARENT),
                        ft.Container(
                            content=ft.Text(value="Login with", size=12),
                            alignment=ft.alignment.center,
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=25,
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src="facebook.png",
                                        height=40, width=40,
                                        color=ft.colors.WHITE,
                                        expand=True
                                    ),
                                    on_click=lambda e: e.page.launch_url("http://www.facebook.com")
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src="twitter.png",
                                        height=40, width=40,
                                        color=ft.colors.WHITE,
                                        expand=True
                                    ),
                                    on_click=lambda e: e.page.launch_url("http://www.x.com")
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src="gmail.png",
                                        height=40, width=40,
                                        color=ft.colors.WHITE,
                                        expand=True
                                    ),
                                    on_click=lambda e: e.page.launch_url("http://www.gmail.com")
                                )
                            ]
                        )
                    ]
                )
            )
        ]

