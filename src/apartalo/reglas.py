def calcular_total(servicio: str, visitas_mes: int = 0) -> int:
    if servicio not in ("corte", "barba", "ambos"):
        raise ValueError("Servicio no válido")

    if (
        not isinstance(visitas_mes, int)
        or isinstance(visitas_mes, bool)
        or visitas_mes < 0
    ):
        raise ValueError("Las visitas deben ser un entero no negativo")

    if servicio == "ambos":
        precio = round((180 + 120) * 0.85)
    elif servicio == "corte":
        precio = 180
    else:
        precio = 120

    if visitas_mes >= 5:
        return precio - 20

    return precio

# función cargo cancelación

def cargo_cancelacion(
    total: float,
    horas_anticipacion: float | None = None,
    inasistencia: bool = False,
) -> float:
    if (
        not isinstance(total, (int, float))
        or isinstance(total, bool)
        or total < 0
    ):
        raise ValueError("El total debe ser un número no negativo")

    if inasistencia:
        return total

    if (
        not isinstance(horas_anticipacion, (int, float))
        or isinstance(horas_anticipacion, bool)
        or horas_anticipacion < 0
    ):
        raise ValueError("Las horas deben ser un número no negativo")

    if horas_anticipacion >= 24:
        return 0

    if horas_anticipacion >= 2:
        return total * 0.50

    return total
