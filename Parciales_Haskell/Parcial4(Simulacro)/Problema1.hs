relacionesValidas :: [(String, String)] -> Bool -- Es True si todas las funciones son True!
relacionesValidas [] = True
relacionesValidas xs = ambosNoRepetidos xs

-- relacionesValidas xs = primerNoRepetidos xs && segundoNoRepetidos xs && ambosNoRepetidos xs

--------------------------------------------------------------------------
{-
primerNoRepetidos :: [(String, String)] -> Bool -- Quiero que no se repita ningun presidente
primerNoRepetidos ((x, _) : ys) = not (pertenece x (listaNombres ys))

listaNombres :: [(String, String)] -> [String]
listaNombres [] = []
listaNombres ((x, _) : ys) = x : listaNombres ys
-}
--------------------------------------------------------------------------

pertenece :: String -> [String] -> Bool -- Quiero ver si el elmento "x" pertenece a la lista
pertenece x [] = False
pertenece x (y : ys)
  | x /= y = pertenece x ys
  | otherwise = True

--------------------------------------------------------------------------
{-
segundoNoRepetidos :: [(String, String)] -> Bool
segundoNoRepetidos ((_, n) : ys) = not (pertenece n (listaVicepresidentes ys))

listaVicepresidentes :: [(String, String)] -> [String]
listaVicepresidentes [] = []
listaVicepresidentes ((_, y) : ys) = y : listaVicepresidentes ys
-}
--------------------------------------------------------------------------
ambosNoRepetidos :: [(String, String)] -> Bool -- Quiero saber si alguna Dupla se repite en la lista de tuplas.
ambosNoRepetidos [] = True
ambosNoRepetidos ((x, y) : ys)
  | x /= y && (perteneceDeADos (x, y) ys == False) && (perteneceDeADos (y, x) ys == False) = ambosNoRepetidos ys
  | otherwise = False

perteneceDeADos :: (String, String) -> [(String, String)] -> Bool -- Quiero saber si la tupla pertenece a la lista de tuplas, no quiero que se repita, si se repite es True sino es False.
perteneceDeADos (_, _) [] = False
perteneceDeADos (n, m) ((x, y) : ys)
  | (n, m) /= (x, y) = perteneceDeADos (n, m) ys
  | otherwise = True
