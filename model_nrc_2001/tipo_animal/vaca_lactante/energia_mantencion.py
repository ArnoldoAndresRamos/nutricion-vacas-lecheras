"""
Para vacas lactantes y secas 
el requisito de mantenimiento para las vacas lactantes 
se calcula utilizando el tamaño corporal metabólico (BW0.75) y se calcula con la siguiente ecuación 
que incluye un ajuste por actividad.
"""
# NEmaint
def calcular_energia_neta_mantencion(
        peso_vivo: float,
        distancia_recorrida_dia: float = None, 
        numero_viajes:int = None, 
        dias_gestacion: int = None, 
        a1: float = 0.08
        ) -> float:
    """
    peso_vivo               ( float , obligatoria ) = peso vivo del animal en kg.
    distancia_recorrida_dia ( float , opcional    ) = distancia en metros que recorre el animal desde el establo a la sala de ordeña o pastoreo.
    numero_viajes           ( int   , opcional    ) = numero de vueltas que da el animal por dia.
    dias_gestacion          ( int   , opcional    ) = None  el valor deben ser >= a 190 dias.
    a1                      ( float , opcional    ) = es un factor de corrección para vacas maduras (0.08 = 80 kcal/kg Peso Vivo^0.75).
    energia_neta_mantencion ( float , retorna     ) = es el requerimiento de energía para el mantenimiento en Mcal/dia.
    (0.08 = 80 kcal/kg PV^0.75) esto es 80kcal de EM por kilogramo de Peso metabólico = peso vivo^0.75

    """
    if distancia_recorrida_dia is None and dias_gestacion is None:
        return calcular_energia_neta_mantencion_base(peso_vivo, a1)

    peso_cria_al_nacer      = calcular_peso_cria_al_nacer( peso_vivo )
    peso_utero_gravido      = calcular_peso_utero_gravido( dias_gestacion , peso_cria_al_nacer)
    energia_neta_actividad  = calcular_energia_neta_actividad( distancia_recorrida_dia , numero_viajes , peso_vivo)
    peso_ajustado           = peso_vivo - peso_utero_gravido

    return calcular_energia_neta_mantencion_base(peso_ajustado, a1) + energia_neta_actividad


def calcular_peso_cria_al_nacer(peso_vivo):
    return peso_vivo * 0.06275


def calcular_peso_utero_gravido(dias_gestacion, peso_cria_al_nacer):
    """
    """
    return (18 + ((dias_gestacion - 190) * 0.665)) * (peso_cria_al_nacer/ 45)


def calcular_energia_neta_actividad(distancia_recorrida_dia , numero_viajes, peso_vivo):
    """
    Descripción:
        calcula la energia neta de actividad del animal durante el dia

    Parametros:
        distancia_recorrida_dia = distancia recorrrida en metros desde el establo o pastoreo a la sala de ordeña
        numero_viajes           = numero de viajes que se da en el dia desde el establo o pastoreo a la sala de ordeña
        peso_vivo               = peso vivo del animal en kg
    
        retorna :
            energia neta en Mcal/dia
    """
    return (((distancia_recorrida_dia/1000) * numero_viajes) * (0.00045 * peso_vivo)) + (0.0012 * peso_vivo)


# topgra
def relieve(relieve_irregular, peso_vivo ): 
    """
    descripción:
        la funcion calcula el efecto que tiene el relieve en calculo de la energia neta de mantencion para la actividad

    parametros:
        irregular   : boleano si el relieve es irregular True, si no False
        peso_vivo   : peso vivo del animal en kg

    retorna:

    """
    if relieve_irregular:
        return 0.006 * peso_vivo
    return 0


def calcular_energia_neta_mantencion_base(peso_vivo, a1 = 0.08):
    """
    Descripción:
        calcula la energia neta del animal en base solo del peso vivo

    Parametros:
        peso_vivo   = kg de peso de la vaca
        a1          = 0.08 es el requerimientos de mantención termoneutral en Mcal/dia

    retorna:
        energia neta en en Mcal/dia
    """
    return (peso_vivo ** 0.75) * a1



