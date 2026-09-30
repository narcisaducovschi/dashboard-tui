from rich.text import Text
from textual.widget import Widget

COLORS = ["red", "orange1", "yellow", "green", "cyan", "magenta"]


class BarChart(Widget):
    """Horizontal bar chart drawn with text."""

    def __init__(self, data: dict[str, float], **kwargs) -> None:
        super().__init__(**kwargs)
        self.data = data

    def render(self) -> Text:
        if not self.data:
            return Text("Sin datos")

        label_width = max(len(label) for label in self.data)
        max_value = max(self.data.values())
        total = sum(self.data.values())
        bar_space = max(self.size.width - label_width - 12, 1)

        text = Text()
        for i, (label, value) in enumerate(self.data.items()):
            length = max(round(value / max_value * bar_space), 1)
            text.append(f"{label:<{label_width}} ", style="bold")
            text.append("█" * length, style=COLORS[i % len(COLORS)])
            text.append(f" {value / total:>4.0%}\n")
        return text