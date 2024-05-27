todosMenores :: (Integer,Integer,Integer) -> Bool
todosMenores (a,b,c) | (funcionF a > funcionG a) && (funcionF b > funcionG b) && (funcionF c > funcionG c) = True
                     | otherwise = False 

funcionF :: Integer -> Integer
funcionF n | n <= 7 = n^2
           | n > 7 = 2*n -1 

funcionG :: Integer -> Integer
funcionG n | mod n 2 == 0 = div n 2 
           | otherwise = 3*n + 1 


















