__author__ = "Omar Belfeki"
__copyright__ = "Copyright 2024-09-18, The Management App using python(flet)"

import flet as ft

from views.login import Login
from views.splash import Splash
from views.verification import Verification
from views.register import Register


def main(page: ft.Page) -> None:
    page.window.height = 637
    page.window.width = 290
    # page.window.top = 1
    # page.window.left = 1000
    page.window.always_on_top = True


    def router(route: str) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(Splash())
            case "/login":
                page.views.append(Login())
            case "/verif":
                page.views.append(Verification())
            case "/reg":
                page.views.append(Register())
        page.update()

    page.on_route_change = router
    page.go("/")
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")