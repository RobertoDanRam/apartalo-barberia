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
