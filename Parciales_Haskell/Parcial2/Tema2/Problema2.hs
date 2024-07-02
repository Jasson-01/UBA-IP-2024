formulasValidas :: [(String, String)] -> Bool -- Es True si todas las funciones son True!
formulasValidas [] = True
formulasValidas xs = presidentesNoRepetidos xs && vicepresidentesNoRepetidos xs && ambosNoRepetidos xs

--------------------------------------------------------------------------

presidentesNoRepetidos :: [(String, String)] -> Bool -- Quiero que no se repita ningun presidente
presidentesNoRepetidos ((x, _) : ys) = not (pertenece x (listaPresidentes ys))

listaPresidentes :: [(String, String)] -> [String]
listaPresidentes [] = []
listaPresidentes ((x, _) : ys) = x : listaPresidentes ys

--------------------------------------------------------------------------

pertenece :: String -> [String] -> Bool -- Quiero ver si el elmento "x" pertenece a la lista
pertenece x [] = False
pertenece x (y : ys)
  | x /= y = pertenece x ys
  | otherwise = True

--------------------------------------------------------------------------

vicepresidentesNoRepetidos :: [(String, String)] -> Bool
vicepresidentesNoRepetidos ((_, n) : ys) = not (pertenece n (listaVicepresidentes ys))

listaVicepresidentes :: [(String, String)] -> [String]
listaVicepresidentes [] = []
listaVicepresidentes ((_, y) : ys) = y : listaVicepresidentes ys

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

--------------------------------------------------------------------------

{-
tests:

presidentesNoRepetidos [("a","b"),("c","d"),("e","f")]

listaPresidentes [("a","b"),("c","d"),("e","f")]

listaVicepresidentes [("a","b"),("c","d"),("e","f")]

ambosNoRepetidos [("a","b"),("c","d"),("e","f"),("b","a"),("z","k")]  -> False

pertenece a ["a"]

formulasValidas [("a","b"),("c","d"),("e","f"),("b","a"),("z","k")] -> False -- se repite la inversa
formulasValidas [("a","b"),("c","d"),("e","f"),("a","b"),("z","k")] -> False -- se repite              ✔
formulasValidas [("a","b"),("c","d"),("e","f"),("f","e"),("z","k")] -> False
formulasValidas [("a","b"),("c","d"),("e","f"),("m","n"),("z","k")] -> True
formulasValidas [("a","b"),("c","d"),("e","f"),("b","a"),("c","d")] -> False
formulasValidas [("a","b"),("c","d"),("e","f"),("c","d"),("z","k")] -> False
formulasValidas [] -> False

-}

f4 :: Float -> Float
f4 n
  | n <= 9 = 7
  | n >= 3 = 5

funcionRara :: Float → Float → Bool → Bool
funcionRara x y z = (x >= y) || z