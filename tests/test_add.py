"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (-2, -3, -5),        # sumar dos numeros negativos
    (5, -2, 3),          # sumar un positivo y un negativo
    (5, 0, 5),           # sumar con cero
    (1.5, 2.5, 4.0),     # sumar dos numeros decimales
])
def test_add_parametrizado(a, b, expected):
    """prueba la funcion add con varios casos"""
    assert add(a, b) == expected
