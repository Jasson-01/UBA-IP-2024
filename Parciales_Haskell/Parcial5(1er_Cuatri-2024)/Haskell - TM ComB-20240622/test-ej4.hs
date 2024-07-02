import Test.HUnit
import Solucion

main = runTestTT tests

-- "nombre" ~: (funcion parametros) ~?= resultado_esperado

tests = test [
  "EJ4 aplicar ofertas sobre precios vacíos" ~:  aplicarOferta [] [] ~?= [],
  "EJ4 aplicar ofertas sin stock" ~:   aplicarOferta [] [("mesa", 10.5),("silla",22.2),("computadora",50.5)]
                                                                     ~?= [("mesa", 10.5),("silla",22.2),("computadora",50.5)],
  "EJ4 aplicar ofertas modifica los precios correctos" ~:   aplicarOferta [("mesa", 12),("computadora",10)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)]
                                                                     ~?= [("mesa", 10.5*0.8),("silla",22.2),("computadora",50.5)],
  "EJ4 aplicar ofertas modifica todos los precios" ~:   aplicarOferta [("mesa", 11),("silla",11),("computadora",11)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)]
                                                                     ~?= [("mesa", 10.5*0.8),("silla",22.2*0.8),("computadora",50.5*0.8)],
  "EJ4 aplicar ofertas no modifica ningún precio" ~:   aplicarOferta [("mesa", 9),("silla",10),("computadora",2)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)]
                                                                     ~?= [("mesa", 10.5),("silla",22.2),("computadora",50.5)],
  "EJ4 aplicar ofertas sobre un precio no modifica" ~:   aplicarOferta [("mesa", 9)] [("mesa", 10.5)]
                                                                                   ~?= [("mesa", 10.5)],
  "EJ4 aplicar ofertas sobre un precio debe modificar" ~:   aplicarOferta [("mesa", 20)] [("mesa", 10.5)]
                                                                                   ~?= [("mesa", 10.5*0.8)]
  ]

