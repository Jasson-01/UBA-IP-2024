--PROBLEMA 1

longitud :: [t] -> Integer
longitud [] = 0 
longitud (x:xs) = 1 + longitud xs 

--PROBLEMA 2

ultimo :: [t] -> t 
ultimo [x] = x 
ultimo (x:xs) = ultimo xs  

--PROBLEMA 3

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs 

--PROBLEMA 4

reverso :: [t] -> [t]
reverso [] = []
reverso lista = (ultimo lista) : reverso (principio lista)  