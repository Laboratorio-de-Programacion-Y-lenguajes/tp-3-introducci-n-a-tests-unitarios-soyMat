"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 2.5),         # division que da decimal
    (-10, 2, -5.0),      # division con numeros negativos
])
def test_div_parametrizado(a, b, expected):
    """prueba la funcion div con casos normales"""
    assert div(a, b) == expected


def test_div_por_cero():
    """tiene que lanzar ZeroDivisionError si dividimos por cero"""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
