pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras ca co h = contarPares ca co h 0 0 

contarPares :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer 
contarPares ca co h p q | p > ca = 0 
                        | q > co = contarPares ca co h (p+1) 0
                        | p^2 + q^2 <= h^2 = 1 + contarPares ca co h p (q + 1) 
                        | otherwise = contarPares ca co h p (q+1)  
 

-- IMPORTANTAE!!! CUIDADO CON EL ORDEN DE LAS GUARDAS, CAMBIA COMPLETAMENTE EL RESULTADO :

-- contarPares ca co h p q | p^2 + q^2 <= h^2 = 1 + contarPares ca co h p (q + 1) 
--                         | q > co = contarPares ca co h (p+1) 0
--                         | p > ca = 0 
--                         | otherwise = contarPares ca co h p (q+1)  
 
