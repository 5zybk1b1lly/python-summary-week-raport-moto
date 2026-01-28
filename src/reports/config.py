"""Konfiguracja aplikacji."""
from typing import Dict, Any

BG_COLOR = "#f8f9fa"
PRIMARY_COLOR = "#2E86C1"
SUCCESS_COLOR = "#27AE60"
ERROR_COLOR = "#E74C3C"
SECONDARY_COLOR = "#34495E"
ACCENT_COLOR = "#F39C12"
TEXT_COLOR = "#2C3E50"

HEADER_TO_METRIC: Dict[str, str] = {
    'Godziny': 'Ilość godzin',
    'Sprzedaż': 'Sprzedaż',
    'Wartość sztywna': 'Wartość sztywna',
    'Wartość AKC': 'Wartość AKC',
    '% 999': '% dziewiątek IMEI',
    'Realizacja godzin': 'Realizacja godzin',
    'Realizacja obrót': 'Realizacja obrót',
    'Realizacja akc': 'Realizacja akc',
    'Target godziny': 'Target godziny',
    'Target Obrót': 'Target Obrót',
    'Target akcesoria': 'Target akcesoria'
}

MONTHS = ["", "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
          "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
