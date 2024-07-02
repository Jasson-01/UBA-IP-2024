module JasonHaskell where

--    1er Parcial HASKELL  ("Vamos Campeon!!!") ---

-- Problema 1
atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes [] [] n = n
atajaronSuplentes _ (x : xs) n = n - sumaDeLaLista (x : xs)

sumaDeLaLista :: [Int] -> Int
sumaDeLaLista [] = 0
sumaDeLaLista (x : xs) = x + sumaDeLaLista xs

{-

      " equipos sin atajadas suplente sin goles" ~: atajaronSuplentes [] [] 0 ~?= 0,
      " equipos sin atajadas suplente con 1 goles" ~: atajaronSuplentes [] [] 1 ~?= 1,
      " equipos sin atajadas suplente con n goles" ~: atajaronSuplentes [] [] 3 ~?= 3,

-}

-- atajaronSuplentes [("A","a"),("B","b"),("C","c")] [3,4,5] 20 -> result = 8
-- atajaronSuplentes [("A","a"),("B","b"),("C","c"),("D","d"),("E","e"),("F","f")] [3,4,5,6,7,8] 40 -> result = 7

------------------------------------------------------------------------------------------------------
-- Problema 2

equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((x, y) : zs)
  | ((repetido (sacoNombresClubes zs) x) == True) || ((repetido (sacoNombresArqueros zs) y) == True) || ((nombreClubDistinto ((x, y) : zs)) == False) || (tieneDuplicados2 ((x, y) : zs)) = False
  | otherwise = equiposValidos zs

sacoNombresClubes :: [(String, String)] -> [String] -- Saca los nombres de los clubes y los junta en una lista
sacoNombresClubes [] = []
sacoNombresClubes ((x, _) : ys) = x : sacoNombresClubes ys -- Funciona!!

sacoNombresArqueros :: [(String, String)] -> [String] -- Saca los nombres de los Arqueros y los junta en una lista
sacoNombresArqueros [] = []
sacoNombresArqueros ((_, y) : ys) = y : sacoNombresArqueros ys -- Funciona!!

repetido :: [String] -> String -> Bool -- Me dice si un nombre pertenece a la lista
repetido [] n = False
repetido (x : xs) n
  | n == x = True
  | otherwise = repetido xs n

nombreClubDistinto :: [(String, String)] -> Bool
nombreClubDistinto [] = True
nombreClubDistinto ((x, y) : xs)
  | x == y = False
  | otherwise = nombreClubDistinto xs

----
tieneDuplicados2 :: [(String, String)] -> Bool
tieneDuplicados2 [] = False
tieneDuplicados2 ((x, y) : xs)
  | elemEnCola x xs == True || elemEnCola y xs == True = True
  | otherwise = tieneDuplicados2 xs

elemEnCola :: String -> [(String, String)] -> Bool
elemEnCola _ [] = False
elemEnCola a ((x, y) : xs)
  | a == x || a == y = True
  | otherwise = elemEnCola a xs

-------------------------------
{- TRATO DE HACER LA FUNCION TIENEDUPLICADOS2

repetido2 :: [(String, String)] -> Bool -- Me dice si hay repetidos en la lista de tuplas
repetido2 [] = False
repetido2 ((x, y) : xs)
  | pertenece (sacoNombresClubes xs) x || pertenece (sacoNombresArqueros xs) y = True
  | otherwise = repetido2 xs

pertenece :: [String] -> String -> Bool -- Me dice si un elemento esta o no en la lista
pertenece [] n = False
pertenece (x : xs) n
  | n == x = True
  | otherwise = pertenece xs n
-}

-------------------------------
--
{- CHAT GPT - Para hacer duplicados2

tieneDuplicados :: [(String, String)] -> Bool
tieneDuplicados [] = False
tieneDuplicados ((x, y) : resto) = (elemEnResto x resto || elemEnResto y resto) || tieneDuplicados resto
  where
    elemEnResto _ [] = False
    elemEnResto a ((x, y) : resto) = a == x || a == y || elemEnResto a resto
-}

--

-------------------------------

-- test: equiposValidos [("A","a"),("B","b"),("D","d"),("C","C")] -> EQ INVALIDO --
-- test: equiposValidos [("A","a"),("C","c"),("B","a")] -> EQ INVALIDO --
-- test: equiposValidos [("A","a"),("C","c"),("D","C")] -> EQ INVALIDO ------------------
-- test: equiposValidos [("A","A"),("A","a"),("D","a")] -> EQ INVALIDO --

-- test: equiposValidos [("A","a"),("B","b"),("C","c")] -> EQ VALIDO
-- test: equiposValidos [("A","a"),("B","c"),("D","d")] -> EQ VALIDO

-- tieneDuplicados2 [("A","a"),("C","c"),("D","C")]

------------------------------------------------------------------------------------------------------
-- Problema 3

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles n ((x, xs) : resto) lista = division (golesDelArquero n ((x, xs) : resto) lista) (sumaDeLaLista lista)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

golesDelArquero :: String -> [(String, String)] -> [Int] -> Int
golesDelArquero n ((x, y) : xs) lista
  | n == fst (head (agregoGoles (sacoNombresArqueros ((x, y) : xs)) lista)) = snd (head (agregoGoles (sacoNombresArqueros ((x, y) : xs)) lista))
  | otherwise = golesDelArquero n xs (tail lista)

-- golesDelArquero "c" [("A","a"),("B","b"),("C","c"),("D","d")] [5,3,4,8] -> result = 4

agregoGoles :: [String] -> [Int] -> [(String, Int)]
agregoGoles [] [] = []
agregoGoles (y : xs) (n : pl) = (y, n) : agregoGoles xs pl

-- porcentajeDeGoles "a" [("A","a"),("B","b")] [5,3] -> result = 5 / 8 = 0.625
-- porcentajeDeGoles "c" [("A","a"),("B","b"),("C","c"),("D","d")] [5,3,4,8] -> result = 4 / 20 = 0.2

------------------------------------------------------------------------------------------------------
-- Problema 4

vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida listaDeArqueros listaGoles = auxValla (agregoGoles (sacoNombresArqueros listaDeArqueros) listaGoles)

auxValla :: [(String, Int)] -> String
auxValla [(x, _)] = x
auxValla ((x, y) : xs)
  | y > snd (head xs) = auxValla ((x, y) : tail xs)
  | otherwise = auxValla xs

-- vallaMenosVencida [("A","a"),("B","b"),("C","c"),("D","d")] [5,3,4,8] -> result = 3 (pues "c" es el que menos recibio goles)

-- auxValla [("a",1),("b",2),("c",3),("d",4)]
-- auxValla [("a",1),("b",5),("c",3),("d",4)]
-- auxValla [("a",1),("b",2),("c",6),("d",4)]
-- auxValla [("a",10),("b",2),("c",3),("d",4)]
