import inspect
import unittest
from solucion import alarma_epidemiologica

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(alarma_epidemiologica)
        if len(code.splitlines()) <= 2:
            Ej2Test.is_default = True

    def setUp(self):
        if Ej2Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    
    def test_caso_base(self):
        registros = [(1, "gripe"), (2, "covid"), (3, "gripe"), (4, "covid"), (5, "covid")]
        infecciosas = ["covid", "ebola"]
        umbral = 0.4
        esperado = {"covid": 0.6}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)

    def test_todas_infecciosas_superan_umbral(self):
        registros = [(1, "gripe"), (2, "gripe"), (3, "gripe"), (4, "covid"), (5, "covid"), (6, "covid")]
        infecciosas = ["gripe", "covid"]
        umbral = 0.3
        esperado = {"gripe": 0.5, "covid": 0.5}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)
    
    def test_nadie_supera_umbral(self):
        registros = [(1, "gripe"), (2, "covid"), (3, "gripe"), (4, "covid"), (5, "ebola")]
        infecciosas = ["gripe", "covid", "ebola"]
        umbral = 0.5
        esperado = {}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)

    def test_ninguna_infecciosa_en_registros(self):
        registros = [(1, "resfriado"), (2, "alergia"), (3, "fractura"), (4, "resfriado"), (5, "alergia")]
        infecciosas = ["gripe", "covid", "ebola"]
        umbral = 0.2
        esperado = {}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)

    def test_sin_registros(self):
        registros = []
        infecciosas = ["gripe", "covid"]
        umbral = 0.2
        esperado = {}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)
    
    def test_alarma_epidemiologica_infecciosas_vacio(self):
        self.assertEqual(alarma_epidemiologica([(3, "Viruela"), (6, "Viruela")], [], 0.5), {})
    
    def test_alarma_epidemiologica_4(self):
        # Caso con pacientes con enfermedades infecciosas, donde pacientes pueden repetirse con misma enfermedad
        enfermedades = [(3, "Viruela"),
                        (6, "Viruela"),
                        (1, "Viruela"),
                        (3, "Cólera"),
                        (10, "Cólera"),
                        (7, "Cólera"),
                        (4, "Fiebre amarilla"),
                        (7, "Cólera"),
                        (3, "Alzheimer")]
        res: dict[str, float] = alarma_epidemiologica(enfermedades, ["Viruela", "Cólera", "Fiebre amarilla"], 0.25)
        
        self.assertEqual(res, {"Cólera": 4/9, "Viruela": 1/3})

   
    def test_alarma_epidemiologica_long_infeccionas_mas_larga(self):
        # Caso con pacientes con enfermedades infecciosas, donde longitud de infecciosas es mayor a pacientes y da el 100%
        res: dict[str, float] = alarma_epidemiologica([(3, "Viruela")], ["Viruela", "Cólera", "Fiebre amarilla"], 0.25)
        self.assertEqual(res, {"Viruela": 1})

if __name__ == '__main__':
    unittest.main(verbosity=2)



   





    
