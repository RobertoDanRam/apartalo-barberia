# Entrega — Evidencia 1

> Proyecto: **Apártalo — Barbería Filo**  
> Repositorio: [apartalo-barberia](https://github.com/RobertoDanRam/apartalo-barberia)  
> GitHub Project: [Apártalo — Project #1](https://github.com/users/RobertoDanRam/projects/1)

## Tabla de evidencias y enlaces

| Ejercicio | Qué entrego | Enlace(s) |
|---|---|---|
| 1 | Visión (README) y `docs/01_vision_y_problema.md` | [README.md](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/README.md) · [Visión y problema](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/01_vision_y_problema.md) |
| 2 | Vista del backlog en el Project | [Table — Backlog](https://github.com/users/RobertoDanRam/projects/1/views/1?sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Title&visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%2C442161572%2C442162520%2C442182303%5D) |
| 2 | Un ejemplo de historia (issue) | [H02 — Calcular precio combinado (#2)](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) |
| 2 | `docs/02_backlog.md` | [Backlog documentado](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/02_backlog.md) |
| 3 | Vista de tablero del Project | [Board — Tablero Kanban](https://github.com/users/RobertoDanRam/projects/1/views/2) |
| 3 | `docs/03_tablero.md` | [Tablero Kanban y políticas WIP](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/03_tablero.md) |
| 4 | `docs/04_refinamiento.md` | [Refinamiento, BDD y tabla FIT](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/04_refinamiento.md) |
| 4 | Carpeta `features/` | [Carpeta features](https://github.com/RobertoDanRam/apartalo-barberia/tree/main/features) |
| 4 | La historia que dividí y sus subhistorias | [H07 original (#7)](https://github.com/RobertoDanRam/apartalo-barberia/issues/7) · [H07A (#17)](https://github.com/RobertoDanRam/apartalo-barberia/issues/17) · [H07B (#18)](https://github.com/RobertoDanRam/apartalo-barberia/issues/18) |
| 5 | `docs/05_sprint1.md` | [Planeación y revisión del Sprint 1](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/05_sprint1.md) |
| 5 | Vista del Sprint 1 en el Project | [Table — GitHub Project (filtrar Sprint 1)](https://github.com/users/RobertoDanRam/projects/1/views/1) |
| 6 | `src/apartalo/reglas.py` | [Código de reglas R1 y R2](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/src/apartalo/reglas.py) |
| 6 | Carpeta `tests/` | [Pruebas automatizadas](https://github.com/RobertoDanRam/apartalo-barberia/tree/main/tests) |
| 6 | `docs/06_tdd.md` (con los commits de cada ciclo) | [Documentación TDD](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/06_tdd.md) · [Ciclo 1 ROJO](https://github.com/RobertoDanRam/apartalo-barberia/commit/a4e750d) · [Ciclo 1 VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/1a330c9) · [Ciclo 2 ROJO](https://github.com/RobertoDanRam/apartalo-barberia/commit/ccd22c7) · [Ciclo 2 VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/d52c04a) · [Ciclo 3 ROJO](https://github.com/RobertoDanRam/apartalo-barberia/commit/3b51a59) · [Ciclo 3 VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/8e9374c) |
| 7 | Las tres restricciones (issues RNF) | [RNF01 — Desempeño (#20)](https://github.com/RobertoDanRam/apartalo-barberia/issues/20) · [RNF02 — Robustez (#21)](https://github.com/RobertoDanRam/apartalo-barberia/issues/21) · [RNF03 — Pruebas (#22)](https://github.com/RobertoDanRam/apartalo-barberia/issues/22) |
| 7 | `docs/07_rnf.md` | [Requisitos no funcionales](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/07_rnf.md) |
| 8 | `metricas/tablero.tsv` y `metricas/consultas.sql` | [Fotografía del tablero (TSV)](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/metricas/tablero.tsv) · [Consultas SQL](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/metricas/consultas.sql) |
| 8 | `docs/08_metricas.md` | [Resultados e interpretación de métricas](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/docs/08_metricas.md) |

## Resultados de las pruebas y métricas

**Pruebas automatizadas:**

- Total: 37 pruebas aprobadas.
- Resultado: `37 passed`.
- [Evidencia de pytest](https://github.com/RobertoDanRam/apartalo-barberia/blob/main/evidencias/pytest_rnf.txt).

**Métricas del Sprint 1:**

- Puntos comprometidos: 14.
- Puntos entregados: 11.
- Cumplimiento: 78.57 %.
- Tiempo de ciclo promedio: 0.0 días.
- Historias Must: 8.

La historia H06 permanece en Desarrollo porque todavía falta completar el registro de una cita como inasistencia.

H07 original se cerró al dividirse durante el refinamiento en H07A y H07B, que permanecen pendientes de desarrollo.

## Lista de revisión antes de enviar

- [x] El repositorio es público.
- [x] El Project es público (Settings del Project → Visibility).
- [x] `pytest` termina en verde: 37 pruebas aprobadas.
- [x] Completé el `README.md` con la variante Barbería Filo y el enlace al Project.
- [x] Subí a Canvas un PDF con los enlaces, mi variante y las 7 capturas.