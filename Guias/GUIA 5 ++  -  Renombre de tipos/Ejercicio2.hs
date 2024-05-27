type Año = Integer
type EsBisiesto = Bool

bisiesto :: Año -> EsBisiesto 
bisiesto y | mod y 4 /= 0 || auxBisiesto y = False
           | otherwise = True

auxBisiesto :: Año -> EsBisiesto
auxBisiesto n = (mod n 100 == 0) && (mod n 400 /= 0) 

{-
bisiesto :: Integer -> Bool 
bisiesto y | mod y 4 /= 0 || auxBisiesto y = False
           | otherwise = True

auxBisiesto :: Integer -> Bool
auxBisiesto n = (mod n 100 == 0) && (mod n 400 /= 0) 
              
-}





























