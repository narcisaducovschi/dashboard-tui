from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import DataTable, Footer, Header, Static
from rich.text import Text
from data import TRANSACTIONS

def format_eur(amount: float) -> str:
    text = f"{amount:+,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} €"

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
            yield DataTable(id="transactions", classes="panel")
            yield Static("Gráfico", id="chart" , classes="panel")

    def on_mount(self):
        self.query_one("#chart").border_title = "Gastos por categoría"

        table = self.query_one("#transactions", DataTable)
        table.border_title = "Transacciones"
        table.cursor_type = "row"
        table.zebra_stripes = True

        table.add_columns("Fecha" , "Concepto" , "Categoría" , "Importe")
        for day, concept, category, amount in TRANSACTIONS:
            color = "green" if amount > 0 else "red"
            table.add_row(
                day.strftime("%d/%m"),
                concept,
                category,
                Text(format_eur(amount), style=color, justify="right"),
            )

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        self.notify(f"Row {event.cursor_row} selected")

        
if __name__ == "__main__":
    FinanceApp().run()