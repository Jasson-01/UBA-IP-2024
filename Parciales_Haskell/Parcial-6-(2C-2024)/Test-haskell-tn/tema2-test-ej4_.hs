import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "cuantosIguales solo una y en comun" ~: cuantosIguales ['a'] ['a'] ~?=1, 
    "cuantosIguales dos en comun y con repe" ~: cuantosIguales ['c', 'a', 's', 'a'] ['m', 'a', 't', 'e', 'r', 'i', 'a', 'l', 'e', 's'] ~?=2,
    "cuantosIguales sin comun pero repe en cada una" ~: cuantosIguales ['c', 'c', 'c'] ['d', 'd', 'd'] ~?=0,
    "cuantosIguales una sola igual" ~: cuantosIguales ['s','o','c','i','a','s'] ['j','u','a','n'] ~?=1,
    "cuantosIguales todas iguales" ~: cuantosIguales ['m', 'a', 't', 'e', 'r', 'i', 'a', 'l', 'e', 's'] ['m', 'a', 't', 'e', 'r', 'i', 'a', 'l', 'e', 's'] ~?=8,
    "cuantosIguales todas iguales mezcladas" ~: cuantosIguales ['m', 'a', 't', 'e', 'r', 'i', 'a', 'l', 'e', 's'] ['s', 'e', 'l', 'a', 'i', 'r', 'e', 't', 'a', 'm'] ~?=8 
    ]


        