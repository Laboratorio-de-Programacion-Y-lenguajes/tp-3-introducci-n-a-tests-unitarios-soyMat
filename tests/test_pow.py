"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 1),           #numero elevado a 0 da 1
    (7, 1, 7),           #numero elevado a 1 da el mismo numero
    (-2, 2, 4),          #base negativa con exponente par da positivo
    (9, 0.5, 3.0),       #exponente decimal para la raiz cuadrada
])
def test_pow_parametrizado(a, b, expected):
    """prueba la funcion pow_ con varios casos"""
    assert pow_(a, b) == expected
