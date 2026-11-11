import pytest
from apartalo import reglas


@pytest.mark.unitaria
@pytest.mark.parametrize("horas,esperado", [
    (48, 0),
    (24, 0),
    (23, 100),
    (2, 100),
    (1, 200),
    (0, 200),
])
def test_cargos_cancelacion(horas, esperado):
    assert reglas.cargo_cancelacion(200, horas) == esperado


@pytest.mark.unitaria
def test_inasistencia():
    assert reglas.cargo_cancelacion(
        200, inasistencia=True
    ) == 200


@pytest.mark.unitaria
@pytest.mark.parametrize("total,horas", [
    (-1, 2),
    (200, -1),
    (200, None),
])
def test_r2_rechaza_datos_invalidos(total, horas):
    with pytest.raises(ValueError):
        reglas.cargo_cancelacion(total, horas)
