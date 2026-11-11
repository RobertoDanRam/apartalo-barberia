# 1. Visión y problema correcto

**Ejercicio 1 · Temas 1, 2 y 5 · 🎩 Product Owner (PO)**

## 1.2 ¿Por qué no cascada?

| Causa de falla de cascada | Cómo se vería en mi proyecto |
|---|---|
| Los proyectos reales rara vez siguen modelos lineales o secuenciales. | En Barbería Filo, Don Rogelio podría solicitar cambios en las políticas de reservación, descuentos o cancelaciones después de revisar los primeros resultados. En cascada, estos cambios serían difíciles de incorporar porque las etapas se desarrollan de forma secuencial, lo que podría generar confusión y retrabajo. |
| A menudo es difícil que el cliente exponga explícitamente todos los requisitos. | Don Rogelio sabe que pierde dinero cuando los clientes no se presentan, pero todavía no tiene claro si quiere cobrar anticipos. Esto demuestra que existen necesidades y decisiones pendientes. Si definiéramos todos los requisitos desde el principio, podríamos desarrollar funcionalidades que no resuelvan correctamente su problema. |

**¿Usaría prototipos? ¿En qué momento y para qué?**

Sí, utilizaría prototipos de baja fidelidad durante el refinamiento del backlog, antes de desarrollar la interfaz. Elaboraría un boceto de la pantalla de reservaciones para mostrar cómo los clientes podrían seleccionar un servicio, consultar su precio y confirmar una cita.

El objetivo sería recibir retroalimentación de Don Rogelio, aclarar requisitos y detectar posibles problemas de usabilidad antes de programar. El prototipo serviría para validar las ideas, no como producto final.

## 1.3 El manifiesto en mi proyecto

| Valor o principio | Decisión concreta en mi proyecto |
|---|---|
| **Valor: Software funcionando sobre documentación extensiva.** | Durante el Sprint 1 priorizaré implementar y probar las reglas R1 (cálculo del servicio) y R2 (cancelaciones) con Python y pytest, en lugar de elaborar únicamente documentos sin funcionalidades comprobables. |
| **Valor: Colaboración con el cliente sobre negociación contractual.** | Tomaré las necesidades de Don Rogelio como referencia para organizar el backlog. Antes de implementar el cobro de anticipos, buscaré aclarar sus dudas para evitar una funcionalidad que pueda perjudicar las reservaciones. |
| **Principio: Entregar software funcionando frecuentemente.** | Organizaré el desarrollo en sprints, comenzando por las funciones de cálculo de precios y cancelaciones. Las funcionalidades adicionales, como la gestión completa de la agenda, se desarrollarán en futuras entregas. |
| **Principio: Aceptar cambios en los requisitos, incluso en etapas avanzadas.** | Si Don Rogelio decide modificar las políticas de reservación o implementar anticipos después de revisar los resultados, registraré los cambios como historias de usuario y evaluaré su prioridad para un sprint posterior. |

## 1.4 Frameworks

| Framework | Lo que tomo de él |
|---|---|
| **Scrum** | Utilizaré sprints para organizar las entregas, un product backlog para administrar y priorizar las historias de usuario, y actividades de planeación, revisión y retrospectiva. Como soy un equipo de una sola persona, asumiré los roles de Product Owner, Scrum Master y desarrollador. |
| **Kanban** | Utilizaré un tablero de GitHub Projects para visualizar el avance de las historias mediante las columnas Historias, Aceptación, Desarrollo, Desarrollo listo, Pruebas, Pruebas listo y Liberación. Estableceré límites WIP para evitar realizar demasiadas tareas simultáneamente y mantener un flujo de trabajo organizado. |
| **XP (Extreme Programming)** | Aplicaré TDD mediante ciclos rojo-verde-refactor, escribiendo pruebas antes de implementar el código. Utilizaré Python y pytest para comprobar las reglas de negocio, además de realizar cambios pequeños y frecuentes mediante commits en Git. |

**La combinación de Scrum y Kanban se llama:** Scrumban.

## 1.5 Requisito o solución

| # | Lo que dijo mi cliente | ¿Requisito o solución? | Si es solución: el requisito que hay detrás |
|---|---|---|---|
| 1 | "Me dejan plantado mucho los sábados y pierdo dinero." | **Requisito (necesidad del negocio).** | Se necesita reducir las pérdidas económicas ocasionadas por clientes que no se presentan a sus citas, mediante una política clara de cancelaciones. |
| 2 | "Quiero un botón verde grande que diga RESERVAR, como el de WhatsApp." | **Solución.** | El cliente necesita identificar fácilmente cómo reservar una cita y completar el proceso de manera sencilla. El color y tamaño del botón son decisiones de diseño que pueden validarse con un prototipo. |
| 3 | "Los clientes de siempre se merecen algo." | **Requisito (necesidad del negocio).** | Se necesita reconocer la fidelidad de los clientes frecuentes mediante algún beneficio. La regla R1 concreta esta necesidad con un descuento de $20 para quienes tengan cinco visitas o más durante el mes. |
| 4 | "Que me llegue la agenda del día en un Excel." | **Solución.** | El dueño necesita consultar y organizar las citas diarias para conocer los horarios ocupados y disponibles. Exportar la agenda a Excel es una alternativa, pero también podrían utilizarse otros formatos de consulta. |
| 5 | "No sé si cobrar por adelantado; me da miedo que la gente ya no reserve." | **Solución propuesta, todavía no decidida.** | Se necesita encontrar una forma de reducir las pérdidas por inasistencias sin desmotivar a los clientes a reservar. Antes de implementar anticipos, es necesario evaluar si realmente benefician al negocio. |

## 1.6 Incertidumbre

- **Incertidumbre del qué: Alta.** Don Rogelio tiene claro que desea reducir las pérdidas ocasionadas por las inasistencias, pero todavía no sabe si cobrar anticipos es la mejor alternativa. También existen decisiones pendientes sobre cómo facilitar las reservaciones y recompensar a los clientes frecuentes.

- **Incertidumbre del cómo: Baja.** Para el alcance técnico del Sprint 1 se utilizarán funciones sencillas de Python para calcular precios, descuentos y cargos por cancelación. Las herramientas y técnicas de implementación están definidas, utilizando pytest y escenarios BDD para comprobar los resultados.

- **Zona del diagrama:** Alta incertidumbre del qué y baja incertidumbre del cómo. El principal reto del proyecto es comprender correctamente las necesidades del negocio y decidir cuáles funcionalidades aportan mayor valor. La implementación técnica inicial es relativamente sencilla y utiliza herramientas conocidas.

- **Qué haré en este sprint para bajar la incertidumbre del qué:** Como Product Owner, prepararé diferentes escenarios de cancelación y posibles anticipos para revisarlos con Don Rogelio. También elaboraré un prototipo sencillo de la pantalla de reservaciones y definiré criterios de aceptación para las reglas R1 y R2. Esto permitirá aclarar necesidades, identificar suposiciones y registrar las decisiones pendientes en el backlog para futuros sprints.