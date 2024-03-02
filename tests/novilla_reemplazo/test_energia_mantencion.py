import unittest 
from model_nrc_2001.tipo_animal.novilla_reemplazo.energia_mantencion import calcular_energia_neta_mantencion_sin_estres 

class Test_calcular_energia_mantencion(unittest.TestCase):
    def test_calcular_energia_mantencion():

        energia_novilla = calcular_energia_neta_mantencion_sin_estres(400,20,200,44,3,True,False) 
        self.assertEqual(energia_novilla,8.1)

if __name__=='__main__':
    unittest.main