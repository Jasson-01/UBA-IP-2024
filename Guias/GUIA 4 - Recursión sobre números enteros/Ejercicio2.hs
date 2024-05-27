parteEntera :: Float -> Integer 
parteEntera n | (n >= 0) && (n < 1) = 0 
              | (n < 0) && (n > -1) = -0
              | n >= 1 = aux1 n 0
              | n <= -1 = aux2 n 0

aux1 :: Float -> Integer -> Integer
aux1 n k | n < 1 = k
         | n >= 1 = aux1 (n-1) (k+1)

aux2 :: Float -> Integer -> Integer
aux2 n k | n > -1 = k 
         | n <= -1 = aux2 (n+1) (k-1)

--------------------------------------------------------------

--FORMA 2
parteEntera2 :: Float -> Integer
parteEntera2 x | x < 0 = round x
               | otherwise = truncate x 