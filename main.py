import flet as ft

def main(page: ft.Page):
    page.title = "Meu App Flet"
    
    # Função para manipular o clique do botão
    def button_clicked(e):
        page.controls.append(ft.Text("Olá, Flet!"))
        page.update()
    
    # Adiciona um botão à página
    btn = ft.ElevatedButton("Clique aqui", on_click=button_clicked)
    
    page.add(btn)

# Inicializa o app Flet
ft.app(target=main)