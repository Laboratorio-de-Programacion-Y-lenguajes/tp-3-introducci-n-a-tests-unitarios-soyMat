"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 0),           #por cero
    (-3, -4, 12),        #dos numeros negativos
    (5, -2, -10),        #un positivo y un negativo
    (7, 1, 7),           #por 1
    (1.5, 2.0, 3.0),     #dos numeros decimales
])
def test_mul_parametrizado(a, b, expected):
    """prueba la funcion mul con varios casos"""
    assert mul(a, b) == expected
