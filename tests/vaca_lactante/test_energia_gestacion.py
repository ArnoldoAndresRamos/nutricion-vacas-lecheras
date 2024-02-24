import unittest
from requerimientos.vaca_lactante.energia_gestacion import calcular_energia_neta_lactancia_gestacion

class test_calcular_energia_neta_lactancia_gestacion(unittest.TestCase):
    
    def test_calcular_energia_neta_lactancia_gestacion(self):
        
        dias_gestacion = 200
        peso_cria_al_nacer = 44
        
        ENL_ge = calcular_energia_neta_lactancia_gestacion( dias_gestacion,peso_cria_al_nacer )
        self.assertEqual(ENL_ge ,2.7)

if __name__=='__main__':
    unittest.main()