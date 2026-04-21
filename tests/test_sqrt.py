"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---

@pytest.mark.parametrize("x, expected", [
    (0, 0.0),            #raiz de 0
    (2.25, 1.5),         #raiz de un numero que no da entero
])
def test_sqrt_parametrizado(x, expected):
    """prueba la funcion sqrt con distintos casos"""
    assert sqrt(x) == expected


def test_sqrt_negativo():
    """lanza ValueError si le pasamos un numero negativo"""
    with pytest.raises(ValueError):
        sqrt(-4)
