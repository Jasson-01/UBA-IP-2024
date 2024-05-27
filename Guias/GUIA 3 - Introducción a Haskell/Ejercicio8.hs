comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0


sumaUltimosDosDigitos ::Integer -> Integer
sumaUltimosDosDigitos n = (mod (modulo n) 10) + (mod ((div (modulo n) 10)) 10)


modulo :: Integer -> Integer
modulo x | x < 0 = -(x)
         | x >= 0 = x