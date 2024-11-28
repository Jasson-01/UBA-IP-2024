module Solucion where

{--El Departamento de Matemática (DM) de la FCEyN-UBA nos ha encargado que desarrollemos un sistema para el
tratamiento de números naturales. Específicamente les interesa conocer cuándo un número es perfecto y
cuándo dos números son amigos. Aunque por ahí no lo sabías, estos conceptos existen y se definen como:

Un número natural es perfecto cuando la suma de sus divisores propios (números que lo dividen menores a él)
es igual al mismo número. Por ejemplo, 6 es un número perfecto porque la suma de sus divisores propios (1,2 y 3)
es igual a 6.
Dos números naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del
otro. Por ejemplo, 220 y 284 son amigos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 y 110 que sumados dan 284 y los divisores propios de 284 son 1, 2 , 4, 71, 142 que sumados dan 220.
Para implementar este sistema nos enviaron las siguientes especificaciones en lenguaje semiformal y nos pidieron
 que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que
se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
--}
{--Ejercicio 1
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
  requiere: {n > 0}
  asegura: {res es la lista de divisores propios de n, de menor a mayor.}
}
--}

divisoresPropios :: Int -> [Int]
divisoresPropios n = queDividenDesde 1 n

queDividenDesde :: Int -> Int -> [Int]
queDividenDesde d n | d >= n = []
                    | mod n d == 0 = d : pasoRecursivo
                    | otherwise = pasoRecursivo
                    where pasoRecursivo = queDividenDesde (d+1) n



{--Ejercicio 2
problema sonAmigos (n: Z, m: Z) : Bool {
  requiere: {n > 0, m >0 y m es distinto de n}
  asegura: {(res = true <=> n y m son números amigos}
}
--}

sonAmigos :: Int -> Int -> Bool
sonAmigos a b = (sumaDeDivisoresPropios a == b) && (sumaDeDivisoresPropios b == a)

sumaDeDivisoresPropios :: Int -> Int
sumaDeDivisoresPropios n = suma (divisoresPropios n) 

suma :: [Int] -> Int
suma [] = 0
suma (a:as) = a + suma as

{--Ejercicio 3
problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
  requiere: {n > 0}
  asegura: {res es la lista de los primeros n números perfectos, de menor a mayor.}
}
--}

esPerfecto :: Int -> Bool
esPerfecto a = sumaDeDivisoresPropios a == a

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = losPrimerosNPerfectosDesde 1 n

losPrimerosNPerfectosDesde :: Int -> Int -> [Int]
losPrimerosNPerfectosDesde _ 0 = []
losPrimerosNPerfectosDesde n x | esPerfecto n = n: losPrimerosNPerfectosDesde (n+1) (x-1)
                               | otherwise = losPrimerosNPerfectosDesde (n+1) x
            


{--Ejercicio 4
problema listaDeAmigos (lista: seq⟨Z⟩) : seq⟨Z x Z⟩{
  requiere: {todos los números de lista son mayores a 0}
  requiere: {todos los números de lista son distintos}
  asegura: {res es una lista sin repetidos de tuplas de dos números donde esos dos números pertenecen a lista y son amigos}
  asegura: {|res| es la cantidad de tuplas de dos números amigos que hay en lista. Consideraremos que la tupla (a,b) (con a y b pertenecientes a Z) es igual a la tupla (b,a) para contar la cantidad de tuplas.}
}
--}

listaDeAmigos :: [Int] -> [(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos (a:as) = listaDeMisAmigos a as ++ listaDeAmigos as

listaDeMisAmigos :: Int -> [Int] -> [(Int, Int)]
listaDeMisAmigos _ [] = []
listaDeMisAmigos a (b:bs) | sonAmigos a b = (a, b) : pasoRecursivo
                          | otherwise = pasoRecursivo
                          where pasoRecursivo = listaDeMisAmigos a bs
