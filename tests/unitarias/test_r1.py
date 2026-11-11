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

# se agrega la regla que dice si el cliente tiene cinco o más visitas al mes, recibe $20 de descuento en el total de su servicio 
@pytest.mark.unitaria
@pytest.mark.parametrize("servicio,visitas,esperado", [
    ("ambos", 4, 255),
    ("ambos", 5, 235),
    ("corte", 5, 160),
    ("barba", 5, 100),
])
def test_cliente_frecuente(servicio, visitas, esperado):
    assert reglas.calcular_total(servicio, visitas) == esperado

# Verificar entradas inválidas para R1

@pytest.mark.unitaria
@pytest.mark.parametrize("servicio,visitas", [
    ("tinte", 0),
    ("corte", -1),
])
def test_r1_rechaza_datos_invalidos(servicio, visitas):
    with pytest.raises(ValueError):
        reglas.calcular_total(servicio, visitas)
