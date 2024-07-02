module Simulacro where

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = False
-- esta mal. lo tenes que corregir

personas :: [(String, String)] -> [String]
personas [] = ["nadie"]
-- esta mal. lo tenes que corregir

amigosDe :: String -> [(String, String)] -> [String]
amigosDe "nadie" [] = ["nadie"]
-- esta mal. lo tenes que corregir

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = "yo"

