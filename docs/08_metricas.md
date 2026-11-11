# 8. Métricas: la fotografía de mi tablero

> Ejercicio 8 · Tema 11 · 🎩 Analista

**Proyecto:** Apártalo — Barbería Filo.

**Fecha de la fotografía estática:** 11 de noviembre de 2026.

**Fuente de información:** GitHub Projects, vista Table, mediante la opción **Export view data**.

**Archivo exportado:** `metricas/tablero.tsv`.

**Base de datos SQLite:** `metricas/tablero.db`.

**Consultas SQL:** `metricas/consultas.sql`.

## 8.1 Fotografía estática del tablero

Se exportó una fotografía estática del tablero de GitHub Projects para analizar el avance del Sprint 1 sin depender de modificaciones posteriores a las tarjetas.

El archivo `metricas/tablero.tsv` contiene **21 registros únicos**, sin duplicados, y ocho columnas:

- `titulo`: nombre de la historia o requisito.
- `url`: enlace al Issue de GitHub.
- `estado`: etapa del flujo Kanban.
- `prioridad`: clasificación Must, Should, Could o Won't.
- `puntos`: estimación de la historia.
- `sprint`: sprint al que fue asignada.
- `inicio`: fecha de inicio registrada.
- `terminado`: fecha de finalización registrada.

La información se cargó mediante el comando:

`python metricas/cargar_tablero.py metricas/tablero.tsv`

El programa creó la base SQLite `metricas/tablero.db` y cargó los 21 registros en la tabla `tablero`.

Posteriormente se ejecutaron las consultas de `metricas/consultas.sql` mediante:

`python metricas/cargar_tablero.py metricas/tablero.tsv --sql metricas/consultas.sql`

La fotografía se tomó el **11 de noviembre de 2026**, después del periodo originalmente planificado para el Sprint 1, del 27 de octubre al 9 de noviembre. Por tanto, se documenta la fecha efectiva de exportación y no se presenta como una captura histórica del 9 de noviembre.

La historia original H07 fue cerrada por descomposición durante el refinamiento, ya que sus 13 puntos superaban el límite máximo de 8 puntos por historia. Sus sustitutas, H07A y H07B, aparecen en la fotografía con estimaciones de 5 y 8 puntos respectivamente y pendientes de desarrollo.

## 8.2 Resultados de mis consultas

| Consulta | Resultado |
|---|---|
| a) Puntos comprometidos en el Sprint 1 | **14 puntos** |
| b) Puntos entregados | **11 puntos** |
| c) Porcentaje de cumplimiento | **78.57 %** |
| d) Tiempo de ciclo promedio (días) | **0.0 días** |
| e) Subconjunto: historias Must | **8 historias**, detalladas a continuación |

### a) Puntos comprometidos en el Sprint 1

Se sumaron los puntos de las historias de usuario asignadas al Sprint 1, independientemente de su estado actual.

| Historia | Puntos | Estado |
|---|---:|---|
| H02 — Calcular precio combinado (R1) | 3 | Liberación |
| H03 — Aplicar descuento frecuente (R1) | 3 | Liberación |
| H05 — Calcular cargo de cancelación (R2) | 5 | Liberación |
| H06 — Registrar inasistencias (R2) | 3 | Desarrollo |
| **Total comprometido** | **14** | |

**Resultado de la consulta SQL: 14 puntos.**

Los requisitos no funcionales no se sumaron como puntos de historia, ya que no cuentan con estimación de puntos dentro de la planeación.

### b) Puntos entregados en el Sprint 1

Se consideraron entregadas únicamente las historias que cumplieron dos condiciones:

1. Estar asignadas al Sprint 1.
2. Haber alcanzado la columna **Liberación**.

Las historias entregadas fueron:

| Historia | Puntos entregados |
|---|---:|
| H02 — Calcular precio combinado (R1) | 3 |
| H03 — Aplicar descuento frecuente (R1) | 3 |
| H05 — Calcular cargo de cancelación (R2) | 5 |
| **Total entregado** | **11** |

**Resultado de la consulta SQL: 11 puntos.**

La historia H06 continúa en Desarrollo. Aunque se implementó y comprobó el cargo económico del 100 % por inasistencia, todavía no se ha demostrado el registro completo de una cita como inasistencia, que también forma parte de sus criterios de aceptación.

Por esa razón, H06 no se contabiliza como entregada.

### c) Porcentaje de cumplimiento

El porcentaje de cumplimiento compara los puntos entregados con los puntos originalmente comprometidos.

**Fórmula:**

Porcentaje de cumplimiento = (Puntos entregados / Puntos comprometidos) × 100

**Cálculo:**

(11 / 14) × 100 = **78.57 %**

**Resultado de la consulta SQL: 78.57 %.**

Esto significa que se entregaron 11 de los 14 puntos comprometidos. Los 3 puntos restantes corresponden a la historia H06.

Este porcentaje representa el cumplimiento del compromiso del sprint, no la calificación académica de la evidencia.

### d) Tiempo de ciclo promedio en días

El tiempo de ciclo representa la diferencia entre la fecha de inicio y la fecha de terminación de una historia.

La consulta utilizó la función `julianday()` de SQLite para calcular la diferencia en días, considerando únicamente las historias entregadas del Sprint 1 con ambas fechas registradas.

| Historia | Inicio | Terminado | Tiempo de ciclo |
|---|---|---|---:|
| H02 | 11/11/2026 | 11/11/2026 | 0 días |
| H03 | 11/11/2026 | 11/11/2026 | 0 días |
| H05 | 11/11/2026 | 11/11/2026 | 0 días |
| **Promedio** | | | **0.0 días** |

**Resultado de la consulta SQL: 0.0 días.**

El resultado no significa que las historias se hayan desarrollado instantáneamente. Como los campos `Inicio` y `Terminado` de GitHub Projects registran fechas sin horas, cualquier historia que comience y termine el mismo día tiene una diferencia de cero días.

El historial de Git permite observar horas de trabajo dentro de ese día, pero estas no forman parte del cálculo SQL solicitado.

### e) Subconjunto: historias con prioridad Must

Se consultaron todas las historias de usuario con prioridad **Must**, mostrando su estimación y estado actual.

| Historia | Puntos | Estado |
|---|---:|---|
| H02 — Calcular precio combinado (R1) | 3 | Liberación |
| H03 — Aplicar descuento frecuente (R1) | 3 | Liberación |
| H05 — Calcular cargo de cancelación (R2) | 5 | Liberación |
| H06 — Registrar inasistencias (R2) | 3 | Desarrollo |
| H07A — Seleccionar servicio y horario | 5 | Historias |
| H07B — Validar y registrar una cita | 8 | Historias |
| H09 — Limitar citas por cliente (R3) | 5 | Historias |
| H10 — Limitar citas por horario (R3) | 5 | Historias |

**Resultado de la consulta SQL: 8 historias Must.**

Esta consulta permite identificar las funcionalidades de mayor prioridad y distinguir las ya liberadas de las que todavía están pendientes.

H07A y H07B corresponden a la división de H07 realizada durante el refinamiento. La historia original H07 se conserva en GitHub como referencia histórica de esa decisión, pero no se considera una funcionalidad entregada.

## 8.3 Interpretación de resultados

### ¿Me comprometí de más o de menos?

**Me comprometí de más respecto a la capacidad demostrada durante el Sprint 1.**

Se planificaron 14 puntos distribuidos entre cuatro historias, pero se entregaron 11 puntos correspondientes a tres historias.

El cumplimiento del 78.57 % muestra que fue posible completar la mayor parte del trabajo comprometido, aunque quedó pendiente la historia H06.

La principal lección es que una historia no debe considerarse terminada únicamente porque una parte de su funcionalidad esté implementada.

En el caso de H06, el cálculo de la penalización por inasistencia funciona, pero todavía es necesario demostrar que una cita puede registrarse como inasistencia, según sus criterios de aceptación.

Para el siguiente sprint conviene considerar mejor el esfuerzo de implementación, pruebas y validación completa antes de comprometer una cantidad determinada de puntos.

### ¿Qué historia tardó más y por qué?

**De acuerdo con la métrica SQL, ninguna historia tuvo un tiempo de ciclo mayor que las demás.**

H02, H03 y H05 registran el mismo tiempo de ciclo de 0 días, porque comenzaron y terminaron el 11 de noviembre de 2026.

Como información complementaria, el historial de Git registra estos intervalos entre el primer commit ROJO y el commit VERDE de cada ciclo TDD:

| Historia | Primer commit ROJO | Commit VERDE | Intervalo registrado |
|---|---|---|---|
| H02 | 01:24:53 | 01:27:14 | 2 min 21 s |
| H03 | 01:31:47 | 01:33:26 | 1 min 39 s |
| H05 | 01:39:46 | 01:41:43 | 1 min 57 s |

Dentro de esos intervalos concretos, **H02 presenta el mayor tiempo registrado**, con 2 minutos y 21 segundos, ya que el ciclo incluyó las pruebas y la implementación de los precios de corte, barba y el descuento del servicio combinado.

Sin embargo, estos intervalos entre commits no equivalen al tiempo de ciclo completo de una historia: excluyen preparación, refinamiento, pruebas posteriores y otras actividades.

Por eso, la respuesta basada estrictamente en las fechas del tablero es un empate entre las tres historias entregadas.

Como mejora futura, se recomienda registrar también horas de inicio y terminación para medir con mayor precisión historias desarrolladas durante un mismo día.

### ¿Con cuántos puntos planearía el Sprint 2?

**Planearía inicialmente 10 puntos.**

Durante el Sprint 1 se entregaron 11 puntos, por lo que una planeación de 10 puntos sería más conservadora que repetir el compromiso original de 14.

La propuesta inicial sería:

| Historia | Puntos propuestos | Justificación |
|---|---:|---|
| H06 — Registrar inasistencias (continuación) | 3 | Completar el registro de la cita como inasistencia y verificar sus criterios de aceptación |
| H09 — Limitar citas por cliente (R3) | 5 | Incorporar una restricción importante de la agenda |
| H01 — Consultar servicios y precios | 2 | Habilitar una consulta básica de servicios para el cliente |
| **Total propuesto** | **10** | |

Esta distribución es una propuesta para el refinamiento y no significa que las tres historias ya estén formalmente comprometidas para el Sprint 2.

La historia H06 conserva aquí su estimación original de 3 puntos como referencia de planeación. Antes de confirmar el nuevo compromiso se debe revisar el trabajo que permanece pendiente.

La capacidad observada en el Sprint 1 sirve como punto de partida, aunque deberá ajustarse con los resultados de los siguientes sprints.

## 8.4 Conclusión

La fotografía estática de GitHub Projects permitió analizar el estado de 21 registros únicos mediante consultas SQL en SQLite.

Los resultados del Sprint 1 fueron:

- **14 puntos comprometidos.**
- **11 puntos entregados.**
- **78.57 % de cumplimiento.**
- **0.0 días de tiempo de ciclo promedio**, debido a la precisión por fechas de los campos utilizados.
- **8 historias de usuario clasificadas como Must.**

La principal conclusión es que se debe mejorar la estimación del trabajo y verificar todos los criterios de aceptación antes de declarar terminada una historia.

Para el Sprint 2 se propone una planeación inicial de 10 puntos, priorizando la finalización de H06 y nuevas funcionalidades relacionadas con la consulta de servicios y la agenda.

Los resultados se obtuvieron mediante `metricas/consultas.sql` sobre la fotografía `metricas/tablero.tsv`, conservando ambas como evidencia reproducible del análisis.