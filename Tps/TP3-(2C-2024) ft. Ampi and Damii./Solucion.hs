module Solucion where

-- Nombre del grupo : "###"
-- Integrante1: ###
-- Integrante2: ###
-- Integrante3: ###

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool
vuelosValidos [] = True
vuelosValidos (x:xs) = (not(elem x xs) && not(mismoOrigenYDestino x xs) && (vueloValido x)) && (vuelosValidos xs) 

-- OBS: La condición not(elem x xs) es más débil que not(mismoOrigenYDestino x xs), es innecesario incluir la primera,i.e. la segunda implica la primera.
                     
mismoOrigenYDestino :: Vuelo -> AgenciaDeViajes -> Bool 
mismoOrigenYDestino _ [] = False
mismoOrigenYDestino (o,d,t) ((g,e,_):xs) = ((o == g) && (d == e)) || mismoOrigenYDestino (o,d,t) xs 
                                         
vueloValido :: Vuelo -> Bool 
vueloValido (o,d,t) = (o /= d) && (t > 0) 
-----------------------------------------------------------------------------------------------------------------------                        
-- EJERCICIO 2
ciudadesConectadas :: AgenciaDeViajes -> Ciudad -> [Ciudad]
ciudadesConectadas viajes ciudad = (sinRepeticiones (conectandoCiudades viajes ciudad))

conectandoCiudades :: AgenciaDeViajes -> Ciudad -> [Ciudad]
conectandoCiudades [] _ = []
conectandoCiudades ((o,d,t):xs) origen | o == origen = d : conectandoCiudades xs origen
                                       | d == origen = o : conectandoCiudades xs origen 
                                       | otherwise = conectandoCiudades xs origen

sinRepeticiones :: (Eq t) => [t] -> [t]
sinRepeticiones lista = separandoUnicos lista []

separandoUnicos :: (Eq t) => [t] -> [t] -> [t]
separandoUnicos [] completo = completo 
separandoUnicos (x:xs) listaUnicos | not(elem x listaUnicos) = separandoUnicos (xs) (x:listaUnicos)
                                   | otherwise = separandoUnicos xs listaUnicos 
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 3
modernizarFlota :: AgenciaDeViajes -> AgenciaDeViajes
modernizarFlota [] = []
modernizarFlota ((o,d,t):xs) = (o,d,disminuyendo10PorCientoMenos t) : modernizarFlota xs 

disminuyendo10PorCientoMenos :: Float -> Float 
disminuyendo10PorCientoMenos num = num - (num*(10/100))
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 4
ciudadMasConectada :: AgenciaDeViajes -> Ciudad
ciudadMasConectada viajes = ciudadConMasAmigosDuplas (listaCiudadesTuplas (ciudadesUnicas viajes) viajes )

listaCiudadesTuplas ::  [Ciudad] -> AgenciaDeViajes -> [(Ciudad,Int)] 
listaCiudadesTuplas [] viajes = []    
listaCiudadesTuplas (x:xs) viajes = (x,length(ciudadesConectadas viajes x)) : listaCiudadesTuplas xs viajes 

ciudadesUnicas :: AgenciaDeViajes -> [Ciudad]
ciudadesUnicas [] = []
ciudadesUnicas ((o,d,t):xs) = sinRepeticiones (o:d:ciudadesUnicas xs)

ciudadConMasAmigosDuplas :: [(Ciudad,Int)] -> Ciudad
ciudadConMasAmigosDuplas [(a,b)] = a 
ciudadConMasAmigosDuplas ((a,b):(c,d):xs) | b >= d = ciudadConMasAmigosDuplas ((a,b):xs) 
                                          | d >= b = ciudadConMasAmigosDuplas ((c,d):xs) 
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 5
sePuedeLlegar :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool
sePuedeLlegar viajes origen destino = elem destino (amigosDuplas (formandoDuplas viajes) origen) || recorriendoEscalas (formandoDuplas viajes) destino (amigosDuplas (formandoDuplas viajes) origen)
                                    
recorriendoEscalas ::  [(Ciudad, Ciudad)]  -> Ciudad -> [Ciudad] -> Bool
recorriendoEscalas _ _ [] = False
recorriendoEscalas viajes destino (x:xs) = elem destino (amigosDuplas viajes x) || recorriendoEscalas viajes  destino xs  
                                         
formandoDuplas :: AgenciaDeViajes -> [(Ciudad, Ciudad)]
formandoDuplas [] = []
formandoDuplas ((o,d,_):xs) = (o,d) : formandoDuplas xs 

amigosDuplas :: [(Ciudad, Ciudad)] -> Ciudad -> [Ciudad]
amigosDuplas [] _ = []
amigosDuplas (x:xs) ciudad | (fst x) == ciudad = (snd x) : amigosDuplas xs ciudad 
                           | otherwise = amigosDuplas xs ciudad 
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 6
duracionDelCaminoMasRapido :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion
duracionDelCaminoMasRapido vuelos origen destino = minimaDuracion (listaDuraciones vuelos origen destino) 

listaDuraciones :: AgenciaDeViajes -> Ciudad -> Ciudad -> [Duracion]
listaDuraciones [] _ _ =  [] 
listaDuraciones ((o,d,t):xs) origen destino | hayVueloDirecto ((o,d,t):xs) origen destino = (duracionDelVueloDirecto ((o,d,t):xs) origen destino) : listaDuraciones (sacoVueloDirecto ((o,d,t):xs) origen destino) origen destino 
                                            | otherwise = (formandoRutas ((o,d,t):xs) (amigosDe ((o,d,t):xs) origen) destino) ++ listaDuraciones xs origen destino                                              

duracionDelVueloDirecto :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion
duracionDelVueloDirecto ((o,d,t):xs) origen destino | d == destino && o == origen = t 
                                                    | otherwise = duracionDelVueloDirecto xs origen destino

hayVueloDirecto :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool 
hayVueloDirecto [] _ _ = False
hayVueloDirecto ((o,d,t):xs) origen destino | d == destino && o == origen = True 
                                            | otherwise = hayVueloDirecto xs origen destino

sacoVueloDirecto :: AgenciaDeViajes -> Ciudad -> Ciudad -> AgenciaDeViajes
sacoVueloDirecto [] _ _ = []
sacoVueloDirecto ((o,d,t):xs) origen destino | o == origen && d == destino = sacoVueloDirecto xs origen destino 
                                             | otherwise = (o,d,t) : sacoVueloDirecto xs origen destino  

amigosDe :: AgenciaDeViajes -> Ciudad -> AgenciaDeViajes
amigosDe [] ciudad = []
amigosDe ((o,d,t):xs) ciudad | o == ciudad = (o,d,t) : amigosDe xs ciudad 
                             | otherwise = amigosDe xs ciudad  

formandoRutas :: AgenciaDeViajes -> AgenciaDeViajes -> Ciudad -> [Duracion]
formandoRutas _ [] _ = []
formandoRutas vuelos ((o,d,t):xs) destino | not(hayConexion (amigosDe vuelos d) destino) && (((o,d,t):xs) /= []) = formandoRutas vuelos xs destino
                                          | otherwise = (sumandoDuraciones (amigosDe vuelos d) destino t) : formandoRutas vuelos xs destino     

hayConexion :: AgenciaDeViajes -> Ciudad -> Bool
hayConexion [] _ = False
hayConexion ((o,d,t):xs) destino = (d == destino) || hayConexion xs destino
                                  
sumandoDuraciones :: AgenciaDeViajes -> Ciudad -> Duracion -> Duracion
sumandoDuraciones [] _ duracion = duracion
sumandoDuraciones ((o,d,t):xs) destino duracion | destino /= d = sumandoDuraciones xs destino duracion
                                                | otherwise = (t+duracion) 

minimaDuracion :: [Duracion] -> Duracion
minimaDuracion [x] = x 
minimaDuracion (x:y:xs) |  x >= y = minimaDuracion (y:xs)
                        | otherwise = minimaDuracion (x:xs)
-----------------------------------------------------------------------------------------------------------------------
-- EJERCICIO 7
puedoVolverAOrigen :: AgenciaDeViajes -> Ciudad ->  Bool
puedoVolverAOrigen viajes origen = buscandoRutas (formandoDuplas viajes) origen origen 

buscandoRutas :: [(Ciudad, Ciudad)] -> Ciudad -> Ciudad -> Bool
buscandoRutas viajes origen destino = elem destino (formandoVisitados viajes (amigosDuplas viajes origen) [origen]) 
                                  
formandoVisitados :: [(Ciudad, Ciudad)] -> [Ciudad] -> [Ciudad] -> [Ciudad]
formandoVisitados _ [] _  = []
formandoVisitados viajes (x:xs) vistos | elem x vistos = x : formandoVisitados viajes xs vistos 
                                       | otherwise = x : formandoVisitados viajes (amigosDuplas viajes x ++ xs) (x : vistos) 
