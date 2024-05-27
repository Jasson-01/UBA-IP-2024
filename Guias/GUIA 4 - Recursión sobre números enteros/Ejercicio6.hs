sumaDigitos :: Integer -> Integer 
sumaDigitos n | mod n 10 == n = n
              | otherwise = (mod n 10) + (sumaDigitos (div n 10))


