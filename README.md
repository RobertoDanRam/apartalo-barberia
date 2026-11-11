# Apártalo — Barbería Filo

Repositorio de la **Evidencia 1** de *Proyecto de ingeniería de software* (Tecmilenio, CRN 13241).

| Dato | |
|---|---|
| Estudiante | ROBERTO DANIEL RAMOS FLORES |
| Matrícula | T02966616 |
| Variante | 1 — Barbería Filo |
| Project (tablero) | [Apártalo — Barbería Filo](https://github.com/users/RobertoDanRam/projects/1/views/1) |

## Visión del producto

Apártalo — Barbería Filo es un sistema de reservaciones para una barbería ubicada en la colonia Narvarte, Ciudad de México.

Su propósito es facilitar la gestión de citas y reducir las pérdidas ocasionadas por cancelaciones tardías y clientes que no se presentan.

Permitirá consultar los precios de los servicios, calcular descuentos para clientes frecuentes y aplicar las reglas de cancelación establecidas por el negocio.

Con ello, se busca mejorar la organización de la barbería y ofrecer mayor claridad a los clientes al reservar.

## Mi equipo Scrum (los tres sombreros)

| Sombrero | Lo que hago con él en este proyecto |
|---|---|
| 🎩 PO | Identifico las necesidades de Don Rogelio, defino las historias de usuario, organizo el product backlog y establezco las prioridades. |
| 🎩 SM | Organizo el Sprint 1, administro el tablero Kanban, superviso el avance y registro los impedimentos para resolverlos. |
| 🎩 Desarrollador | Implemento las reglas de precios y cancelaciones en Python, desarrollo pruebas con pytest y documento los resultados. |

## Cómo está organizado este repositorio

| Carpeta o archivo | Qué contiene | Ejercicio |
|---|---|---|
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues `historia` y `epica` + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues `rnf` + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas

En Windows, desde PowerShell, dentro de la carpeta del proyecto:

```powershell
py -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt

python -m pytest

python -m pytest -m aceptacion

python -m pytest -m unitaria

python -m pytest -m rnf
```
