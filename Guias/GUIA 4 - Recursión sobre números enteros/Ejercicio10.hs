-- Problema a)

f1 :: Integer -> Integer
f1 n | n == 0 = 2^0
     | otherwise = 2^(n) +  f1 (n-1)

-- Problema b)

f2 :: Integer -> Integer -> Integer
f2 n q | n == 1 = q
       | otherwise = q^n + f2 (n-1) q  

-- Problema c)

f3 :: Integer -> Integer -> Integer
f3 n q = aux3 (2*n) q
 
aux3 :: Integer -> Integer -> Integer
aux3 a b | a == 1 = b
         | otherwise = b^a + aux3 (a-1) b 





















