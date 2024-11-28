import Test.HUnit
import Solucion

main = runTestTT tests

-- "nombre" ~: (funcion parametros) ~?= resultado_esperado

tests = test [
  "EJ2 stock vacío" ~: stockDeProducto [] "mesa" ~?= 0,
  "EJ2 producto no está en stock" ~: stockDeProducto [("mesa", 3),("silla",2), ("computadora",1)] "asd" ~?= 0,
  "EJ2 producto está en stock con 1" ~: stockDeProducto [("mesa", 3),("silla",2), ("computadora",1)] "computadora" ~?= 1,
  "EJ2 producto está en stock con 3" ~: stockDeProducto [("mesa", 3),("silla",2), ("computadora",1)] "mesa" ~?= 3,
  "EJ2 producto está en stock único" ~: stockDeProducto [("mesa", 3)] "mesa" ~?= 3,
  "EJ2 producto no está en stock único" ~: stockDeProducto [("mesa", 3)] "silla" ~?= 0,
  "EJ 2 producto está en stock caso del medio:" ~: stockDeProducto [("mesa", 3),("silla",2), ("impresora",1),("computadora",1)] "silla" ~?= 2
  ]
