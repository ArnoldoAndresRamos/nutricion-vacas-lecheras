
def calcular_energia_neta_mantencion(peso_vivo: float, distancia_recorrida_dia: float = None, numero_viajes:int = None, dias_gestacion: int = None, a1: float = 0.08) -> float:
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


"""
las siguentes son todas las funciones que se usaran en la funcion principal -> "calcular_energia_neta_mantencion()"
"""
def calcular_peso_cria_al_nacer(peso_vivo):
    """
    descripcion:
        calcula el peso del ternero al nacer en base a peso de vaca
        se llama en el modelo del NRC "CBW"

    parametros:
        peso de vaca adulta 

    retorna:
        peso estimado de la cria al nacer en kg
    """
    return peso_vivo * 0.06275


def calcular_peso_utero_gravido(dias_gestacion, peso_cria_al_nacer):
    """
    descripción:
        calcula el peso del utero en crecimiento "CW" en el modelo del NRC
    parametros:
        dias_gestacion : numero de dias de gestación
        peso_cria_al_nacer: peso del ternero al nacer
    """
    return (18 + ((dias_gestacion - 190) * 0.665)) * (peso_cria_al_nacer/ 45)


def calcular_energia_neta_actividad(distancia_recorrida_dia , numero_viajes, peso_vivo):
    return (((distancia_recorrida_dia/1000) * numero_viajes) * (0.00045 * peso_vivo)) + (0.0012 * peso_vivo)

def topogrfia():
    """
    diferencias en la topografía de los animales en pastoreo.
    La topografía puede ser plana o montañosa. No se realiza ningún ajuste si la topografía es plana
    """
    pass

def calcular_energia_neta_mantencion_base(peso_vivo, a1 = 0.08):
    return (peso_vivo ** 0.75) * a1



def calcular_energia_neta_mantencion_gestacion():
    """
    Calculo de energia neta de mantencion para los 2 ultimos meses de gestacion
    """
    pass