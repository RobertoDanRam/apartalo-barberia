import pytest
from apartalo import reglas


@pytest.mark.rnf
@pytest.mark.parametrize(
    "total, horas",
    [
        (-1, 2),
        (200, -1),
        (200, None),
    ],
)
def test_rnf_robustez_cancelaciones(total, horas):
    # Dado un total o una anticipación inválidos
    # Cuando se intenta calcular el cargo
    # Entonces se rechaza la entrada con ValueError
    with pytest.raises(ValueError):
        reglas.cargo_cancelacion(total, horas)
