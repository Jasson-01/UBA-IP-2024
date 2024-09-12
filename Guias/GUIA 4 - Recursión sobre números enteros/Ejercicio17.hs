--                             --- 1ERA FORMA ---

esFibonacci :: Integer -> Bool
esFibonacci n = aux17 n 0

aux17 :: Integer -> Integer -> Bool
aux17 n i | (fibonacci i) > n = False
          | fibonacci i == n = True
          | otherwise = aux17 n (i+1)  

fibonacci ::Integer -> Integer 
fibonacci n | n == 0 = 0
            | n == 1 = 1 
            | otherwise = fibonacci (n-1) + fibonacci (n-2)

--                             --- 2DA FORMA ---

esFibonacci2 :: Integer -> Bool
esFibonacci2 n = auxEsFibonacci n 0 

auxEsFibonacci :: Integer -> Integer -> Bool 
auxEsFibonacci n contador | (fibonacci contador) == n = True  
                          | (fibonacci contador) /= n && ((fibonacci contador) < n) = auxEsFibonacci n (contador+1)
                          | (fibonacci contador) > n = False

fibonacci :: Integer -> Integer
fibonacci 0 = 0 
fibonacci 1 = 1 
fibonacci n = fibonacci (n-1) + fibonacci (n-2) 
