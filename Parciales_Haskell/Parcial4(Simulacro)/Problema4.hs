personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos listaTuplas = maxAux (convertidor (personas listaTuplas) listaTuplas)

{-
personaConMasAmigos listaTuplas = contadorAmigos -----/// (amigosDe x)
-}

contadorAmigos :: [String] -> Integer
contadorAmigos [] = 0
contadorAmigos (x : xs) = 1 + contadorAmigos xs

{-
contadorAmigos ["a","b","c","d","e","f","g","h","I"] ✔

personaConMasAmigos [("a","b"),("c","d"),("a","d"),("v","m"),("x","k"),("l","m"),("o","q"),("z","a")]
personaConMasAmigos [("d","f"),("c","d"),("f","d"),("f","m"),("d","k"),("l","f"),("o","f"),("f","a")]

 [("Alice", "Bob"), ("Alice", "Carol"), ("Bob", "David"), ("Carol", "Eve"), ("Eve", "Frank")]

-}

maxAux :: [(String, Integer)] -> String
maxAux [(a, b)] = a
maxAux ((x, y) : (n, m) : ys)
  | y >= m = maxAux ((x, y) : ys)
  | otherwise = maxAux ((n, m) : ys)

----------------------------------------------------------------------------------------------
convertidor :: [String] -> [(String, String)] -> [(String, Integer)]
convertidor [] _ = []
convertidor (x : xs) lista = (x, (contadorAmigos (amigosDe x lista))) : convertidor xs lista

----------------------------------------------------------------------------------------------
amigosDe :: String -> [(String, String)] -> [String]
amigosDe x [] = []
amigosDe x ((y, z) : ys)
  | x == y = z : amigosDe x ys
  | x == z = y : amigosDe x ys
  | otherwise = amigosDe x ys

{-
personaConMasAmigos listaTuplas  = maxAux (convertidor (personas listaTuplas) listaTuplas)

   convertidor  :: [String] -> [(String, String)] -> [(String, Integer)]
   convertidor      []            _   = []
   convertidor     (x:xs)       lista =  (x ,(contadorAmigos (amigosDe x lista))) : convertidor xs lista

        [(String, Integer)] -> String
   max (a,b) = a
   max ((x,y),(n,m):ys) | y >= m = max ((x,y):ys)
                        | otherwise = max ((n,m):ys)
-}

------------------------------------------------------------------------------------

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