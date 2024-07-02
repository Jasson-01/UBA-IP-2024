personas :: [(String, String)] -> [String]
personas n = quitarRepetidos (listaAux n)

quitarRepetidos :: [String] -> [String]
quitarRepetidos [] = []
quitarRepetidos (x : xs)
  | pertenece x xs = quitarRepetidos xs
  | otherwise = x : quitarRepetidos xs

listaAux :: [(String, String)] -> [String]
listaAux [] = []
listaAux ((x, y) : xs) = x : y : listaAux xs

pertenece :: String -> [String] -> Bool
pertenece x [] = False
pertenece x (y : ys)
  | x /= y = pertenece x ys
  | otherwise = True

{-
 prueba 1:

Dado: [(Juan, Perez), (Maria, Lopez), (Juan, Perez)]
 es ["Juan", "Perez", "Maria", "Lopez"].

Caso de prueba 2:

Dado: [(Ana, Garcia), (Pedro, Martinez), (Maria, Rodriguez)]
 es ["Ana", "Garcia", "Pedro", "Martinez", "Maria", "Rodriguez"].

Caso de prueba 3:

Dado: [(Juan, Perez), (Juan, Perez), (Juan, Perez)]
o es ["Juan", "Perez"].

-}