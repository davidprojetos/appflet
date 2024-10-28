import flet as ft

def main(page: ft.Page):
    page.title = "App Flet Android"

    def on_button_click(e):
        page.add(ft.Text(f"Olá, {name_field.value}!"))

    name_field = ft.TextField(label="Digite seu nome")
    greet_button = ft.ElevatedButton(text="Cumprimentar", on_click=on_button_click)

    page.add(name_field, greet_button)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
