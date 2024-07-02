prod :: Integer -> Integer
prod n = prodAUX (2 * n)

prodAUX :: Integer -> Integer
prodAUX b
  | b == 2 = 24
  | b > 2 = (b ^ 2 + 2 * b) * prodAUX (b - 1)