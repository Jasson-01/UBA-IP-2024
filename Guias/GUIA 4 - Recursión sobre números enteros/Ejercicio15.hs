sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m = auxSumaRacionales n m m

auxSumaRacionales :: Integer -> Integer -> Integer -> Float
auxSumaRacionales n m contador | n == 0 = 0 
                               | m == 0 = auxSumaRacionales (n-1) (contador) contador 
                               | otherwise = ( fromIntegral n / fromIntegral m) + auxSumaRacionales n (m-1) contador 
