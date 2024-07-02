votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco _ n m = m - (suma n)

suma :: [Int] -> Int
suma [] = 0
suma (x : xs) = x + suma xs
