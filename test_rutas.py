import unittest
from main import ESTACIONES, CONEXIONES, buscar_ruta

class PruebasSistemaInteligente(unittest.TestCase):
    def test_estaciones_cargadas(self):
        self.assertEqual(len(ESTACIONES), 12)
        self.assertEqual(sum(map(len, CONEXIONES.values())) // 2, 13)

    def test_ruta_norte_dorado(self):
        resultado = buscar_ruta('Portal Norte', 'Portal El Dorado')
        self.assertEqual(resultado['ruta'], ['Portal Norte', 'Calle 100', 'Calle 72', 'Calle 45', 'CAD', 'Av. El Dorado', 'Portal El Dorado'])
        self.assertEqual(resultado['costo_total'], 34.5)
        self.assertEqual(len(resultado['detalles']), 6)

    def test_ruta_inversa(self):
        resultado = buscar_ruta('Portal El Dorado', 'Portal Norte')
        self.assertEqual(resultado['ruta'][0], 'Portal El Dorado')
        self.assertEqual(resultado['ruta'][-1], 'Portal Norte')

    def test_origen_igual_destino(self):
        resultado = buscar_ruta('Ricaurte', 'Ricaurte')
        self.assertEqual(resultado['ruta'], ['Ricaurte'])
        self.assertEqual(resultado['costo_total'], 0)

    def test_estacion_no_existente(self):
        with self.assertRaisesRegex(ValueError, 'no existe'):
            buscar_ruta('Estacion inventada', 'Ricaurte')

    def test_registro_de_exploracion(self):
        resultado = buscar_ruta('Portal Norte', 'Portal El Dorado')
        self.assertGreater(len(resultado['exploracion']), 1)
        self.assertEqual(resultado['exploracion'][0]['estacion'], 'Portal Norte')
        self.assertEqual(resultado['exploracion'][-1]['estacion'], 'Portal El Dorado')

if __name__ == '__main__':
    unittest.main(verbosity=2)
