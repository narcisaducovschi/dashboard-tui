from datetime import date

TRANSACTIONS = [
    (date(2026, 9, 28), "Nómina septiembre", "Ingresos", 3200.00),
    (date(2026, 9, 27), "Mercadona", "Alimentación", -84.35),
    (date(2026, 9, 25), "Alquiler", "Vivienda", -750.00),
    (date(2026, 9, 24), "Netflix", "Ocio", -12.99),
    (date(2026, 9, 22), "Gasolina", "Transporte", -58.20),
    (date(2026, 9, 20), "Restaurante", "Ocio", -45.50),
    (date(2026, 9, 18), "Factura luz", "Vivienda", -67.80),
    (date(2026, 9, 15), "Freelance web", "Ingresos", 450.00),
    (date(2026, 9, 12), "Farmacia", "Salud", -23.10),
    (date(2026, 9, 10), "Gimnasio", "Salud", -35.00),
]

from collections import defaultdict


def totals(transactions=TRANSACTIONS):
    income = sum(a for *_, a in transactions if a > 0)
    expenses = -sum(a for *_, a in transactions if a < 0)
    return income, expenses, income - expenses


def expenses_by_category(transactions=TRANSACTIONS):
    result = defaultdict(float)
    for _, _, category, amount in transactions:
        if amount < 0:
            result[category] += -amount
    return dict(sorted(result.items(), key=lambda kv: kv[1], reverse=True))