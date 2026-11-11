# 6. Pruebas de aceptación y TDD

**Ejercicio 6 · Tema 8 ·  Desarrollador**

## 6.1 Implementación de las reglas de negocio

Se implementaron las reglas de negocio R1 y R2 de Apártalo — Barbería Filo mediante funciones de Python en `src/apartalo/reglas.py`.

**Regla R1 — Cálculo del total del servicio**

La función `calcular_total()` determina el importe de los servicios:

- Corte de cabello: $180.
- Arreglo de barba: $120.
- Corte y barba combinados: 15 % de descuento, con un total de $255.
- Cliente frecuente con cinco visitas mensuales o más: descuento adicional de $20.

Para un cliente frecuente que reserva ambos servicios, el total es de $235.

**Regla R2 — Cancelaciones e inasistencias**

La función `cargo_cancelacion()` calcula los cargos según la anticipación:

- 24 horas o más: 0 %.
- Desde 2 horas hasta menos de 24 horas: 50 %.
- Menos de 2 horas: 100 %.
- Inasistencia: 100 %.

Las funciones validan las entradas y lanzan `ValueError` ante datos inválidos, como servicios inexistentes, visitas negativas, importes negativos u horas de anticipación incorrectas.

## 6.2 Mis ciclos de TDD

Se realizaron tres ciclos de desarrollo guiado por pruebas (TDD), siguiendo la secuencia ROJO → VERDE.

En cada ciclo primero se escribieron pruebas que fallaban porque la funcionalidad todavía no estaba implementada. Posteriormente se agregó el código necesario para que pasaran.

Los commits se registraron el 11 de noviembre de 2026.

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) | Qué aprendí |
|---|---|---|---|---|
| 1 — Precios base y combo | [a4e750d — Pruebas de precios](https://github.com/RobertoDanRam/apartalo-barberia/commit/a4e750d) | [1a330c9 — Implementar precios](https://github.com/RobertoDanRam/apartalo-barberia/commit/1a330c9) | No hubo commit de refactorización independiente | Escribir primero los casos de prueba permitió comprobar los precios individuales y el descuento combinado del 15 %. |
| 2 — Cliente frecuente | [ccd22c7 — Pruebas de descuento](https://github.com/RobertoDanRam/apartalo-barberia/commit/ccd22c7) | [d52c04a — Aplicar descuento](https://github.com/RobertoDanRam/apartalo-barberia/commit/d52c04a) | No hubo commit de refactorización independiente | Probar cuatro y cinco visitas permitió verificar que el descuento adicional se aplica al alcanzar el límite establecido. |
| 3 — Cancelaciones | [3b51a59 — Pruebas de cancelación](https://github.com/RobertoDanRam/apartalo-barberia/commit/3b51a59) | [8e9374c — Calcular cargos](https://github.com/RobertoDanRam/apartalo-barberia/commit/8e9374c) | No hubo commit de refactorización independiente | Evaluar los límites de 24 y 2 horas permitió verificar los porcentajes de penalización y el cargo por inasistencia. |

**Secuencia registrada en Git:**

1. ROJO: probar precios de corte, barba y combo — `a4e750d`.
2. VERDE: calcular precios base y descuento combinado — `1a330c9`.
3. ROJO: probar descuento de cliente frecuente — `ccd22c7`.
4. VERDE: aplicar descuento adicional desde cinco visitas — `d52c04a`.
5. ROJO: probar límites de cancelación e inasistencias — `3b51a59`.
6. VERDE: calcular cargos según anticipación e inasistencia — `8e9374c`.

Los commits conservan la trazabilidad entre las pruebas escritas y las implementaciones que permiten superarlas.

## 6.3 Pruebas unitarias

Las pruebas unitarias se encuentran en:

- `tests/unitarias/test_r1.py`
- `tests/unitarias/test_r2.py`
- `tests/unitarias/test_regresion.py`

Se utiliza la marca `@pytest.mark.unitaria` para identificar las pruebas unitarias.

