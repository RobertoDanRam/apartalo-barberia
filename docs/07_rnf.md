# 7. Requisitos no funcionales

> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador

> Cada restricción se registró como un Issue mediante el formulario **Requisito no funcional**. A continuación se presenta el resumen de las tres restricciones SMART de Barbería Filo.

## 7.1 Restricciones SMART

Para definir las restricciones se consideró la hora pico de Barbería Filo: **sábados de 10:00 a 14:00, con hasta 40 solicitudes de reserva por hora y tres sillas disponibles**.

Cada restricción establece una condición específica, medible, alcanzable, relevante y trazable a una historia del Product Backlog.

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| [RNF01 — #20](https://github.com/RobertoDanRam/apartalo-barberia/issues/20) | Durante la hora pico de los sábados, de 10:00 a 14:00, al menos 38 de cada 40 consultas de precios deberán responder en un máximo de 1 segundo. | Externa | Desempeño | [H02 — #2](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) | **Tabla 2:** medir el tiempo de respuesta e inspeccionar los recursos utilizados mediante una prueba de carga. |
| [RNF02 — #21](https://github.com/RobertoDanRam/apartalo-barberia/issues/21) | La función `cargo_cancelacion()` deberá rechazar mediante `ValueError` el 100 % de los tres casos inválidos definidos: importe negativo, horas negativas y horas ausentes. | Externa | Robustez | [H05 — #5](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | **Tabla 2:** comprobar el comportamiento ante entradas inválidas mediante pruebas automatizadas con pytest. |
| [RNF03 — #22](https://github.com/RobertoDanRam/apartalo-barberia/issues/22) | Antes de integrar cambios a R2 en `main`, las pruebas deberán recorrer el 100 % de las seis salidas `return` y `raise` identificadas en `cargo_cancelacion()`. | Interna | Pruebas | [H05 — #5](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | **Tabla 4:** adoptar pruebas de cobertura y la práctica Red–Green–Refactor. |

## 7.2 Clasificación y trazabilidad

**RNF01 — Desempeño**

Es una cualidad externa porque afecta el tiempo que espera el cliente para obtener información de los servicios durante la hora pico.

Se relaciona con H02, ya que el cálculo del precio combinado debe ofrecer una respuesta oportuna incluso cuando aumenta la demanda.

La restricción se comprobará cuando exista un flujo de consultas de la aplicación que permita simular las solicitudes y medir sus tiempos de respuesta.

**RNF02 — Robustez**

Es una cualidad externa porque determina cómo responde el sistema ante datos inválidos introducidos durante el cálculo de una cancelación.

Se relaciona con H05, ya que un importe negativo o unas horas de anticipación incorrectas no deben producir un cargo válido.

La restricción se comprueba mediante tres casos automatizados que esperan una excepción `ValueError`.

**RNF03 — Pruebas**

Es una cualidad interna porque busca que el código sea verificable y que los errores puedan reproducirse y detectarse cuando se modifica la implementación.

Se relaciona con H05 porque la función de cancelaciones tiene distintas condiciones y resultados que deben mantenerse correctos.

Se adopta la práctica de pruebas de cobertura y Red–Green–Refactor, utilizando los casos unitarios y de regresión desarrollados durante el Ejercicio 6.

La revisión manual de las seis salidas de `cargo_cancelacion()` se encuentra documentada en [06_tdd.md](06_tdd.md).

## 7.3 La que compruebo con código

- **Restricción:** [RNF02 — Robustez ante entradas inválidas (#21)](https://github.com/RobertoDanRam/apartalo-barberia/issues/21).
- **Cualidad:** Externa — Robustez.
- **Historia relacionada:** [H05 — Calcular cargo de cancelación (#5)](https://github.com/RobertoDanRam/apartalo-barberia/issues/5).
- **Prueba:** `tests/rnf/test_robustez.py`.
- **Marca de pytest:** `@pytest.mark.rnf`.

**Objetivo:**

Verificar que el 100 % de los tres casos inválidos definidos sean rechazados mediante `ValueError`.

**Casos ejecutados:**

| Caso | Entrada | Resultado esperado | Resultado real |
|---|---|---|---|
| 1 | `cargo_cancelacion(-1, 2)` | `ValueError` |  Aprobado |
| 2 | `cargo_cancelacion(200, -1)` | `ValueError` |  Aprobado |
| 3 | `cargo_cancelacion(200, None)` | `ValueError` |  Aprobado |

**Comando de ejecución:**

`python -m pytest tests/rnf/test_robustez.py -v`

**Resultado obtenido:**

`3 passed in 0.16s`

Por lo tanto, se cumplió la restricción para los tres casos definidos:

**3 / 3 × 100 = 100 % de casos aprobados.**

Posteriormente se ejecutó toda la suite mediante:

`python -m pytest -v`

**Resultado final:**

`37 passed in 0.15s`

Las 37 pruebas incluyen los casos unitarios, de aceptación, de regresión, de humo y los tres nuevos casos de requisitos no funcionales.

**Evidencia:** [Resultados completos de pytest](../evidencias/pytest_rnf.txt).

La prueba confirma la robustez frente a los tres casos definidos. No representa una comprobación exhaustiva de todas las entradas inválidas posibles.

## 7.4 Una por sprint

**La que agrego a mi DoD en el Sprint 1:**

[RNF02 — Robustez ante entradas inválidas (#21)](https://github.com/RobertoDanRam/apartalo-barberia/issues/21).

Se agrega a la Definición de Terminado el siguiente criterio:

> La regla R2 debe rechazar mediante `ValueError` los tres casos de entradas inválidas definidos para RNF02. Las tres pruebas automatizadas deben aprobarse antes de considerar terminada la funcionalidad de cálculo de cancelaciones.

Se eligió esta restricción porque se relaciona directamente con H05, una historia implementada durante el Sprint 1.

Además, la validación de datos ya estaba presente en la función `cargo_cancelacion()`, por lo que fue posible comprobarla mediante pytest sin modificar las reglas de negocio.

**Las que dejo para después y por qué:**

**RNF01 — Desempeño (#20): Sprint 2.**

Se deja para un sprint posterior porque actualmente se dispone de funciones de cálculo en Python, pero todavía no se cuenta con un flujo completo de solicitudes de reserva que permita medir los tiempos de respuesta bajo la demanda de hora pico.

Cuando exista ese flujo, se realizará una prueba de carga con 40 solicitudes por hora y se comprobará que al menos 38 respondan en un máximo de 1 segundo.

**RNF03 — Pruebas (#22): Sprint 2.**

Aunque durante el Ejercicio 6 se verificaron las seis salidas de la función de cancelaciones, se propone adoptar formalmente esta comprobación como una práctica recurrente para los cambios futuros.

En el siguiente sprint se revisará que las pruebas continúen cubriendo las seis salidas identificadas y se actualizarán los casos cuando se modifique la función.

**Conclusión:**

Se definieron tres restricciones SMART, dos externas y una interna. Todas cuentan con un valor medible, una historia relacionada y una práctica de verificación correspondiente a las Tablas 2 o 4 del Tema 9.

La restricción RNF02 fue comprobada mediante código, obteniendo tres casos aprobados de tres ejecutados. La suite completa del proyecto terminó con 37 pruebas aprobadas y ninguna fallida.