combinacionesMenoresOIguales :: Integer -> Integer
combinacionesMenoresOIguales n = combinacionesAux 1 1 n (n * n)

combinacionesAux :: Integer -> Integer -> Integer -> Integer -> Integer
combinacionesAux i j n 0 = 0
combinacionesAux i j n m
  | i * j <= n && j <= n = 1 + combinacionesAux i (j + 1) n (m - 1)
  | otherwise = 0 + combinacionesAux (i + 1) 1 n (m - 1)
