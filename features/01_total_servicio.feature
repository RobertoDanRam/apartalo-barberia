
# language: es

Característica: Calcular el total del servicio
  Como Cliente de Barbería Filo
  quiero conocer el costo de los servicios reservados
  para saber cuánto pagaré después de los descuentos.

  Esquema del escenario: Calcular el total según los servicios y las visitas
    Dado que el cliente reserva corte "<corte>" y barba "<barba>"
    Y tiene <visitas> visitas en el mes
    Cuando se calcula el total del servicio
    Entonces el importe final debe ser <total> pesos

    Ejemplos:
      | corte | barba | visitas | total |
      | si    | no    | 0       | 180   |
      | no    | si    | 0       | 120   |
      | si    | si    | 4       | 255   |
      | si    | si    | 5       | 235   |
      | si    | no    | 5       | 160   |
      | no    | si    | 5       | 100   |
