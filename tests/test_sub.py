"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize(
    "a, b, expected",
    [
        #restar un numero mayor al primero
        (2, 5, -3),
        (1.0, 3.0, -2.0),
        #restar cero
        (10, 0, 10),
        (-5, 0, -5),
        (0.0, 0, 0.0),
        #restar dos numeros negativos
        (-5, -2, -3),
        (-10, -15, 5),
        (-2.5, -1.0, -1.5),
        #restar dos numeros decimales
        (5.5, 2.2, 3.3),
        (10.0, 0.1, 9.9),
    ],
)
def test_sub_parametrizado(a, b, expected):
    """prueba la funcion sub con varios casos"""
    assert sub(a, b) == expected
