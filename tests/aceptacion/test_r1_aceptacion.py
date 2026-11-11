import pytest
from apartalo import reglas


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "corte,barba,visitas,total_esperado",
    [
        (True, False, 0, 180),
        (False, True, 0, 120),
        (True, True, 4, 255),
        (True, True, 5, 235),
        (True, False, 5, 160),
        (False, True, 5, 100),
    ],
)
def test_total_r1(corte, barba, visitas, total_esperado):
    # Dado: los servicios elegidos y las visitas mensuales
    if corte and barba:
        servicio = "ambos"
    elif corte:
        servicio = "corte"
    else:
        servicio = "barba"

    # Cuando: se calcula el importe del servicio
    total_real = reglas.calcular_total(servicio, visitas)

    # Entonces: el importe coincide con el esperado
    assert total_real == total_esperado
