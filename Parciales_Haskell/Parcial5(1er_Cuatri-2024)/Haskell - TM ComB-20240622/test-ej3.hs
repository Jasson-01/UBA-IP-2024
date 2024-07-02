import Test.HUnit
import Solucion

main = runTestTT tests

-- "nombre" ~: (funcion parametros) ~?= resultado_esperado

tests = test [
  "EJ3 dinero con stock y precios vacíos" ~: dineroEnStock [] [] ~?= 0,
  "EJ3 dinero en stock del stock vacío " ~: dineroEnStock [] [("mesa", 10.2),("silla",9.5),("computadora",8.1)] ~?= 0,
  "EJ3 dinero en stock con 1 producto stock 1" ~: dineroEnStock [("silla", 1)] [("silla",11.2)] ~?= 11.2,
  "EJ3 dinero en stock con 1 producto stock 3" ~: dineroEnStock [("silla", 3)] [("silla",11.2)] ~?= 3*11.2,
  "EJ3 dinero con stock limitado igual" ~: dineroEnStock [("mesa", 3),("computadora", 3)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)] ~?= (10.5*3 + 50.5*3),
  "EJ3 dinero con stock limitado distinto" ~: dineroEnStock [("mesa", 2),("computadora",1)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)] ~?= (10.5*2 + 50.5*1),
  "EJ3 dinero con stock completo" ~: dineroEnStock [("mesa", 2),("silla",3),("computadora",1)] [("mesa", 10.5),("silla",22.2),("computadora",50.5)] ~?= (10.5*2 + 22.2*3 + 50.5*1),
  "EJ3 dinero en stock con 1 producto stock 3, precio entero y stock distinto" ~: dineroEnStock [("silla", 3)] [("silla",21), ("cama", 15)] ~?= 3*21,
  "EJ3 dinero con stock distinto ++" ~: dineroEnStock [("mesa", 2),("silla",3),("computadora",1), ("mueble",8)] [("mesa", 10.5),("silla",22.2),("computadora",50.5), ("mueble", 1), ("buque", 100)] ~?= (10.5*2 + 22.2*3 + 50.5*1 + 8*1)
  ]