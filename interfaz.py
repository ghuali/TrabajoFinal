from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Container


class ThreeButtonsApp(App):
    def compose(self) -> ComposeResult:
        # Crear un contenedor para los botones
        with Container():
            yield Button("Botón 1", id="button1")
            yield Button("Botón 2", id="button2")
            yield Button("Botón 3", id="button3")
