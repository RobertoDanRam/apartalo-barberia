# 3. El tablero kanban

**Ejercicio 3 · Tema 3 · 🎩 Scrum Master (SM)**

## 3.2 Límites WIP

| Columna | Límite | Por qué ese número |
|---|---|---|
| Aceptación | 1 | Como soy el único integrante del equipo, revisaré una historia a la vez para asegurar que esté clara y que sus criterios de aceptación sean comprobables. |
| Desarrollo | 1 | Trabajaré en una historia a la vez para evitar cambios de contexto y concentrarme en la implementación y las pruebas unitarias mediante TDD. |
| Pruebas | 1 | Verificaré una historia a la vez con pytest para identificar errores y evitar acumular trabajo sin validar. |

Los límites WIP permiten controlar el trabajo activo. Las columnas Desarrollo listo y Pruebas listo funcionan como búferes, por lo que una tarjeta puede esperar allí hasta que la siguiente etapa tenga capacidad.

## 3.3 Políticas explícitas

| Para pasar a… | La tarjeta debe cumplir… |
|---|---|
| Aceptación | Debe estar registrada en el Product Backlog, tener prioridad definida y contar con una historia de usuario que exprese el rol, el deseo y el beneficio, además de al menos dos criterios de aceptación. |
| Desarrollo | Debe contar con criterios de aceptación revisados, cumplir con INVEST, tener puntos estimados y estar seleccionada para el sprint. Debe existir capacidad disponible en Desarrollo. |
| Desarrollo listo | La funcionalidad debe estar implementada en Python, sus pruebas unitarias deben pasar y el código debe estar registrado mediante commits e integrado en `main`. |
| Pruebas | La implementación debe encontrarse en Desarrollo listo, contar con sus pruebas unitarias aprobadas y tener escenarios de aceptación definidos. Solo avanzará si existe capacidad disponible en Pruebas. |
| Pruebas listo | Las pruebas de aceptación deben pasar correctamente con pytest y no deben existir errores críticos pendientes. Los resultados deben quedar registrados como evidencia. |
| Liberación | La historia debe cumplir sus criterios de aceptación y la Definición de Terminado (DoD). Como Product Owner, revisaré y aceptaré el resultado antes de considerarlo entregado. |

Si una prueba falla, la historia regresará a Desarrollo para corregir el defecto. Una historia no se considerará liberada si todavía tiene criterios de aceptación sin cumplir.

## 3.4 Las seis prácticas de kanban en mi tablero

| Práctica | Cómo la aplico (o por qué todavía no aplica) |
|---|---|
| 1. Visualizar el trabajo | Utilizaré el tablero Board de GitHub Projects, dividido en siete columnas, para identificar qué historias están pendientes, en desarrollo, en pruebas o liberadas. |
| 2. Limitar el WIP | Estableceré un límite de una historia en Aceptación, Desarrollo y Pruebas, debido a que trabajo individualmente y necesito evitar realizar demasiadas tareas simultáneamente. |
| 3. Administrar el flujo | Moveré cada historia solamente cuando cumpla las políticas de su siguiente etapa. Revisaré los búferes para detectar trabajo acumulado y daré prioridad a terminar lo iniciado. |
| 4. Hacer explícitas las políticas | Documentaré las condiciones para que una tarjeta avance entre columnas, considerando criterios de aceptación, estimaciones, pruebas automatizadas y la Definición de Terminado. |
| 5. Implementar ciclos de retroalimentación | Utilizaré los resultados de pytest, la revisión del sprint y la retrospectiva para identificar errores y oportunidades de mejora. Como trabajo individualmente, documentaré las observaciones desde los tres sombreros Scrum. |
| 6. Mejora colaborativa y evolución experimental | Analizaré los resultados del Sprint 1 y propondré acciones de mejora para el Sprint 2. Aunque no existen otros desarrolladores en mi equipo, aplicaré mejoras incrementales y consideraré la retroalimentación del cliente. |

## 3.5 Movimiento de tarjetas durante el sprint

Las historias comenzarán en la columna Historias y avanzarán conforme cumplan las políticas establecidas para cada etapa.

Durante el Sprint 1 daré prioridad a las historias relacionadas con R1 (cálculo del total del servicio) y R2 (cancelaciones), según el compromiso y la capacidad definidos durante la planeación.

Registraré las fechas reales de inicio y finalización de las historias. No moveré ninguna historia a Liberación sin haber comprobado sus criterios de aceptación y ejecutado las pruebas correspondientes.

Los estados finales del tablero y las fechas registradas se utilizarán posteriormente para calcular las métricas del Ejercicio 8.