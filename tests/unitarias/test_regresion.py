import pytest
from apartalo import reglas


@pytest.mark.unitaria
@pytest.mark.regresion
def test_exactamente_24_horas_no_cobra():
    assert reglas.cargo_cancelacion(200, 24) == 0
