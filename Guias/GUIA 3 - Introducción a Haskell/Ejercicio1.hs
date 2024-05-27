-- Problema a) ---------------------------------------
f :: Integer -> Integer
f n | n == 1 = 8 
    | n == 4 = 131
    | n == 16 = 16

-- Problema b) ---------------------------------------
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- Problema c) ---------------------------------------
h :: Integer -> Integer -- h = fog
h x = g (f x)

-- Problema d) ---------------------------------------
k :: Integer -> Integer -- k = gof
k x == f (g x)





