proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente ((x, y) : xs) n = ganador (votosAux ((x, y) : xs) n)

-- Voy a suponer que cada voto por presidente son distintos y mayores a cero.
ganador :: [(String, Int)] -> String
ganador [(x, y)] = x
ganador ((x, y) : (n, m) : ys)
  | y < m = ganador ((n, m) : ys)
  | otherwise = x

votosAux :: [(String, String)] -> [Int] -> [(String, Int)]
votosAux [] [] = []
votosAux ((x, _) : ys) (n : ns) = (x, n) : votosAux ys ns