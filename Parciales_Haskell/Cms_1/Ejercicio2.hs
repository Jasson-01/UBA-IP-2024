sumaDigitos :: Integer -> Integer
sumaDigitos x
  | x >= 0 && x < 10 = x
  | x >= 10 = sumaDigitos (div x 10) + mod x 10
