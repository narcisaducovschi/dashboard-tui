from textual.app import App, ComposeResult
from textual.widgets import Header , Footer, Static

class FinanceApp(App):
    TITLE = "TUI Dashboard"
    BINDINGS = [("q" , "quit" , "Salir")]

    def compose(self):
        yield Header()
        yield Static()
        yield Footer()

if __name__ == "__main__":
    FinanceApp().run()