sumaPrimerosNImparesEspecial :: Integer -> Integer
sumaPrimerosNImparesEspecial n = sumAux ((2 * n) - 1)

sumAux :: Integer -> Integer
sumAux 1 = 4
sumAux i
  | mod i 2 /= 0 = ((2 * i) + 2) + (sumAux (i - 1))
  | otherwise = 0 + (sumAux (i - 1))
