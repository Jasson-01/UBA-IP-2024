import inspect
import unittest
from solucionParcial6 import torneo_de_gallinas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''


class Ej1Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(torneo_de_gallinas)
        if len(code.splitlines()) <= 2:
            Ej1Test.is_default = True

    def setUp(self):
        if Ej1Test.is_default:
            self.skipTest(
                "el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_torneo_de_gallinas_ambos_desvian(self):
        ME_DESVIO: str = "me desvio siempre"
        NO_ME_DESVIO: str = "me la banco y no me desvio"

        entrada = {"jugador1": ME_DESVIO, "jugador2": ME_DESVIO}
        salida = {"jugador1": -10, "jugador2": -10}
        res = torneo_de_gallinas(entrada)
        self.assertDictEqual(res, salida)

    def test_torneo_de_gallinas_ambos_no_desvian(self):
        ME_DESVIO: str = "me desvio siempre"
        NO_ME_DESVIO: str = "me la banco y no me desvio"
        entrada = {"jugador1": NO_ME_DESVIO, "jugador2": NO_ME_DESVIO}
        salida = {"jugador1": -5, "jugador2": -5}
        res = torneo_de_gallinas(entrada)
        self.assertDictEqual(res, salida)

    def test_torneo_de_gallinas_uno_y_uno(self):
        ME_DESVIO: str = "me desvio siempre"
        NO_ME_DESVIO: str = "me la banco y no me desvio"

        entrada = {"jugador1": NO_ME_DESVIO, "jugador2": ME_DESVIO}
        salida = {"jugador1": 10, "jugador2": -15}
        res = torneo_de_gallinas(entrada)
        self.assertDictEqual(res, salida)

    def test_torneo_variado_por_4(self):

        ME_DESVIO: str = "me desvio siempre"
        NO_ME_DESVIO: str = "me la banco y no me desvio"

        estrategias = {'Juli': NO_ME_DESVIO, 'Facu': NO_ME_DESVIO,
                       'Lucas': ME_DESVIO, 'Ana': ME_DESVIO}

        res = torneo_de_gallinas(estrategias)

        self.assertDictEqual(res, {
            'Juli': 15,
            'Facu': 15,
            'Lucas': -40,
            'Ana': -40
        })


if __name__ == '__main__':
    unittest.main(verbosity=2)
