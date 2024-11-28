import Solucion
import Test.HUnit

main = runTestTT allTests


-- Función de ayuda para crear el mensaje personalizado
assertAproximado :: String -> Float -> Float -> Assertion
assertAproximado nombre esperado obtenido =
    if aproximado obtenido esperado
    then return ()  -- Si es True, el test pasa
    else assertFailure (nombre ++ ": Valor esperado " ++ show esperado ++ ", pero se obtuvo " ++ show obtenido)

allTests = test [
    "promedioPrimo del primer primo 2" ~: assertAproximado "Caso 1" 2.0 (promedioPrimo 2),
    "promedioPrimo de N no primo con repetidos" ~: assertAproximado "Caso 2" 2.5 (promedioPrimo 36), 
    "promedioPrimo de N no primo sin repetidos" ~: assertAproximado "Caso 3" 11.0 (promedioPrimo 57), 
    "promedioPrimo de primo grande" ~: assertAproximado "Caso 4" 41.0 (promedioPrimo 41),
    "promedioPrimo de no primo grande" ~: assertAproximado "Caso 5" 21.5 (promedioPrimo 82),
    "promedioPrimo de no primo grande con repetidos" ~: assertAproximado "Caso 6" 15 (promedioPrimo 164)
    ]

margenFloat = 0.00001
aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat