"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---

@pytest.mark.parametrize("values, expected", [
    ([5], 5.0),                # lista con un solo elemento  
    ([-2, -4, -6], -4.0),      # numeros negativos
    ([1.5, 2.5, 5.0], 3.0),    # numeros decimales
])
def test_mean_parametrizado(values, expected):
    """prueba la funcion mean con listas de distintos tipos"""
    assert mean(values) == expected


def test_mean_lista_vacia():
    """lanza ValueError si le pasamos una lista vacia"""
    with pytest.raises(ValueError):
        mean([])
