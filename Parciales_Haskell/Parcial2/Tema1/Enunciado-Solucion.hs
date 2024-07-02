module Tema1Solucion where

{--
1) Goles de no goleadores [1 punto]
problema golesDeNoGoleadores (goleadoresPorEquipo: seq⟨String x String⟩,goles:seq< Z >, totalGolesTorneo: Z) : Z {
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {La suma de todos los elementos de goles es menor o igual a totalGolesTorneo}
  asegura:  {res es la cantidad de goles convertidos en el torneo por jugadores que no
            son los goleadores de sus equipos}
}
--}
golesDeNoGoleadores :: [(String, String)] -> [Int] -> Int  -> Int
golesDeNoGoleadores _ goles totalGolesTorneo = totalGolesTorneo - contarGoles goles

contarGoles  :: [Int] -> Int
contarGoles [] = 0
contarGoles (x:xs) = x + contarGoles xs

{--
2) Equipos Válidos  [3 puntos]
problema equiposValidos (equipos: seq⟨String x String⟩) : Bool {
  requiere: {True}
  asegura:  {(res = true) <=> equipos no contiene nombres de clubes repetidos,
            ni goleadores repetidos, ni jugadores con nombre de club}
}
--}
equiposValidos  :: [(String,String)] -> Bool
equiposValidos xs = not (hayRepetidos (aplanar xs))

aplanar  :: [(String,String)] -> [String]
aplanar [] = []
aplanar ((a,b):xs) = a:b:aplanar xs

hayRepetidos :: (Eq t ) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

pertenece :: (Eq t ) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x  || pertenece e xs

{--
3) Porcentaje de Goles  [3 puntos]
problema porcentajeDeGoles (goleador: String, goleadoresPorEquipo: seq⟨String x String⟩,goles:seq⟨Z⟩) : R {
  requiere: {La segunda componente de algún elemento de equipos es goleador}
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {Hay al menos un elemento de goles mayores estricto a 0}
  asegura:  {res es el porcentaje de goles que marcó goleador sobre el total de goles
            convertidos por goleadores}
}
--}
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles goleador goleadoresPorEquipo goles =
            division (golesDe goleador goleadoresPorEquipo goles)
              (contarGoles goles)

golesDe  :: String  -> [(String, String)] -> [Int] -> Int
golesDe jugador ((e,j):js) (g:gs) | jugador == j = g
                                  | otherwise = golesDe jugador js gs

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

{--
4) Botín de Oro  [3 puntos]
problema botinDeOro (goleadoresPorEquipo: seq⟨String x String⟩, goles:seq⟨Z⟩) : String {
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {|goles| > 0}
  asegura:  {res es alguno de los goleadores de goleadoresPorEquipo que más tantos
            convirtió de acuerdo a goles}
}
--}
botinDeOro :: [(String, String)] -> [Int] -> String
botinDeOro [(_,j)] [_] = j
botinDeOro (x:x2:xs) (g:g2:gs)
  | g > g2 = botinDeOro (x:xs) (g:gs)
  | otherwise = botinDeOro (x2:xs) (g2:gs)
