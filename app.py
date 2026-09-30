from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import DataTable, Footer, Header, Static
from rich.text import Text
from charts import BarChart
from data import TRANSACTIONS, expenses_by_category, totals

def format_eur(amount: float, sign: bool = True) -> str:
    text = f"{amount:+,.2f}" if sign else f"{amount:,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} €"

class Card(Static):
    """"""

class FinanceApp(App):
    TITLE = "TUI Dashboard"
    CSS_PATH = "app.tcss"
    BINDINGS = [("q" , "quit" , "Salir")]

    def compose(self) -> ComposeResult:
        income, expenses, balance = totals()
        yield Header()
        with Horizontal(id="cards"):
            yield Card(f"Saldo\n[b]{format_eur(balance, sign=False)}[/b]", id="balance")
            yield Card(f"Ingresos\n[b]{format_eur(income, sign=False)}[/b]", id="income")
            yield Card(f"Gastos\n[b]{format_eur(expenses, sign=False)}[/b]", id="expenses")
        with Horizontal(id="main"):
            yield DataTable(id="transactions", classes="panel")
            yield BarChart(expenses_by_category(), id="chart", classes="panel")
        yield Footer()

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