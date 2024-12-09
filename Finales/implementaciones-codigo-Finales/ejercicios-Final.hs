
-- Final 18 ------------------------------------------------------------------
esSudokuValido :: [[Int]] -> Bool
esSudokuValido m = (not(hayRepetidosEnFilas m)) && (not(hayRepetidosEnColumnas m)) 

hayRepetidosEnFilas :: [[Int]] -> Bool
hayRepetidosEnFilas [] = False
hayRepetidosEnFilas (x:xs) | hayRepetidos x = True
                           | otherwise = hayRepetidosEnFilas xs 

hayRepetidos :: [Int] -> Bool
hayRepetidos [y] = False    
hayRepetidos (x:xs) | esRepetido x xs && x /= 0 = True 
                    | otherwise = hayRepetidos xs 

esRepetido :: Int -> [Int] -> Bool 
esRepetido _ [] = False
esRepetido y (x:xs) | y == x = True
                    | otherwise = esRepetido y xs 

-----
hayRepetidosEnColumnas :: [[Int]] -> Bool
hayRepetidosEnColumnas m = hayRepetidosEnFilas (matrizTranspuesta m)

matrizTranspuesta :: [[Int]] -> [[Int]]
matrizTranspuesta [] = []
matrizTranspuesta ([]:_) = [] -- NO hay mas columnas
matrizTranspuesta m = primeraColumna m : matrizTranspuesta (restoMatriz m)

--Extrae la primera columna
primeraColumna :: [[Int]] -> [Int]
primeraColumna [] = []
primeraColumna (x:xs) = head x : primeraColumna xs 

--Extrae la matriz sin la primera columna
restoMatriz :: [[Int]] -> [[Int]]
restoMatriz [] = []
restoMatriz (x:xs) = tail x : restoMatriz xs  



-- sudoku1 = [
--     [1, 2, 3, 4, 5, 6, 7, 8, 9],
--     [9, 8, 7, 6, 4, 5, 3, 2, 1],
--     [0, 0, 0, 0, 0, 0, 1, 0, 0],
--     [0, 0, 0, 0, 0, 4, 0, 0, 0],
--     [0, 0, 0, 0, 6, 0, 0, 0, 0],
--     [0, 0, 0, 5, 0, 0, 0, 0, 0],
--     [0, 0, 4, 0, 0, 0, 0, 0, 0],
--     [0, 3, 0, 0, 0, 0, 0, 0, 0],
--     [2, 0, 0, 0, 0, 0, 0, 0, 0],
-- ]
-- sudoku1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[9, 8, 7, 6, 4, 5, 3, 2, 1],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 4, 0, 0, 0],[0, 0, 0, 0, 6, 0, 0, 0, 0],[0, 0, 0, 5, 0, 0, 0, 0, 0],[0, 0, 4, 0, 0, 0, 0, 0, 0],[0, 3, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0]]


-- sudoku2 = [
--     [1, 2, 3, 4, 5, 6, 7, 8, 9],
--     [9, 8, 7, 6, 0, 0, 0, 2, 1],
--     [2, 3, 4, 5, 6, 7, 8, 9, 0],
--     [5, 6, 0, 8, 9, 1, 2, 3, 4],
--     [8, 9, 1, 2, 3, 4, 5, 6, 7],
--     [3, 4, 5, 0, 7, 8, 9, 1, 2],
--     [6, 7, 8, 9, 1, 2, 3, 4, 5],
--     [4, 5, 6, 7, 8, 9, 1, 0, 3],
--     [7, 8, 9, 1, 2, 3, 4, 5, 6]
-- ]
--sudoku2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[9, 0, 7, 6, 0, 0, 0, 2, 0],[2, 3, 4, 5, 6, 7, 8, 9, 1],[5, 6, 0, 8, 9, 1, 2, 3, 4],[8, 9, 1, 2, 3, 4, 5, 6, 7],[3, 4, 5, 0, 7, 0, 9, 1, 2],[6, 7, 8, 9, 1, 2, 3, 4, 5],[4, 5, 6, 7, 0, 9, 1, 0, 3],[7, 8, 9, 1, 2, 3, 4, 5, 6]]



----  Final 25 de Julio ...........................................................................................

intercambiandoPorElMayor :: [Int] -> [Int] -> [Int]
intercambiandoPorElMayor [] _ = []
intercambiandoPorElMayor (x:xs) lista = (maximo (subsecuencia x lista)) : intercambiandoPorElMayor xs lista 

subsecuencia :: Int -> [Int] -> [Int]
subsecuencia _ [] = [] -- Cuando elem > S2
subsecuencia 0 (x:_) = [x] -- Hasta la posicion 0
subsecuencia pos (x:xs) = x : subsecuencia (pos-1) xs 

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)


----  Final 1 de Agosto ...........................................................................................

mayorPrimoRepetido :: [Int] -> Int
mayorPrimoRepetido lista = maximoTupla (tuplasPrimos (noHayRepetidos (listaDePrimos lista))  lista)

pertenece :: Int -> [Int] -> Bool
pertenece x [] = False
pertenece x (y:ys) | x /= y = pertenece x ys 
                   | otherwise = True   

noHayRepetidos :: [Int] -> [Int]
noHayRepetidos [] = []
noHayRepetidos (x:xs) | not(pertenece x xs) = x : noHayRepetidos xs 
                      | otherwise = noHayRepetidos xs    

listaDePrimos :: [Int] -> [Int]
listaDePrimos [] = []
listaDePrimos (x:xs) | (esPrimo x) = x : listaDePrimos xs 
                     | otherwise = listaDePrimos xs 

tuplasPrimos :: [Int] -> [Int] -> [(Int,Int)]        
tuplasPrimos [] lista = []
tuplasPrimos (x:xs) lista | esPrimo x = (x,cuantosPrimosHay x lista) : tuplasPrimos xs lista 
                          | otherwise = tuplasPrimos xs lista

esPrimo :: Int -> Bool
esPrimo n = longitud (listaDeDivisores n n) == 2 
          
listaDeDivisores :: Int -> Int -> [Int]
listaDeDivisores _ 0 = []
listaDeDivisores n div | mod n div == 0 = div : listaDeDivisores n (div-1)
                       | otherwise = listaDeDivisores n (div-1)

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs 

cuantosPrimosHay :: Int -> [Int] -> Int
cuantosPrimosHay _ [] = 0
cuantosPrimosHay x (y:ys) | x == y = 1 + cuantosPrimosHay x ys 
                          | otherwise = cuantosPrimosHay x ys 

maximoTupla :: [(Int,Int)] -> Int
maximoTupla [(x,y)] = x
maximoTupla ((x,y):(n,m):ls) | y >= m = maximoTupla ((x,y):ls)
                             | otherwise = maximoTupla ((n,m):ls)


-- matriz003 = [2,2,3,8,3,8,4,3,7,7,9] -> 3










