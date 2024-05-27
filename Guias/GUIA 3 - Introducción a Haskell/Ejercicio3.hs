estanRelacionados :: Integer -> Integer -> Bool 
estanRelacionados a b = auxEstanRel a b (div (a*a) (a*b)) 

auxEstanRel :: Integer -> Integer -> Integer -> Bool 
auxEstanRel a b k | (a*a - (a*b*k)) == 0 || (a*a - (a*b*(-k))) == 0 = True
                  | otherwise = False