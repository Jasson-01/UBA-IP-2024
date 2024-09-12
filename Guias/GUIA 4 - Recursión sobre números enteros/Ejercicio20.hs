tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2 | sumaDivisores n1 > sumaDivisores n2 = tomaValorMax n1 (n2 - 1 ) 
                   | sumaDivisores n1 < sumaDivisores n2 = tomaValorMax (n1 + 1) n2 
                   | sumaDivisores n1 == sumaDivisores n2 = n2 
                   | sumaDivisores n2 == sumaDivisores n1 = n1 

sumaDivisores :: Integer -> Integer
sumaDivisores n = auxSumaDivisores n 1

auxSumaDivisores :: Integer -> Integer -> Integer
auxSumaDivisores n d | d > n = 0  -- Caso base: si el divisor es mayor que n, terminamos
                     | mod n d == 0 = d + auxSumaDivisores n (d + 1) 
                     | otherwise = auxSumaDivisores n (d + 1) 
