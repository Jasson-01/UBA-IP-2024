-- # a) ------------------------------------
absoluto :: Int -> Int
absoluto x | x < 0 = x * (-1)
           | x > 0 = x
           | otherwise = x

-- # b) ------------------------------------

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto a b | (a > 0) && (b > 0) && (a >= b) = a 
                   | (a > 0) && (b > 0) && (a <= b) = b
                   | (a < 0) && (b < 0) && (a*(-1) >= b*(-1)) = (-1)*a
                   | (a < 0) && (b < 0) && (a*(-1) <= b*(-1)) = (-1)*b
                   | (a < 0) && (b > 0) && (a*(-1) >= b) = (-1)*a
                   | (a > 0) && (b < 0) && (a*(-1) <= b) = (-1)*b
                   | (a < 0) && (b > 0) && (a*(-1) <= b) = b
                   | (a < 0) && (b > 0) && (a*(-1) >= b) = (-1)*a

-- 2da manera:


maximoAbsoluto2 :: Int -> Int -> Int
maximoAbsoluto2 a b | absoluto a > absoluto b = absoluto a 
                    | absoluto b > absoluto a = absoluto b

-- # c) ------------------------------------

maximo3 :: Int -> Int -> Int -> Int
maximo3 a b c | (a >= b) && (a >= c) = a 
              | (b >= a) && (b >= c) = b 
              | (c >= a) && (c >= b) = c

-- # d) ------------------------------------

algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 a b | (a == 0) || (b == 0) = True
              | otherwise = False 
              
-- Usando Pattern Matching
algunoEs0_2 :: Integer -> Integer -> Bool
algunoEs0_2 _ 0 = True
algunoEs0_2 0 _ = True
algunoEs0_2 _ _ = False

-- # e) ------------------------------------
ambosSon0 :: Integer -> Integer -> Bool
ambosSon0 x y | (x == 0) && (y == 0) = True
              | otherwise = False

-- Usando Pattern Matching
ambosSon0_2 :: Integer -> Integer -> Bool
ambosSon0_2 0 0 = True
ambosSon0_2 _ _ = False

-- # f) ------------------------------------
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | (x > 7) && (y > 7) = True
                   | (3 < x  && x <= 7) && (3 < x && x <= 7) = True
                   | otherwise = False  

-- # g) ------------------------------------
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z 
                    | (x /= y) && (x /= z) && (y == z) = x + y 
                    | (y /= x) && (y /= z) && (x == z) = z + y
                    | (z /= y) && (z /= x) && (y == y) = x + z
                    | otherwise = 0

-- # h) ------------------------------------
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

-- # i) ------------------------------------
digitoUnidades :: Int -> Int
digitoUnidades x | x < 10 = x 
                 | otherwise = mod x 10 

-- # j) ------------------------------------
digitoDecenas :: Int -> Int
digitoDecenas x | x < 10 = x 
                | otherwise = mod x 100 