import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    "laQueMasHayQueCodificar stringDeUnChar" ~: laQueMasHayQueCodificar "a" mapeo_a_probar ~?= 'a',
    "laQueMasHayQueCodificar stringDeUnCharRepetido" ~: laQueMasHayQueCodificar "sssss" mapeo_a_probar ~?= 's',
    "laQueMasHayQueCodificar unaLetrasVariasApariciones" ~: laQueMasHayQueCodificar "casa" mapeo_a_probar ~?= 'a',
    "laQueMasHayQueCodificar variasAparicionesDosLetrasGana1ra" ~: laQueMasHayQueCodificar "cosos" mapeo_a_probar ~?= 'o',
    "laQueMasHayQueCodificar variasAparicionesDosLetrasGana2da" ~: laQueMasHayQueCodificar "cososs" mapeo_a_probar ~?= 's',
    "laQueMasHayQueCodificar variasAparicionesTresLetrasGana3ra" ~: laQueMasHayQueCodificar "cocosss" mapeo_a_probar ~?= 's',
    "laQueMasHayQueCodificar fraseSoloConLetrasDiferentes" ~: laQueMasHayQueCodificar "aos" mapeo_a_probar ~?= 'a',
    "laQueMasHayQueCodificar laMasFrecuenteNoSeMapea" ~: laQueMasHayQueCodificar "ttcotsottstst" mapeo_a_probar ~?= 's'
    ]

mapeo_a_probar = [('a','g'), ('o','a'), ('s','z')]
