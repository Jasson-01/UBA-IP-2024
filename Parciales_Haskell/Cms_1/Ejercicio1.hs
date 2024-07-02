sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax (a, b, c)
  | maximo (a, b, c) > minimo (a, b, c) + medio (a, b, c) = True
  | otherwise = False

-- 1ERA FORMA
-- Si a es mayor o igual que b y c devuelve "a", sino comparamos b y c si b es mayor igual a "c" devolvemos "b", si los casos anteriores son falsos se activara otherwise y devolvera "c".
maximo :: (Int, Int, Int) -> Int
maximo (a, b, c)
  | (a >= b) && (a >= c) = a
  | b >= c = b
  | otherwise = c

-- 2DA FORMA de maximo
{- maximo2 :: (Int, Int, Int) -> Int
maximo2 (a, b, c)
  | (a >= b) && (a >= c) = a
  | (b >= a) && (b >= c) = b
  | (c >= b) && (c >= a) = c -}

minimo :: (Int, Int, Int) -> Int
minimo (a, b, c)
  | a < b && a < c = a
  | b < c = b
  | otherwise = c

medio :: (Int, Int, Int) -> Int
medio (a, b, c)
  | a >= b && a <= c || a >= c && a <= b = a
  | b >= c && b <= a || b >= a && b <= c = b
  | otherwise = c

-- 2da forma de medio

medio2 :: (Int, Int, Int) -> Int
medio2 (a, b, c) = (a + b + c) - maximo (a, b, c) - minimo (a, b, c)
