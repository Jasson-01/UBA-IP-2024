--                                         ---   1ERA FORMA  ---
-- PROBLEMA A) ---------

menorDivisor :: Integer -> Integer
menorDivisor n = aux n 2 

aux :: Integer -> Integer -> Integer
aux m n | mod m n == 0 && n <= m  = n
        | mod m n /= 0 = aux m (n+1)

-- PROBLEMA B) ----------

esPrimo :: Integer -> Bool
esPrimo 0 = False
esPrimo 1 = False
esPrimo 2 = True
esPrimo n | menorDivisor n > 1 && menorDivisor n /= n = False
          | otherwise = True

-- PROBLEMA C) ----------

sonCoprimos :: Integer -> Integer -> Bool 
sonCoprimos n m = aux3 n m 

aux3 :: Integer -> Integer -> Bool
aux3 n m | auxMod m (divisoresDe n) == True = False
         | otherwise = True

--Esto me da la lista de los divisores de un numero mayores que 1.        
divisoresDe :: Integer -> [Integer]
divisoresDe n = divisoresAux n 2 


divisoresAux :: Integer -> Integer -> [Integer]
divisoresAux n k | n == k = [n]
                 | mod n k == 0 = k : divisoresAux n (k+1)
                 | otherwise = divisoresAux n (k+1)

auxMod :: Integer -> [Integer] -> Bool
auxMod m [] = False
auxMod m (x:xs) | mod m x == 0 = True
                | otherwise = auxMod m xs 


-- PROBLEMA D) ---------


nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2 
nEsimoPrimo n = auxEnesimo n 0 0

auxEnesimo :: Integer -> Integer -> Integer -> Integer
auxEnesimo n k contador | n == contador = (k-1)
                        | esPrimo k == False = auxEnesimo n (k+1) contador
                        | otherwise = auxEnesimo n (k+1) (contador+1) 



--                                            ---   2da FORMA  ---

--a)
menorDivisor :: Integer -> Integer
menorDivisor n = auxMenorDivisor n 2 

auxMenorDivisor :: Integer -> Integer -> Integer
auxMenorDivisor n m | mod n m == 0 = m
                    | m * m > n = n -- Si no hay divisores menores que la raíz cuadrada de n, entonces n es primo.
                    | mod n m /= 0 = auxMenorDivisor n (m+1)
--b) 
esPrimo :: Integer -> Bool 
esPrimo n = menorDivisor n == n
         
--c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b = mcd a b == 1 

--Usando el algoritmo de Euclides
mcd :: Integer -> Integer -> Integer
mcd a 0 = a --caso base
mcd a b = mcd b (mod a b)
            
--d)
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = auxNEsimoPrimo 2 n  

auxNEsimoPrimo :: Integer -> Integer -> Integer
auxNEsimoPrimo n contador | contador == 0 = n-1 
                          | esPrimo n = auxNEsimoPrimo (n+1) (contador-1) 
                          | otherwise = auxNEsimoPrimo (n+1) (contador)

