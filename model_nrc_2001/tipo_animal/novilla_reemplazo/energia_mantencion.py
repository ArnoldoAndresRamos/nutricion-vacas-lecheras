# The maintenance requirements for heifers without stress (NEmaintNS) are calculated with the following equation


def calcular_energia_neta_mantencion_sin_estres(
        peso_vivo=None , temperatura_previa=None , dias_gestacion=None , peso_cria_al_nacer= None, 
        grado_condicion_corporal_5  = None , pastoreo= None , relieve_irregular= None ):
    
    """
    descrición:
        calcula la energia de mantencion para novillas preñadas sin estres
    parametros:
        peso_vivo                   = peso corporal del animal en kg 
        temperatura_previa          = en °C  "PrevTemp en el modelo de la nrc"
        dias_gestacion              = numero de dias de gestacion
        peso_cria_al_nacer          = peso en kg de ternero de puede calcular o ingresar valor
        a1                          = 0.086 es el requerimientos de mantención termoneutral en Mcal/dia
        grado_condicion_corporal_5  = condicion corporal del animal de 1 a 5 CS5
        pastando                    = si la novilla
        relieve_irregular           = boleano si el el terreno es irregular == True
    
    retorna:
        energia neta de mantención en Mcal/dia
    """
    
    if peso_cria_al_nacer == None:
        peso_cria_al_nacer = calcular_peso_cria_al_nacer(peso_vivo)
    
    a1                      = 0.086 # a1
    peso_corporal_reducido  = calcular_peso_corporal_reducido(peso_vivo) # SBW
    peso_utero_gravido      = calcular_peso_utero_gravido(dias_gestacion , peso_cria_al_nacer) # CW
    ajuste_plano_alimentacion_previa = calcular_ajuste_plano_alimentacion_previa(grado_condicion_corporal_5) # COMP
    a2                      = calcular_a2(temperatura_previa) # a2
    energia_neta_actividad  = calcular_energia_neta_mantecion_actividad( peso_vivo , pastoreo) + relieve( relieve_irregular , peso_vivo)

    return ( (peso_corporal_reducido-peso_utero_gravido)**0.75 ) * ((a1*ajuste_plano_alimentacion_previa) + a2) + energia_neta_actividad



def calcular_peso_corporal_reducido(peso_vivo):
    """
    descripción:
        la funcion calcula a partir del peso vivo del animal el peso corporal reducido llamdo en el modelo del NRC como 
        "SBW" shrunk body weight
    parametros:
        peso vivo del animal "novilla de reeplazo" en kg
    retorna:
        peso reducido en kg
    """
    return peso_vivo* 0.96


def calcular_peso_cria_al_nacer(peso_vivo):
    """
    descripcion:
        calcula el peso del ternero al nacer en base a peso de vaca
        se llama en el modelo del NRC "CBW"
    
    parametros:
        peso_vivo = peso de vaca adulta en kg
    
    retorna:
        peso de ternero en kg
    """
    return peso_vivo * 0.06275


def calcular_peso_utero_gravido(dias_gestacion, peso_cria_al_nacer:float):
    """
    descripción:
        calcula el peso del utero en crecimiento "CW" en el modelo del NRC
    
    parametros:
        dias_gestacion : numero de dias de gestación
        peso_cria_al_nacer: peso del ternero puede se calculada con la funcion "peso_cria_al_nacer(peso_vivo)"
    
    retorna:
        peso usterogravido en kg    
    """
    return (18 + (( dias_gestacion - 190) * 0.665)) * (peso_cria_al_nacer/ 45)

    
def calcular_a2(temperatura_previa):
    """
    descripción:
        Ajuste de mantenimiento para la temperatura ambiente (Mcal/día/BW^0,75)
        la funcion calcula el ajuste realizado en el mantenimiento de los animales basado en la 
        temperatura ambiente previa
    
    parametros: 
        - temperatura_previa = en C° "PrevTemp" en el modelo de la nrc
    
    retorna:

    """
    return 0.0007 * (20 - temperatura_previa)


# COMP
def calcular_ajuste_plano_alimentacion_previa(grado_condicion_corporal_5):
    """
    descripción:
        calcula el ajuste del estado de nutrición previo de un animal en sus necesidades de energía neta para mantenimiento
        en el modelo NRC es "COMP"
    parametros:
        grado_composicion_corporal_5 puntaje en la escala 1 a 5 de la condicion corporal del animal
        "es transformado a la escala de composición corporal de 1 a 9"

    retorna:
        condicion corporal del animal en puntuacion 1 a 9    
    """
    return 0.8 + ( (convertir_escala_5_a_9( grado_condicion_corporal_5)-1) * 0.05 )


# CS9
def convertir_escala_5_a_9( grado_condicion_corporal_5):
    """
    descripción:
        Convierte el grado de composición corporal de una escala de 1 a 5 a una escala de 1 a 9.

    Parámetros:
        grado_composicion_corporal_5 (int): El grado en la escala de 1 a 5.

    Retorna:
        El equivalente en la escala de 1 a 9.
    """
    return ((grado_condicion_corporal_5 - 1) * 2) + 1

def calcular_energia_neta_mantecion_actividad(peso_vivo , pastoreo):
    """
    descripción:
        calcula la energia neta de actividad para novillas de reemplazo
    
    parametros:
        peso_vivo   : peso del animal en kg 
        pastoreo    : boolean si el animal pastorea o no
    
    retorna
    """
    if pastoreo:
        return ((0.0009 * peso_vivo) + (0.0016 * peso_vivo))
    return 0


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






"""
Para las novillas, estos requisitos luego se ajustan según los efectos de la 
temperatura que se basan en el área de superficie,la producción de calor, 
el aislamiento del tejido y del pelaje, la condición del pelaje y la temperatura. 
Se calcula la primera superficie (SA) y producción de calor (HP) (Mcal/m2/día).

"""

# SA
def calculo_superficie_piel( peso_vivo ):
    """
    descripcion:
        calcula la superficie de la piel de la novilla en m2
        utiliza la funcion que calcular_peso_corporal_reducido(peso_vivo) que esta mas arriba en este mismo archivo 

    Parametros:
        peso_vivo = en kg

    retorna:
        m2 de superficie de piel del animal
    """
    return 0.09 * ( calcular_peso_corporal_reducido(peso_vivo)**0.67 )


# HP
def calcular_produccion_de_calor():
    """
    Descripcion:
        Calcula la produccion de calor del animal en Mcal/m2/dia
    Parametros:

    """
    return 0
