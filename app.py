from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static

class Card(Static):
    """"""

class FinanceApp(App):
    TITLE = "TUI Dashboard"
    CSS_PATH = "app.tcss"
    BINDINGS = [("q" , "quit" , "Salir")]

    def compose(self):
        yield Header()
        with Horizontal(id="cards"):
            yield Card("Saldo\n[b]12.450 €[/b]", id="balance")
            yield Card("Ingresos\n[b]3.200 €[/b]", id="income")
            yield Card("Gastos\n[b]1.850 €[/b]", id="expenses")
        with Horizontal(id="main"):
            yield Static("Tabla", id="transactions" , classes="panel")
            yield Static("Gráfico", id="chart" , classes="panel")
    def on_mount(self):
        self.query_one("#transactions").border_title = "Transacciones"
        self.query_one("#chart").border_title = "Gastos por categoría"

if __name__ == "__main__":
    FinanceApp().run()