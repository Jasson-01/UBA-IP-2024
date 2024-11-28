import Test.HUnit
import Data.List
import Solucion
-- No está permitido agregar nuevos imports.


runCatedraTests = runTestTT allTests

allTests = test [
    "vuelosValidos" ~: testsEjvuelosValidos,
    "ciudadesConectadas" ~: testsEjciudadesConectadas,
    "modernizarFlota" ~: testsEjmodernizarFlota,
    "ciudadMasConectada" ~: testsEjciudadMasConectada,
    "sePuedeLlegar" ~: testsEjsePuedeLlegar,
    "duracionDelCaminoMasRapido" ~: testsEjduracionDelCaminoMasRapido,
    "puedoVolverAOrigen" ~: testsEjpuedoVolverAOrigen
    ]

-- corregir los tests si es necesario con las funciones extras que se encuentran al final del archivo

testsEjvuelosValidos = test [
    "vuelos válido con un elemento" ~: vuelosValidos [("BsAs", "Rosario", 5.0)] ~?= True,
    "Vuelos repetidos" ~: vuelosValidos [("BsAs","Rosario",5.4),("BsAs","Rosario",5.4)] ~?= False,
    "Dos vuelos que tienen origen y destino iguales pero duracion distinta" ~: vuelosValidos [("BsAs", "Rosario", 5.4), ("BsAs", "Rosario", 7.0)] ~?= False,
    "Un vuelo con mismo origen y destino" ~: vuelosValidos [("BsAs","BsAs",8.3)] ~?= False,
    "Varios vuelos validos" ~: vuelosValidos [("BsAs","Rosario",8.3),("Rosario","Mendoza",2.0),("Mendoza","Catamarca",1.3),("Entre Rios","Formosa",1.8),("Formosa","Cordoba",2.1)] ~?= True,
    "Vuelos con duracion negativa" ~: vuelosValidos [("BsAs","Rosario",-8.3),("Mendoza","Tucuman",-2.0)] ~?= False,
    "Un vuelo con mismo origen y destino iguales" ~: vuelosValidos [("BsAs","Rosario",-8.3),("Tucuman","Misiones",3.4),("Cordoba","Cordoba",9.0),("Bolivia","Paraguay",4.0)] ~?= False,
    "Agencia de viajes no tiene ningun vuelo" ~: vuelosValidos [] ~?= True,
    "Dos vuelos que tienen origen y destino iguales pero duracion distinta en varios vuelos " ~: vuelosValidos [("BsAs", "Rosario", 5.4),("Tucuman","Cordoba",3.4),("Catamarca","Bolivia",9.0),("Entre Rios","Bolivia",4.0),("BsAs", "Rosario", 7.0)] ~?= False,
    "vuelos con origen iguales pero destinos diferentes" ~: vuelosValidos [("Rosario","BsAs",3.4),("Tucuman","Mendoza",3.4),("Tucuman","Corrientes",3.4),("Bolivia","Catamarca",3.4),("Tucuman","Formosa",3.4),("Formosa","Rosario",3.4),("Rosario","Tucuman",3.4)] ~?= True
    ]

testsEjciudadesConectadas = test [
    "ciudad conectada con un elemento" ~: ciudadesConectadas  [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
    "Vuelo de regreso" ~: ciudadesConectadas [("BsAs","Rosario",4.5)] "BsAs" ~?= ["Rosario"],
    "Varios vuelos pero solo hay dos vuelos directos" ~: expectPermutacion (ciudadesConectadas [("BsAs","Rosario",4.5),("Tucuman","Mendoza",9.9),("Corrientes","BsAs",2.3),("Mendoza","Rio Negro",7.5)] "BsAs") ["Rosario","Corrientes"],
    "Sin vuelos" ~: ciudadesConectadas [] "BsAs" ~?= [],
    "ciudades conectadas iguales" ~: expectPermutacion (ciudadesConectadas [("BsAs","Rosario",4.5),("Rosario","Tucuman",9.9),("Rosario","BsAs",2.3),("Mendoza","Rosario",7.5)] "Rosario") ["BsAs","Tucuman","Mendoza"],
    "Ciudad no existe" ~: ciudadesConectadas [("BsAs", "Córdoba", 2.0)] "Rosario" ~?= [],
    "Ciudad con 9 conexiones y una repeticion" ~: expectPermutacion  (ciudadesConectadas [("a","c1",8.3),("c2","a",3.4),("a","c3",9.0),("c4","a",3.6),("a","c5",9.0),("c6","a",2.0),("a","c7",7.0),("a","c8",8.0),("c9","a",3.0),("a","c4",3.0)] "a") ["c9","c8","c7","c6","c5","c4","c3","c2","c1"]
    ]

testsEjmodernizarFlota = test [
    "flota modernizada con un elemento" ~: expectlistProximity (listaDeDuraciones (modernizarFlota [("BsAs", "Rosario", 10.0)])) (listaDeDuraciones ([("BsAs", "Rosario", 9.0)])),
    "flota con varios elementos" ~: expectPermutacion((modernizarFlota [("BsAs","Rosario",4.5),("Rosario","Cordoba",9.9),("Rosario","Catamarca",2.3),("Mendoza","Rosario",7.5)])) ([("Mendoza","Rosario",6.75),("Rosario","Catamarca",2.07),("Rosario","Cordoba",8.91),("BsAs","Rosario",4.05)]), 
    "Vuelo con duracion < 1 " ~: expectPermutacion (modernizarFlota [("BsAs","Mendoza",0.8),("New York","BsAs",0.99),("Rosario","Tucuman",0.3)]) [("Rosario","Tucuman",0.27),("New York","BsAs",0.89100003),("BsAs","Mendoza",0.72)],
    "Vuelos con duraciones muy largas" ~: expectPermutacion (modernizarFlota [("BsAs","Cordoba",9999999),("BsAs","Rosario",496543.5),("Rosario","Tucuman",9234456.9),("New York","BsAs",2431234.3),("Mendoza","Rosario",7454312.5)]) [("Mendoza","Rosario",6708881.0),("New York","BsAs",2188110.8),("Rosario","Tucuman",8311011.5),("BsAs","Rosario",446889.15),("BsAs","Cordoba",8999999.1)],
    "Sin Vuelos" ~: modernizarFlota [] ~?= [],
    "Dos vuelos con duracion muy larga" ~: expectPermutacion (modernizarFlota [("a","b",56.5423),("f","g",37.037037)]) ([("f","g", 33.333332),("a","b",50.88807)])
    ]

testsEjciudadMasConectada = test [
    "Ciudad mas conectada que aparece dos veces" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "Dos ciudades con la misma cantidad de conexiones" ~: expectAny(ciudadMasConectada [("a", "b", 4.5),("a", "y", 3.5),("a", "x", 2.1),("o", "z", 7.5),("z", "p", 4.5),("s", "z", 9.1),("l", "x", 2.7),("a", "z", 5.2)]) ["z","a"],
    "Ciudad con una sola conexion" ~: expectAny(ciudadMasConectada [("a","b",6.5)]) ["a","b"],
    "Sin conexiones" ~: expectAny(ciudadMasConectada [("BsAs", "Rosario", 5.0), ("Cordoba", "Mendoza", 3.0)]) ["BsAs","Rosario","Cordoba","Mendoza"],
    "Ciclos en conexiones" ~: ciudadMasConectada [("BsAs", "Rosario", 5.0), ("Rosario", "BsAs", 2.0), ("BsAs", "Córdoba", 1.0)] ~?= "BsAs",
    "Ciudades con ciclos pero gana la que tienen mas conexiones" ~: ciudadMasConectada [("a","b",2.3),("b","a",3.4),("a","e",4.5),("e","a",6.7),("l","i",7.8),("i","m",7.8),("p","i",7.8)] ~?= "i",
    "Vuelo con su reciproco" ~: expectAny(ciudadMasConectada [("a","b",2.3),("b","a",3.4)]) ["a","b"]
    ]

testsEjsePuedeLlegar = test [
    "Se puede llegar caso verdadero con una escala" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= True,
    "Un vuelo directo" ~: sePuedeLlegar [("BsAs","Rosario",5.3)] "BsAs" "Rosario" ~?= True,
    "Agencia sin vuelos" ~: sePuedeLlegar [] "BsAs" "Rosario" ~?= False,
    "Vuelo con una escala" ~: sePuedeLlegar [("BsAs","Rosario",2.2),("Rosario","Mendoza",6.7)] "BsAs" "Mendoza" ~?= True,
    "Dos rutas con una escala y el mismo destino" ~: sePuedeLlegar [("BsAs","Tucuman",2.5),("BsAs","Mendoza",4.7),("Tucuman","Entre Rios",7.2),("Mendoza","Entre Rios",5.6)] "BsAs" "Entre Rios" ~?= True,
    "Varios rutas con una escala pero no llega a su destino" ~: sePuedeLlegar [("BsAs","Rosario",2.3),("Rosario","Mendoza",5.3),("BsAs","Entre Rios",2.4),("Entre Rios","Cordoba",9.8),("BsAs","Catamarca",7.8),("Rio Negro","Bariloche",4.2)] "BsAs" "Bariloche" ~?= False,
    "Ciudades no conectadas" ~: sePuedeLlegar [("a", "x", 4.5),("o", "z", 4.5),("BsAs", "Rosario", 5.0),("z", "p", 4.5),("s", "z", 4.5)] "Córdoba" "Mendoza" ~?= False,
    "Ruta inexistente" ~: sePuedeLlegar [("Tucuman","Mendoza",3.4),("Tucuman","Corrientes",3.4),("Cordoba", "Rosario", 5.0),("Bolivia","Catamarca",3.4),("Tucuman","Formosa",3.4)] "BsAs" "Rosario" ~?= False
    ]

testsEjduracionDelCaminoMasRapido = test [
    "duración del camino más rápido con una escala" ~: expectAnyTuplaAprox("BsAs",duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Cordoba")  [("BsAs",10.0)],
    "Dos vuelos con el mismo destino pero solo uno tiene la duracion mas rapida" ~: expectAnyTuplaAprox ("BsAs",duracionDelCaminoMasRapido [("BsAs","Rosario",6.5),("BsAs","Cordoba",5.7),("Rosario","Entre Rios",2.3),("Cordoba","Entre Rios",1.3)] "BsAs" "Entre Rios") [("BsAs",8.8),("BsAs",7.0)],
    "vuelo directo" ~: expectAnyTuplaAprox("BsAs",duracionDelCaminoMasRapido [("BsAs","Rosario",2.9)] "BsAs" "Rosario") [("BsAs",2.9)],
    "tres vuelos con el mismo destino pero solo una tiene la duracion mas rapida" ~: expectAnyTuplaAprox("BsAs",duracionDelCaminoMasRapido [("Mendoza","Entre Rios",7.5),("BsAs","Cordoba",1.0),("Catamarca","La Rioja",5.3),("Cordoba",
    "Tucuman",8.0),("BsAs","Mendoza",4.0),("Rio Negro","Catamarca",2.0),("Mendoza","Tucuman",1.0),("Corrientes","Rio Negro",2.0),("BsAs","Rio Negro",9.0),("Mar Del Plata","Bariloche",1.0),("Bariloche","Mar Del Plata",4.0),("Rio Negro","Tucuman",1.0)] "BsAs" "Tucuman") [("BsAs",9.0),("BsAs",5.0),("BsAs",10.0)], 
    "tres vuelos con el mismo destino y dos tienen la misma duracion" ~: expectAnyTuplaAprox("Corrientes",duracionDelCaminoMasRapido [("BsAs","Catamarca",7.5),("Corrientes","Entre Rios",1.0),("Tucuman","Catamarca",0.2),("Corrientes","BsAs",8.0),("Cordoba","Mendoza",4.0),("Corrientes","Tucuman",0.1),("Entre Rios","Catamarca",1.0),("Catamarca","Bariloche",2.0),("Corrientes","Paraguay",0.1),("Entre Rios","Catamarca",1.0),("Paraguay","Catamarca",0.2),("Paraguay","Bolivia",1.0)] "Corrientes" "Catamarca")  [("Corrientes",0.3),("Corrientes",0.3),("Corrientes",2)],
    "Una escala cerrada y otra llega al destino" ~: expectAnyTuplaAprox("Mendoza",duracionDelCaminoMasRapido [("BsAs","Catamarca",7.5),("Mendoza","Bolivia",1.0),("Bolivia","Catamarca",0.2),("Mendoza","BsAs",2.0),("Tucuman","Mendoza",4.0),("BsAs","Rio Negro",0.1)] "Mendoza" "Rio Negro") [("Mendoza",2.1)],
    "Una ruta directa y una ruta con una escala" ~: expectAnyTuplaAprox("Lima",duracionDelCaminoMasRapido [("Lima","Bogota",8.3),("Bogota","Tokio",3.4),("Lima","Sucre",9.0),("Lima","Tokio",1.0),("Sucre","Tokio",9.0),("Lima","Caracas",2.0)] "Lima" "Tokio") [("Lima",1.0),("Lima",11.7),("Lima",18.0)]
    ]

testsEjpuedoVolverAOrigen = test [
    "puedo volver a origen caso verdadero con una escala" ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" ~?= True,
    "No hay vuelta al origen" ~: puedoVolverAOrigen [("BsAs","Rosario",3.4),("Rosario","Entre Rios",4.7)] "BsAs" ~?= False,
    "Ruta con cuatro escalas desordenadas pudiendo regresar al origen" ~: puedoVolverAOrigen [("BsAs","Mendoza",3.4),("BsAs","Rosario",3.4),("Cordoba","Catamarca",3.4),("Rosario","Tucuman",3.4),("Rosario","Corrientes",3.4),("Entre Rios","Misiones",3.4),("Corrientes","Entre Rios",3.4),("Misiones","BsAs",3.4)] "BsAs" ~?= True,
    "Ruta con 5 escalas desordenas pero no puede volver al origen" ~: puedoVolverAOrigen [("Cordoba","Misiones",3.4),("Corrientes","Mendoza",3.4),("Rosario","Catamarca",3.4),("Mar Del Plata","Tucuman",3.4),("Catamarca","Formosa",3.4),("Formosa","Cordoba",3.4),("Misiones","Neuquen",3.4)] "Rosario" ~?= False,
    "Origen con multiples destinos directos pero solo una ruta regresa" ~: puedoVolverAOrigen [("Cordoba","Misiones",3.4),("BsAs","Mendoza",3.4),("BsAs","Corrientes",3.4),("Mar Del Plata","Tucuman",3.4),("BsAs","Formosa",3.4),("Formosa","Cordoba",3.4),("Cordoba","BsAs",3.4)] "BsAs" ~?= True,
    "Camino muy largo, pero si puedes volver al origen" ~: puedoVolverAOrigen [("BsAs","Rosario",7.3),("Rosario","Corrientes",2.3),("Mendoza","Entre Rios",6.1),("BsAs","Formosa",54.1),("BsAs","San Juan",8.3),("Bolivia","Rio Negro",1.2),("San Juan","Corrientes",9.1),("San Juan","Catamarca",7.5),("San Juan","Bolivia",5.4),("BsAs","Catamarca",6.2),("Mendoza","Cordoba",3.5),("Cordoba","Mendoza",4.3),("Cordoba","Rio Negro",5.3),("Cordoba","Chile",1.3),("Cordoba","Paraguay",1.37),("Paraguay","Misiones",8.1),("Rio Negro","Bolivia",78.3),("Bolivia","BsAs",1.3)] "BsAs" ~?= True,
    "Camino muy largo pero no puedes volver al origen" ~: puedoVolverAOrigen [("BsAs","Rosario",7.3),("Rosario","Corrientes",2.3),("Mendoza","Entre Rios",6.1),("BsAs","Formosa",54.1),("BsAs","San Juan",8.3),("Bolivia","Rio Negro",8.2),("San Juan","Corrientes",1.1),("San Juan","Catamarca",7.5),("San Juan","Bolivia",1.4),("BsAs","Catamarca",6.2),("Mendoza","Cordona",7.5),("Cordoba","Mendoza",44.3),("Cordoba","Rio Negro",52.3),("Cordoba","Chile",9.3),("Cordoba","Paraguay",1.37),("Paraguay","Misiones",3.1),("Rio Negro","Bolivia",8.3)] "BsAs" ~?= False,
    "Agencia vacía" ~: puedoVolverAOrigen [] "BsAs" ~?= False
    ]

-- Funciones extras

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat

-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (String, Float) -> [(String, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (String, Float) -> [(String, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)


-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)

-- Funciones Auxiliares:

listaDeDuraciones :: [(String,String,Float)] -> [Float]
listaDeDuraciones [] = []
listaDeDuraciones ((x,y,d):xs) = d : listaDeDuraciones xs 
