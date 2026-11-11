# 2. El product backlog

**Ejercicio 2 · Tema 6 · 🎩 Product Owner (PO)**

## 2.1 Roles

| Rol | Quién es | Qué desea |
|---|---|---|
| Cliente | Persona que acude a Barbería Filo para recibir un servicio de corte de cabello o barba. | Consultar los servicios y sus precios, reservar citas, conocer sus descuentos y cancelar con reglas claras. |
| Administrador | Don Rogelio, dueño de Barbería Filo, responsable de la administración del negocio. | Organizar las reservaciones, evitar citas duplicadas, controlar la disponibilidad y reducir las pérdidas por inasistencias. |
| Barbero | Trabajador de la barbería encargado de atender los servicios reservados. | Consultar las citas asignadas y conocer los servicios que debe realizar durante su jornada. |


## 2.4 Plantilla invertida: historias que me faltaban

La plantilla invertida comienza por el beneficio que necesita obtener el usuario:

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
|---|---|---|
| Evitar sorpresas relacionadas con los cargos por cancelación. | Para poder conocer las condiciones antes de reservar, como Cliente, quiero consultar la política de cancelaciones de la barbería. | [H12 — Issue #12](https://github.com/RobertoDanRam/apartalo-barberia/issues/12) |
| Tener la seguridad de que una reservación quedó registrada correctamente. | Para poder confirmar que mi cita se guardó, como Cliente, quiero recibir una confirmación con la fecha, hora y servicio reservado. | [H13 — Issue #13](https://github.com/RobertoDanRam/apartalo-barberia/issues/13) |

**¿Cómo me ayudó ordenar por beneficio?**

Comenzar por los beneficios me permitió identificar necesidades que no había considerado al pensar únicamente en las funciones principales del sistema. Descubrí que los clientes necesitan conocer las reglas de cancelación antes de reservar y comprobar que sus citas fueron registradas. Estas dos historias complementan las funciones de reservación y contribuyen a reducir las confusiones y las inasistencias.


## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
|---|---|
| Reservación o cita | Registro de un cliente para recibir un servicio de barbería en una fecha y hora determinadas. |
| Servicio | Atención que ofrece Barbería Filo: corte de cabello ($180), arreglo de barba ($120) o ambos servicios combinados. |
| Cliente frecuente | Cliente que ha realizado cinco visitas o más durante el mes y tiene derecho a un descuento adicional de $20. |
| Cancelación | Anulación de una cita previamente registrada. Puede generar un cargo dependiendo de las horas de anticipación. |
| Inasistencia | Situación en la que un cliente no se presenta a su cita sin haberla cancelado oportunamente. Se cobra el 100 % del servicio reservado. |

## 2.6 El iceberg

- **En la punta:** Colocaré las historias relacionadas con las reglas R1 y R2, como calcular precios, aplicar descuentos y determinar los cargos por cancelación. Son funcionalidades claras, importantes para Don Rogelio y necesarias para el Sprint 1.

- **En el fondo:** Dejaré funcionalidades posteriores como exportar la agenda, consultar citas asignadas y las épicas relacionadas con la gestión completa de reservaciones y la evolución del programa de fidelidad.

- **Por qué:** La punta del iceberg contiene historias prioritarias, pequeñas y suficientemente claras para desarrollarse y probarse. En el fondo permanecen historias menos urgentes o funcionalidades grandes que todavía necesitan análisis, negociación o división antes de desarrollarse.