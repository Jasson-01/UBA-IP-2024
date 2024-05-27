esDivisible :: Integer -> Integer -> Bool
esDivisible 0 _ = True
esDivisible n m | (n-m) < 0 = False
                | otherwise = esDivisible (n-m) m 