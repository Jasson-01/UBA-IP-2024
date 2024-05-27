todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | mod n 10 == n = True    
                      | mod n 10 /= (mod (div n 10) 10) = False
                      | mod n 10 == (mod (div n 10) 10) = todosDigitosIguales (div n 10)