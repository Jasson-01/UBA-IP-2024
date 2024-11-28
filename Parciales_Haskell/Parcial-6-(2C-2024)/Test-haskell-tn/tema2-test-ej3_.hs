import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "letrasIguales una letra" ~: letrasIguales ['h'] ~?= 0,
    "letrasIguales ninguna igual" ~: letrasIguales ['h','o','y'] ~?=0,
    "letrasIguales todas iguales" ~: letrasIguales ['a', 'a', 'a'] ~?=1,
    "letrasIguales una sola igual" ~: letrasIguales ['s','o','c','i','a','s'] ~?=1,
    "letrasIguales varias iguales" ~: letrasIguales ['c','a','s','c','a','d','a','s'] ~?=3 ,
    "letrasIguales varias iguales con espacios" ~: letrasIguales [' ','c','a','s',' ','c',' ','a','d','a','s', ' '] ~?=3 
    ]
