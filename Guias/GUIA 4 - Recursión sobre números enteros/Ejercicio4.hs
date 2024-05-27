sumaImpares :: Integer -> Integer 
sumaImpares n = auxImpares n 0 

auxImpares :: Integer -> Integer -> Integer
auxImpares 0 _ = 0 
auxImpares n c = (2*c + 1) + (auxImpares (n-1) (c+1)) 



-- 1,3,5,7,9,11,13,...