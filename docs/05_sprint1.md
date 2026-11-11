# 5. Sprint 1 (27 oct – 9 nov 2026)

**Ejercicio 5 · Temas 4 y 11**

**Proyecto:** Apártalo — Barbería Filo

## A. Planeación del sprint

**🎩 SM facilita · 🎩 PO presenta · 🎩 Desarrollador se compromete**

**Objetivo del sprint:**

Implementar y validar mediante Python y pytest las reglas R1 y R2 de Barbería Filo, incluyendo el cálculo de precios, descuentos y cargos por cancelaciones e inasistencias.

**Capacidad en horas (Figura 2 del Tema 11):**

*Ejemplo de estimación inicial. Sustituir las cantidades por las horas realmente disponibles durante el periodo.*

| Concepto | Horas |
|---|---:|
| Horas disponibles en las dos semanas | 56 |
| − Otras actividades (clases, trabajo, tareas) | 24 |
| = Disponibilidad | 32 |
| ÷ 2 = **Capacidad** | **16** |

**Operación:** (56 − 24) / 2 = **16 horas**.

**Compromiso (historias del Sprint 1):**

| Historia | Puntos | Horas estimadas |
|---|---:|---:|
| [H02 — Calcular precio combinado](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) | 3 | 3 |
| [H03 — Aplicar descuento frecuente](https://github.com/RobertoDanRam/apartalo-barberia/issues/3) | 3 | 3 |
| [H05 — Calcular cargo de cancelación](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | 5 | 5 |
| [H06 — Registrar inasistencias](https://github.com/RobertoDanRam/apartalo-barberia/issues/6) | 3 | 3 |
| **Total** | **14** | **14** |

Las historias comprometidas cubren la regla R1 (total del servicio) y la regla R2 (cancelaciones e inasistencias).

En este ejemplo, las 14 horas estimadas no superan las 16 horas de capacidad y dejan un margen de 2 horas.

La carga máxima por historia es de 8 puntos, según el refinamiento del Ejercicio 4. Todas las historias seleccionadas cumplen con ese límite.

**Definición de Terminado (DoD):**

1. La funcionalidad se encuentra implementada correctamente en `src/apartalo/reglas.py`.
2. Las pruebas unitarias y de aceptación correspondientes pasan con pytest.
3. El código está integrado en la rama `main` y los cambios están registrados mediante commits de Git.
4. Todos los criterios de aceptación de la historia se cumplen.
5. No existen defectos críticos pendientes y se conserva evidencia de los resultados obtenidos.

**DoD vs. criterios de aceptación (con un ejemplo de mi backlog):**

Los criterios de aceptación establecen las condiciones específicas que debe cumplir una historia de usuario. En cambio, la Definición de Terminado establece las condiciones generales de calidad que debe cumplir cualquier historia antes de considerarse entregada.

Por ejemplo, H02 exige que al reservar corte ($180) y barba ($120) juntos se aplique un descuento del 15 %, dando un total de $255.

Cumplir ese cálculo satisface un criterio de aceptación, pero para cumplir la DoD también es necesario implementar el código, ejecutar las pruebas correspondientes, registrar los cambios en GitHub y verificar que no queden defectos críticos.

## B. Junta diaria — bitácora

**🎩 Desarrollador responde · 🎩 SM anota impedimentos**

Las entradas siguientes deben completarse con actividades y fechas reales. Cada una corresponde a una jornada diferente.

### [Fecha real 1]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

### [Fecha real 2]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

### [Fecha real 3]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

### [Fecha real 4]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

### [Fecha real 5]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

### [Fecha real 6]

- **¿Qué hice?** [Registrar actividades realizadas.]
- **¿Qué haré?** [Registrar el siguiente paso.]
- **¿Qué me lo impide?** [Indicar un impedimento real o ninguno.]

**Impedimentos y qué hizo el SM:**

| Fecha | Impedimento | Qué hizo el SM |
|---|---|---|
| [Fecha real] | [Describir el problema observado.] | [Explicar la acción concreta utilizada para resolverlo.] |

## C. Revisión del sprint

**🎩 PO revisa como si fuera mi cliente**

La revisión se completará después de implementar y ejecutar las pruebas de R1 y R2.

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| [H02](https://github.com/RobertoDanRam/apartalo-barberia/issues/2) | Pendiente de verificar | Pendiente | [Agregar enlace a pruebas o commit] |
| [H03](https://github.com/RobertoDanRam/apartalo-barberia/issues/3) | Pendiente de verificar | Pendiente | [Agregar enlace a pruebas o commit] |
| [H05](https://github.com/RobertoDanRam/apartalo-barberia/issues/5) | Pendiente de verificar | Pendiente | [Agregar enlace a pruebas o commit] |
| [H06](https://github.com/RobertoDanRam/apartalo-barberia/issues/6) | Pendiente de verificar | Pendiente | [Agregar enlace a pruebas o commit] |

**Cambio que pediría mi cliente → historia nueva:**

Propuesta para validar durante la revisión: generar un comprobante de cancelación que informe al cliente el importe de la penalización aplicada.

**Historia propuesta:** H15 — Generar comprobante de cancelación.

Como Cliente, quiero recibir un comprobante con la información de mi cancelación y el cargo aplicado, para tener constancia de la operación.

**Issue:** [Agregar el enlace real después de crear la historia en GitHub].

## D. Retrospectiva

**🎩 SM facilita**

**¿Qué salió bien?**

[Registrar los resultados positivos que realmente observé durante el sprint, por ejemplo, el refinamiento del backlog, la claridad de los escenarios o la ejecución de las pruebas.]

**¿Qué hay que mejorar?**

[Describir dificultades reales del proceso sin atribuir culpas, por ejemplo, las estimaciones, la organización del tiempo o la gestión de impedimentos.]

**Acciones para el Sprint 2:**

1. Reservar un bloque específico de tiempo para escribir y ejecutar las pruebas antes de implementar cada funcionalidad, conservando evidencia de los ciclos TDD.
2. Revisar al comienzo de cada jornada las historias activas y los límites WIP del tablero, priorizando terminar una historia antes de comenzar otra.

Las acciones se revisarán nuevamente durante la planeación de la Evidencia 2.