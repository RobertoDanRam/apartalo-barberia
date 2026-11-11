# 5. Sprint 1 (27 oct – 9 nov 2026)

**Ejercicio 5 · Temas 4 y 11**

**Proyecto:** Apártalo — Barbería Filo

**Nota sobre la ejecución:** El periodo indicado en la plantilla del curso es del 27 de octubre al 9 de noviembre de 2026. La evidencia de trabajo disponible también incluye actividades realizadas los días 10 y 11 de noviembre, después del periodo planificado. Se conservan las fechas reales de los commits y las pruebas.

## A. Planeación del sprint

**🎩 SM facilita · 🎩 PO presenta · 🎩 Desarrollador se compromete**

**Objetivo del sprint:**

Implementar y validar mediante Python y pytest las reglas R1 y R2 de Barbería Filo, incluyendo el cálculo de precios, descuentos y cargos por cancelaciones e inasistencias.

**Capacidad en horas (Figura 2 del Tema 11):**

La siguiente tabla contiene la estimación preliminar utilizada para planear el trabajo. Las horas deben contrastarse con la disponibilidad personal real.

| Concepto | Horas |
|---|---:|
| Horas disponibles en las dos semanas | 56 (estimación preliminar) |
| − Otras actividades (clases, trabajo, tareas) | 24 (estimación preliminar) |
| = Disponibilidad | 32 |
| ÷ 2 = **Capacidad estimada** | **16** |

**Operación:** (56 − 24) / 2 = **16 horas estimadas**.

**Compromiso (historias del Sprint 1):**

| Historia | Puntos | Horas estimadas |
|---|---:|---:|
| [H02 — Calcular precio combinado](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) | 3 | 3 |
| [H03 — Aplicar descuento frecuente](https://github.com/RobertoDanRam/apartalo-barberia/issues/3) | 3 | 3 |
| [H05 — Calcular cargo de cancelación](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | 5 | 5 |
| [H06 — Registrar inasistencias](https://github.com/RobertoDanRam/apartalo-barberia/issues/6) | 3 | 3 |
| **Total** | **14** | **14** |

Las historias seleccionadas cubren las reglas R1 y R2.

El esfuerzo propuesto de 14 horas no supera la capacidad preliminar de 16 horas. La planeación deja un margen de 2 horas.

La carga máxima por historia es de 8 puntos, según el refinamiento del Ejercicio 4. Todas las historias comprometidas están dentro de ese límite.

**Definición de Terminado (DoD):**

1. La funcionalidad se encuentra implementada correctamente en `src/apartalo/reglas.py`.
2. Las pruebas unitarias y de aceptación correspondientes pasan con pytest.
3. El código está integrado en la rama `main` y los cambios están registrados mediante commits de Git.
4. Todos los criterios de aceptación de la historia se cumplen.
5. No existen defectos críticos pendientes y se conserva evidencia de los resultados obtenidos.

**DoD vs. criterios de aceptación (con un ejemplo de mi backlog):**

Los criterios de aceptación establecen las condiciones específicas que debe cumplir una historia de usuario. En cambio, la Definición de Terminado establece las condiciones generales de calidad que debe cumplir cualquier historia antes de considerarse entregada.

Por ejemplo, H02 exige que al reservar corte ($180) y barba ($120) juntos se aplique un descuento del 15 %, dando un total de $255.

Cumplir ese cálculo satisface el criterio funcional, pero para cumplir la DoD también es necesario implementar el código, ejecutar las pruebas correspondientes, registrar los cambios en GitHub y verificar que no queden defectos críticos.

## B. Junta diaria — bitácora

**🎩 Desarrollador responde · 🎩 SM anota impedimentos**

Los registros siguientes documentan jornadas respaldadas por actividades y commits disponibles. No se presentan seis reuniones ficticias en días distintos.

### 10 de noviembre de 2026

- **¿Qué hice?** Trabajé en la documentación y preparación de Barbería Filo. Registré las historias y sus enlaces, completé el tablero Kanban con políticas y límites WIP, preparé el refinamiento y agregué el boceto de servicios al repositorio.
- **¿Qué haré?** Implementar las reglas R1 y R2 mediante pruebas unitarias, siguiendo ciclos ROJO → VERDE.
- **¿Qué me lo impide?** No se identifica un impedimento de esta jornada en los registros disponibles.

**Evidencia:** [Historial de commits](https://github.com/RobertoDanRam/apartalo-barberia/commits/main/).

### 11 de noviembre de 2026

- **¿Qué hice?** Implementé las reglas R1 y R2 con tres ciclos de TDD. Creé pruebas unitarias y de aceptación, comprobé entradas inválidas y ejecuté una prueba de regresión para el límite de 24 horas. La suite completa terminó con 34 pruebas aprobadas.
- **¿Qué haré?** Publicar la documentación definitiva, actualizar los resultados FIT, realizar la revisión del sprint y preparar los siguientes ejercicios.
- **¿Qué me lo impide?** Al iniciar una nueva sesión de terminal, Python no estaba disponible desde el comando `python`, debido a que el entorno virtual correcto no estaba activado. El problema se resolvió seleccionando y activando `.venv` dentro del repositorio.

**Evidencia:** [Pruebas completas de Sprint 1](../evidencias/pytest_sprint1.txt).

**Seguimiento de impedimentos y acción del SM:**

| Fecha | Impedimento | Qué hizo el SM |
|---|---|---|
| 11/11/2026 | La terminal no encontraba Python al ejecutar pytest porque no estaba activado el entorno virtual correcto. | Identificó la configuración incorrecta y activó el entorno `.venv` del repositorio, permitiendo continuar con las pruebas. |
| 11/11/2026 | Se detectó un cobro incorrecto al simular una modificación de la comparación de 24 horas. | Priorizó la corrección, verificó la prueba de regresión y confirmó que la suite completa volviera a pasar. |

**Limitación de la bitácora:**

La evidencia documentada no permite acreditar seis juntas realizadas en seis días distintos. Para mantener la trazabilidad, se registran las jornadas verificables y no se asignan fechas ficticias.

## C. Revisión del sprint

**🎩 PO revisa como si fuera mi cliente**

Se ejecutaron las pruebas automatizadas de R1 y R2 con el siguiente resultado:

**34 pruebas aprobadas y 0 fallidas.**

La revisión técnica se resume en la siguiente tabla. La aceptación definitiva de una historia requiere comprobar todos los criterios escritos en su Issue, además de las pruebas.

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| [H02 — Precio combinado](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) | Cálculo comprobado: corte $180 + barba $120 con 15 % de descuento = $255. | Aceptación técnica del cálculo; verificar demás criterios del Issue. | [Pruebas de R1](../evidencias/pytest_sprint1.txt) · [Commit VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/1a330c9) |
| [H03 — Descuento frecuente](https://github.com/RobertoDanRam/apartalo-barberia/issues/3) | Se verificó que con cuatro visitas no se aplica el descuento y desde cinco se descuentan $20 adicionales. | Aceptación técnica del cálculo; verificar demás criterios del Issue. | [Pruebas de R1](../evidencias/pytest_sprint1.txt) · [Commit VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/d52c04a) |
| [H05 — Cargo por cancelación](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | Se comprobaron los límites de 24 y 2 horas y las penalizaciones correspondientes. | Aceptación técnica del cálculo; verificar demás criterios del Issue. | [Pruebas de R2](../evidencias/pytest_sprint1.txt) · [Commit VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/8e9374c) |
| [H06 — Registrar inasistencias](https://github.com/RobertoDanRam/apartalo-barberia/issues/6) | Se comprobó el cargo del 100 % por inasistencia. No se ha demostrado un registro persistente de la inasistencia. | Pendiente de aceptación completa si la historia exige registrar el evento. | [Prueba de inasistencia](../evidencias/pytest_sprint1.txt) · [Commit VERDE](https://github.com/RobertoDanRam/apartalo-barberia/commit/8e9374c) |

**Evaluación del incremento:**

Las reglas de cálculo de R1 y R2 funcionan correctamente para los casos probados. Las pruebas también validan las principales condiciones límite y el rechazo de entradas inválidas.

La revisión distingue entre las funciones comprobadas y cualquier funcionalidad adicional descrita en los Issues, que deberá verificarse antes de declarar una historia totalmente terminada.

**Cambio que pediría mi cliente → historia nueva:**

Durante una revisión simulada desde la perspectiva de Don Rogelio, se propone que el cliente pueda recibir un comprobante al cancelar su cita, mostrando el cargo aplicado.

**Historia propuesta: Generar comprobante de cancelación**

**Como** Cliente de Barbería Filo, **quiero** recibir un comprobante con los datos de mi cancelación y el cargo aplicado, **para** tener constancia de la operación.

**Criterios de aceptación:**

1. El comprobante muestra el servicio, la fecha de la cita y el importe cobrado.
2. Si la cancelación se realiza con 24 horas o más de anticipación, el comprobante muestra un cargo de $0.

**Issue:** [H15 — Generar comprobante de cancelación (#19)](https://github.com/RobertoDanRam/apartalo-barberia/issues/19) 

Esta historia se incorporará al Product Backlog para evaluación en un sprint posterior.

## D. Retrospectiva

**🎩 SM facilita**

**¿Qué salió bien?**

Se logró configurar un tablero Kanban con límites WIP y políticas explícitas. El refinamiento permitió identificar las reglas de negocio y convertirlas en escenarios BDD verificables.

También se completaron tres ciclos ROJO → VERDE de TDD y una suite de 34 pruebas aprobadas. La prueba de regresión demostró que la condición de exactamente 24 horas queda protegida frente a cambios incorrectos.

**¿Qué hay que mejorar?**

Es necesario distribuir mejor el trabajo durante el periodo del sprint, en lugar de concentrar gran parte de las actividades y pruebas cerca de la fecha de entrega.

También conviene verificar antes de cada sesión que el entorno virtual esté activado y dedicar tiempo a contrastar los resultados técnicos con todos los criterios de aceptación de los Issues.

La falta de registros diarios suficientes dificulta documentar el seguimiento del sprint con la frecuencia solicitada.

**Acciones para el Sprint 2:**

1. **Establecer una rutina diaria de seguimiento:** al comenzar cada jornada, revisar el tablero Kanban, registrar las tres preguntas de la junta diaria y comprobar los impedimentos. Mantener el límite WIP de una historia activa en Desarrollo.
2. **Integrar pruebas desde el inicio de cada historia:** activar el entorno virtual, escribir primero las pruebas, ejecutar los ciclos TDD y comprobar los criterios de aceptación antes de marcar una historia como terminada.

Estas acciones se retomarán y evaluarán durante la Evidencia 2.