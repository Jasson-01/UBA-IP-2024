import Test.HUnit
import Solucion

main = runTestTT tests

-- "nombre" ~: (funcion parametros) ~?= resultado_esperado

tests = test [
  "EJ1 stock vacio" ~: generarStock [] ~?= [],
  "EJ1 stock con 1 producto 1 aparición" ~: generarStock ["mesa"] ~?= [("mesa", 1)],
  "EJ1 stock con 1 aparicion 3 productos" ~: sonIguales_hunit (generarStock ["mesa", "silla", "computadora"])
                                                                [("mesa", 1),("silla",1), ("computadora",1)] ~?= True,

  "EJ1 stock con distintas apariciones" ~: sonIguales_hunit (generarStock ["mesa", "mesa", "silla", "computadora", "mesa", "silla"])
                                                                          [("mesa", 3),("silla",2), ("computadora",1)] ~?= True,

  "EJ1 stock con mismas apariciones" ~: sonIguales_hunit (generarStock ["mesa", "mesa", "mesa", "silla", "silla", "silla", "computadora", "computadora", "computadora"])
                                                                          [("mesa", 3),("silla",3), ("computadora",3)] ~?= True,

  "EJ1 stock con muchas apariciones del mismo" ~: generarStock ["mesa", "mesa", "mesa", "mesa"] ~?= [("mesa", 4)],
  --agregamos, otros casos:
  "EJ1 stock con 1 y 2 apariciones 2 productos" ~: sonIguales_hunit (generarStock ["cama", "mesa", "cama"])
                                                                [("mesa", 1),("cama", 2)] ~?= True,

  "EJ1 stock con varias apariciones varios productos" ~: sonIguales_hunit (generarStock ["cama", "mesa", "cama", "tele", "cama", "mesa", "tele", "tele", "tele", "avion", "helicoptero"])
                                                                [("mesa", 2),("cama", 3), ("tele", 4), ("avion", 1), ("helicoptero", 1)] ~?= True
  ]

quitar_hunit :: (Eq t) => t -> [t] -> [t]
quitar_hunit x (y:ys) | x == y = ys
                | otherwise = y : quitar_hunit x ys

incluido_hunit :: (Eq t) => [t] -> [t] -> Bool
incluido_hunit [] l = True
incluido_hunit (x:c) l = elem x l && incluido_hunit c (quitar_hunit x l)

sonIguales_hunit :: (Eq t) => [t] -> [t] -> Bool
sonIguales_hunit xs ys = incluido_hunit xs ys && incluido_hunit ys xs
