
-- Ejercicio 8 - Metricas de Barberia Filo
-- Fuente: fotografia estatica del tablero de GitHub Projects

-- a) Puntos comprometidos en el Sprint 1
SELECT
    COALESCE(SUM(puntos), 0) AS puntos_comprometidos
FROM tablero
WHERE sprint = 'Sprint 1'
  AND titulo LIKE 'H%';


-- b) Puntos entregados: historias del Sprint 1 en Liberacion
SELECT
    COALESCE(SUM(puntos), 0) AS puntos_entregados
FROM tablero
WHERE sprint = 'Sprint 1'
  AND estado = 'Liberación'
  AND titulo LIKE 'H%';


-- c) Porcentaje de cumplimiento del Sprint 1
SELECT
    ROUND(
        100.0 *
        SUM(CASE
            WHEN estado = 'Liberación' THEN COALESCE(puntos, 0)
            ELSE 0
        END)
        / NULLIF(SUM(COALESCE(puntos, 0)), 0),
        2
    ) AS porcentaje_cumplimiento
FROM tablero
WHERE sprint = 'Sprint 1'
  AND titulo LIKE 'H%';


-- d) Tiempo de ciclo promedio de historias entregadas
SELECT
    ROUND(
        AVG(julianday(terminado) - julianday(inicio)),
        2
    ) AS ciclo_promedio_dias
FROM tablero
WHERE sprint = 'Sprint 1'
  AND estado = 'Liberación'
  AND titulo LIKE 'H%'
  AND inicio IS NOT NULL
  AND terminado IS NOT NULL;


-- e) Subconjunto de historias con prioridad Must
SELECT
    titulo AS historia,
    puntos,
    estado
FROM tablero
WHERE prioridad = 'Must'
  AND titulo LIKE 'H%'
ORDER BY titulo;
