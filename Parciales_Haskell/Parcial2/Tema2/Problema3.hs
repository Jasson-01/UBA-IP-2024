porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos p ((x, y) : ys) v = division (votosDelPresidente p ((x, y) : ys) v) (sumaTotalVotos v)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

--------------------------------------------------------------------------------------

sumaTotalVotos :: [Int] -> Int
sumaTotalVotos [] = 0 -- Innecesario por especificacion -- En el requiere !
sumaTotalVotos (x : xs) = x + sumaTotalVotos xs

--------------------------------------------------------------------------------------
votosDelPresidente :: String -> [(String, String)] -> [Int] -> Int
votosDelPresidente p ((x, y) : xs) n = (contadorVotos p (votosAux ((x, y) : xs) n))

contadorVotos :: String -> [(String, Int)] -> Int
contadorVotos p [] = 0 -- Innecesario por especificacion -- En el requiere !
contadorVotos p ((x, y) : ys)
  | p /= x = contadorVotos p ys
  | otherwise = y

votosAux :: [(String, String)] -> [Int] -> [(String, Int)]
votosAux [] [] = []
votosAux ((x, _) : ys) (n : ns) = (x, n) : votosAux ys ns
