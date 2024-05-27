--PROBLEMA 1 

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x (y:ys) | x /= y = pertenece x ys 
                   | otherwise = True

--PROBLEMA 2

todosIguales :: (Eq t) => [t] -> Bool 
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales (x:xs) 
                      | otherwise = False

--PROBLEMA 3

todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos [x] = True
todosDistintos (x:y:xs) | pertenece x (y:xs) == False = todosDistintos (y:xs)
                        | otherwise = False   

--PROBLEMA 4

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:y:xs) | pertenece x (y:xs) == False = hayRepetidos (y:xs)
                      | otherwise = True

--PROBLEMA 5

quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n /= x = x : quitar n (xs)
                | otherwise = xs 

--PROBLEMA 6

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs) | n /= x = x : quitarTodos n xs 
                     | otherwise = quitarTodos n xs 

--PROBLEMA 7

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = [] 
eliminarRepetidos (x:xs) = x: eliminarRepetidos (quitarTodos x xs) 

--PROBLEMA 8

mismosElementos :: (Eq t) => [t] -> [t] -> Bool 
mismosElementos [] [] = True
mismosElementos lista1 lista2 | (auxMismosL1 lista1 lista2) && (auxMismosL2 lista1 lista2) = True
                              | otherwise = False 

auxMismosL1 :: (Eq t) => [t] -> [t] -> Bool 
auxMismosL1 [] _ = True
auxMismosL1 (x:xs) lista2 | (pertenece x lista2) = auxMismosL1 xs lista2
                          | otherwise = False

auxMismosL2 :: (Eq t) => [t] -> [t] -> Bool 
auxMismosL2 _ [] = True
auxMismosL2 lista1 (y:ys) | (pertenece y lista1) = auxMismosL2 lista1 ys
                          | otherwise = False

--PROBLEMA 9

capicua :: (Eq t) => [t] -> Bool 
capicua [] = True
capicua [x] = True 
capicua lista = esCApicua lista 

--Auxiliares:

esCApicua :: (Eq t) => [t] -> Bool 
esCApicua listaB | sonIguales listaB (reverso listaB) = True
                 | otherwise = False 

sonIguales :: (Eq t) => [t] -> [t] -> Bool 
sonIguales [] [] = True
sonIguales (x:xs) (y:ys) | x == y = sonIguales xs ys 
                         | otherwise = False


reverso :: [t] -> [t]
reverso [] = []
reverso lista = (ultimo lista) : reverso (principio lista) 

ultimo :: [t] -> t 
ultimo [x] = x 
ultimo (x:xs) = ultimo xs  

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs 
































