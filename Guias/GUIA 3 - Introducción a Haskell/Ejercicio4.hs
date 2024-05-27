-- A)

prodInt :: (Integer,Integer) -> (Integer,Integer) -> Integer
prodInt (x,y) (n,m) = x*n + y*m

---------------------------------------------------------------------------------

-- B) 

todoMenor :: (Integer,Integer) -> (Integer,Integer) -> Bool 
todoMenor (a,b) (c,d) | a < c && b < d = True
                      | otherwise = False

---------------------------------------------------------------------------------

-- C)

distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt(((c-a)^2)+((d-b)^2))

---------------------------------------------------------------------------------

-- E)

sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | (mod a n == 0) && (mod b n == 0) && (mod c n == 0) = a + b + c  
                             | (mod a n == 0) && (mod b n == 0) = a + b 
                             | (mod a n == 0) && (mod c n == 0) = a + c
                             | (mod b n == 0) && (mod c n == 0) = b + c 
                             | (mod a n == 0) = a
                             | (mod b n == 0) = b
                             | (mod c n == 0) = c
                             | otherwise = 0

---------------------------------------------------------------------------------

-- F)

posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (a,b,c) | mod a 2 == 0 = 0
                     | mod b 2 == 0 = 1 
                     | mod c 2 == 0 = 2 
                     | otherwise = 4





































