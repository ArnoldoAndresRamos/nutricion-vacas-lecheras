from requerimientos.vaca_lactante.energia_mantencion import calcular_peso_cria_al_nacer


def calcular_energia_metabolizable_gestacion(dias_gestacion , peso_cria_al_nacer = None , peso_vivo=None):
    """
    descricion:
        la funcion estima los requerimientos de energia para la mantención 
        los ultimos 100 dias de gestación ultimos 2 meses de gestacion

    parametros:
        dias_gestacion      = entre 190 a 279
        peso_cria_al_nacer  = peso cria al necer en kg
        peso_vivo           = peso vivo de vaca en gestación en kg
    
    retorna :
        energia metabilica para la gestación en Mcal/dia
    """

    if dias_gestacion < 190:
        "si los días en gestación son menores a 190 la la energia metabolizables es 0"
        return 0
    if peso_cria_al_nacer==None and peso_vivo!=None:
        peso_cria_al_nacer = calcular_peso_cria_al_nacer(peso_vivo)
    
    if dias_gestacion>=190 and dias_gestacion<= 279 :
        return ( (0.00318*dias_gestacion-0.0352)*(peso_cria_al_nacer/45) )/0.14
    
 
"""
La ME representa la energía disponible en la dieta, pero no tiene en cuenta 
las pérdidas de energía asociadas con la digestión, el metabolismo 
y otros procesos fisiológicos.

La energía neta de lactación, por otro lado, tiene en cuenta estas pérdidas y refleja 
más precisamente la cantidad de energía disponible para la producción de leche
"""  


# calcular energia neta lactancia gestacion
def calcular_energia_neta_lactancia_gestacion(dias_gestacion , peso_cria_al_nacer=None , peso_vivo=None):
    """
    descricion:
        la función estima los requisitos de energia para la mantencion neta de lactancia
        los ultimos 100 dias de gestacion

    parametros:
        dias_gestacion  = entre 190 a 279
        peso_cria       = peso cria al necer en kg
        peso_vivo       = peso vivo de vaca en gestación en kg
    
    retorna :
        energia metabilica para la gestacion en Mcal/dia
    """

    if dias_gestacion < 190:
        "si los días en gestación son menores a 190 la la energia metabolizables es 0"
        return 0
    
    if peso_cria_al_nacer==None and peso_vivo!=None:
        peso_cria_al_nacer = calcular_peso_cria_al_nacer(peso_vivo)
    
    if dias_gestacion>=190 and dias_gestacion<= 279 :
        # redondeamos a 2 digitos
        return round( ( (0.00318*dias_gestacion-0.0352)*(peso_cria_al_nacer/45) )/0.218 , 1)