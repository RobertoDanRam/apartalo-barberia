import pytest
from apartalo import reglas


@pytest.mark.unitaria
@pytest.mark.parametrize("servicio,esperado", [
    ("corte", 180),
    ("barba", 120),
    ("ambos", 255),
])
def test_precios_base(servicio, esperado):
    assert reglas.calcular_total(servicio) == esperado

