distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = modulo (a-d) + modulo (b-e) + modulo (c-f)


modulo :: Float -> Float
modulo x | x < 0 = -(x)
         | x >= 0 = x  