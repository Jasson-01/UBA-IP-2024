type Texto = [Char]
type Nombre = Texto 
type Telefono = Texto 
type Contacto = (Nombre,Telefono)
type ContactosTel = [Contacto] 

--FUNCONES AUXILIARES

elNombre :: Contacto -> Nombre
elNombre (x,_) = x 

elTelefono :: Contacto -> Telefono
elTelefono (_,y) = y

-- PROBLEMA A)
--EJM : enLosContactos "a" [("a","2"),("b","3"),("c","4"),("d","5"),("e","6")]
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos x lista | pertenece x (listaNombres lista) = True
                       | otherwise = False  

listaNombres :: ContactosTel -> [Nombre]
listaNombres [] = []
listaNombres (y:ys) = (elNombre y) : listaNombres ys  

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x (y:ys) | x /= y = pertenece x ys 
                   | otherwise = True


--PROBLEMA B
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto x [] = []
agregarContacto x [n] = [n]
agregarContacto x ((y,n):ys) | ((fst x) == y) && ((snd x) == n) = agregarContacto x ((y,n):ys)
                             | otherwise = x : agregarContacto x ys 

--agregarContacto ('a','1') [('b','2'),('c','2'),('d','2'),('e','2'),('f','2'),('g','2')]





{-
type Texto = [Char]
type Nombre = Texto 
type Telefono = Texto 
type Contacto = (Nombre,Telefono)
type ContactosTel = [Contacto] 


pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x (y:ys) | x /= y = pertenece x ys 
                   | otherwise = True


--PROBLEMA B
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto x [] = []
agregarContacto x [n] = [n]
agregarContacto x ((y,n):ys) | (pertenece x ((y,n):ys) == True) = ((y,n):ys)
                             | otherwise = x : agregarContacto x ys 









-}



















