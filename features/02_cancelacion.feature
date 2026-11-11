
# language: es

Característica: Calcular cargos por cancelación
  Como Administrador de Barbería Filo
  quiero determinar el cargo correspondiente a una cancelación
  para reducir las pérdidas ocasionadas por inasistencias.

  Esquema del escenario: Cancelar una reserva con anticipación
    Dado que existe una reserva con total de <total> pesos
    Y faltan <horas> horas para la cita
    Cuando el cliente cancela su reservación
    Entonces el cargo debe ser de <cargo> pesos

    Ejemplos:
      | total | horas | cargo |
      | 200   | 48    | 0     |
      | 200   | 24    | 0     |
      | 200   | 23    | 100   |
      | 200   | 2     | 100   |
      | 200   | 1     | 200   |
      | 200   | 0     | 200   |

  Escenario: Registrar una inasistencia
    Dado que existe una reserva con total de 200 pesos
    Y el cliente no se presentó a la cita
    Cuando se registra la inasistencia
    Entonces el cargo debe ser de 200 pesos
