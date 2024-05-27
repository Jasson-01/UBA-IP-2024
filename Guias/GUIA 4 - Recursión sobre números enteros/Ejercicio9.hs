esCapicua :: Integer -> Bool
esCapicua n = esAux n 1


esAux :: Integer -> Integer -> Bool 
esAux n k | (cantDigitos n <= k) = True
          | (ultimoDigito n == iesimoDigito n k) && ((cantDigitos n) > k) = esAux (div n 10) (k+1)
          | otherwise = False


---------------------------
ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10


primerDigito :: Integer -> Integer
primerDigito n = div n (10^((cantDigitos n) - 1))

-----------------------------------------------------------------------------

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^((cantDigitos n)-i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n = auxCant n 0 

auxCant :: Integer -> Integer -> Integer
auxCant n c | mod n 10 == n = c+1
            | otherwise = auxCant (div n 10) (c+1)


{-
34543 -> True
121 -> True
1231 -> False 
2345432 ->  True
9090909 -> True
23237873232 -> True 
126321 -> False
785087 -> False
-}