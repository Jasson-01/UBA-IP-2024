amigosDe :: String -> [(String, String)] -> [String]
amigosDe x [] = []
amigosDe x ((y, z) : ys)
  | x == y = z : amigosDe x ys
  | x == z = y : amigosDe x ys
  | otherwise = amigosDe x ys

{-

amigosDe "a" [("a","b"),("a","c"),("d","x"),("a","g")]

-}