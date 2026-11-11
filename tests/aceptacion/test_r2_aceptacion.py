import pytest
from apartalo import reglas


@pytest.mark.aceptacion
@pytest.mark.parametrize("horas,cargo_esperado", [
    (48, 0),
    (24, 0),
    (23, 100),
    (2, 100),
    (1, 200),
    (0, 200),
])
def test_cancelacion_r2(horas, cargo_esperado):
    # Dado: que una reservación cuesta 200 pesos
    total = 200

    # Cuando: se calcula el cargo de cancelación
    cargo_real = reglas.cargo_cancelacion(total, horas)

    # Entonces: se aplica la penalización correspondiente
    assert cargo_real == cargo_esperado


@pytest.mark.aceptacion
def test_inasistencia_r2():
    # Dado: que existe una reservación de 200 pesos
    total = 200

    # Cuando: el cliente no se presenta a su cita
    cargo_real = reglas.cargo_cancelacion(
        total, inasistencia=True
    )

    # Entonces: se cobra el 100 %
    assert cargo_real == 200
