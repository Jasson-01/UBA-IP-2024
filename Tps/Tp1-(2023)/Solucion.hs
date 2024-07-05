module Solucion where

type Usuario = (Integer, String) -- (id, nombre)
type Relacion = (Usuario, Usuario) -- usuarios que se relacionan
type Publicacion = (Usuario, String, [Usuario]) -- (usuario que publica, texto publicacion, likes)
type RedSocial = ([Usuario], [Relacion], [Publicacion])

-- Funciones basicas

usuarios :: RedSocial -> [Usuario]
usuarios (us,_,_) = us

relaciones :: RedSocial -> [Relacion]
relaciones (_,rs,_) = rs

publicaciones :: RedSocial -> [Publicacion]
publicaciones (_,_,ps) = ps

idDeUsuario :: Usuario -> Integer
idDeUsuario (id,_) = id 

nombreDeUsuario :: Usuario -> String
nombreDeUsuario (_,nombre) = nombre 

usuarioDePublicacion :: Publicacion -> Usuario
usuarioDePublicacion (u,_,_) = u

likesDePublicacion :: Publicacion -> [Usuario]
likesDePublicacion (_,_,us) = us

-- Ejercicio 1

-- Recibe una red social y devuelve los nombres,sin repetidos entre los mismos,de los usuarios de la red.
nombresDeUsuarios :: RedSocial -> [String]
nombresDeUsuarios red = verificandoUsuarios (usuarios red) 


verificandoUsuarios :: [Usuario] -> [String]
verificandoUsuarios [] = []
verificandoUsuarios (u:us) | pertenece x xs == True = verificandoUsuarios us  -- Si el nombre se repite en la lista lo sacamos
                           | otherwise =  x : verificandoUsuarios us -- Sino, la queremos en la lista
                           where (x:xs) = proyectarNombres (u:us)                    

proyectarNombres :: [Usuario] -> [String] -- Recibe una RedSocial y devuelve todos los nombres de los usuarios 
proyectarNombres [] = []
proyectarNombres (u:us) = (nombreDeUsuario u) : proyectarNombres us   


pertenece :: Eq t => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True 
                   | otherwise = pertenece e xs


-- Ejercicio 2

-- Recibe una red social y un usuario y devuelve una lista con los amigos del usuario en cuestion.
amigosDe :: RedSocial -> Usuario -> [Usuario]
amigosDe red usuario = listaDeAmigos (relaciones red) usuario

listaDeAmigos :: [Relacion] -> Usuario -> [Usuario]
listaDeAmigos [] _ = []
listaDeAmigos (r:rs) usuario | idDeUsuario usuario == idDeUsuario (fst r) = snd r : listaDeAmigos rs usuario
                             | idDeUsuario usuario == idDeUsuario (snd r) = fst r : listaDeAmigos rs usuario
                             | otherwise = listaDeAmigos rs usuario

-- Ejercicio 3

-- Recibe una red social y un usuario y devuelve la cantidad de amigos del usuario
cantidadDeAmigos :: RedSocial -> Usuario -> Int
cantidadDeAmigos red usuario = longitud(amigosDe red usuario)

longitud :: (Eq a1, Num a2) => [a1] -> a2
longitud [] = 0
longitud (x:xs) = longitud xs + 1

 

-- Ejercicio 4

-- Recibe una red social y devuelve aquel usuario con la mayor cantidad de amigos, notese que este usuario puede no ser unico
usuarioConMasAmigos :: RedSocial -> Usuario
usuarioConMasAmigos ([],_,_) = undefined
usuarioConMasAmigos red = cantidadAmigosPorUsuario red (usuarios red)


cantidadAmigosPorUsuario :: RedSocial -> [Usuario] -> Usuario
cantidadAmigosPorUsuario red [u] = u
cantidadAmigosPorUsuario red (u:i:us) | cantidadDeAmigos red u >= cantidadDeAmigos red i = cantidadAmigosPorUsuario red (u:us)
                                      | otherwise = cantidadAmigosPorUsuario red (i:us)


-- Ejercicio 5

-- Recibe una red social y devuelve verdadero si y solo si algun usuario tiene mas de 10 amigos
estaRobertoCarlos :: RedSocial -> Bool
estaRobertoCarlos ([],_,_) = False
estaRobertoCarlos (_,[],_) = False
estaRobertoCarlos red = cantidadDeAmigos red (usuarioConMasAmigos red) > 10

-- Ejercicio 6

-- Recibe una red social y un usuario y devuelve una lista con las publicaciones del usuario
publicacionesDe :: RedSocial -> Usuario -> [Publicacion]
publicacionesDe red usuario = viendoPublicaciones (publicaciones red) usuario

viendoPublicaciones :: [Publicacion] -> Usuario -> [Publicacion]
viendoPublicaciones [] _ = []
viendoPublicaciones (p:ps) usuario | usuario == usuarioDePublicacion p = p : viendoPublicaciones ps usuario
                                   | otherwise = viendoPublicaciones ps usuario



-- Ejercicio 7

-- Recibe una red social y un usuario y devuelve una lista con las publicaciones que le gustan(dio like) al usuario
publicacionesQueLeGustanA :: RedSocial -> Usuario -> [Publicacion]
publicacionesQueLeGustanA red usuario = usuarioEnLikes (publicaciones red) usuario
 
usuarioEnLikes :: [Publicacion] -> Usuario -> [Publicacion]
usuarioEnLikes [] _ = []
usuarioEnLikes (p:ps) usuario | pertenece usuario (likesDePublicacion p) = p : usuarioEnLikes ps usuario
                              | otherwise = usuarioEnLikes ps usuario



-- Ejercicio 8

-- Recibe una red social y dos usuarios y devuelve verdadero si y solo si a los usuarios les gustan las mismas publicaciones
lesGustanLasMismasPublicaciones :: RedSocial -> Usuario -> Usuario -> Bool
lesGustanLasMismasPublicaciones red usuario1 usuario2 = publicacionesQueLeGustanA red usuario1 == publicacionesQueLeGustanA red usuario2


-- Ejercicio 9
--  Recibe una red social y un usuario "a" y devuelve verdadero si y solo si existe algun usuario distinto de "a" que le halla dado like a todas las publicaciones de -- "a"

tieneUnSeguidorFiel :: RedSocial -> Usuario -> Bool
tieneUnSeguidorFiel red usuario = publicacionesIncluidas (usuarios red) (relaciones red) (publicaciones red) usuario

publicacionesIncluidas :: [Usuario] -> [Relacion] -> [Publicacion] -> Usuario -> Bool
publicacionesIncluidas [] _ _ _ = False
publicacionesIncluidas (u:us) rs ps usuario | publicacionesDe (u:us,rs,ps) usuario == [] = False
                                            | estaIncluida (publicacionesDe (u:us,rs,ps) usuario) (publicacionesQueLeGustanA (u:us,rs,ps) u) && (u /= usuario) = True
                                            | otherwise = publicacionesIncluidas us rs ps usuario

estaIncluida :: Eq a => [a] -> [a] -> Bool
estaIncluida [] [] = True
estaIncluida _ []  = False
estaIncluida [] _  = True
estaIncluida (x:xs) (y:ys) | x == y    = estaIncluida xs ys   
                           | otherwise = estaIncluida (x:xs) ys


-- Ejercicio 10
-- Recibe una red social y dos usuarios y devuelve verdadero si y solo si existe una cadena de amistades(relaciones de amistad que concetan a los usuarios) que me ---permita conectar a los usuarios
existeSecuenciaDeAmigos :: RedSocial -> Usuario -> Usuario -> Bool
existeSecuenciaDeAmigos ([],_,_) _ _ = False
existeSecuenciaDeAmigos (_,[],_) _ _ = False
existeSecuenciaDeAmigos red u1 u2 | u1 == u2 = elMismoUsuario red (relaciones red) u1 
                                  | otherwise = pertenece u2 (formandoCadena red (amigosDe red u1) [u1])


elMismoUsuario :: RedSocial -> [Relacion] -> Usuario -> Bool
elMismoUsuario _ [] _ = False 
elMismoUsuario (us,(rp:rps),ps) (r:rs) u1 | (fst r) == u1 && (existeSecuenciaDeAmigos (us, quitar (u1,(snd r)) (rp:rps),ps) u1 (snd r)) == True = True
                                          | (snd r) == u1 && (existeSecuenciaDeAmigos (us, quitar ((fst r),u1) (rp:rps),ps) u1 (fst r)) == True = True
                                          | otherwise = elMismoUsuario (us,(rp:rps),ps) rs u1


formandoCadena :: RedSocial -> [Usuario] -> [Usuario] -> [Usuario]
formandoCadena _ [] _ = []
formandoCadena red (am:ams) (v:vs) | pertenece am (v:vs) = formandoCadena red ams (v:vs)
                                   | otherwise = am : formandoCadena red ((am:ams)++(amigosDe red am)) ((v:vs)++[am])
                                   
quitar :: Eq a => a -> [a] -> [a]
quitar _ [] = []
quitar a (u:us) | a == u = us
                | otherwise = u : quitar a us


