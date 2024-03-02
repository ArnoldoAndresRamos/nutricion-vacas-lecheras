"""
Calculo de los requerimientos de Proteina para el manteniemiento de vacas en lactancia,
vacas secas y novillas de reemplazo
"""

# 
def calcular_proteina_metabolizable_mantenimiento( consumo_materia_seca, total_nutrientes_digestibles, peso_vivo , dias_gestacion , peso_cria_al_nacer = None):

    """ 
    Descripción:
        Requerimiento de proteínas metabolizables para mantenimiento (g/día)

    Parametros:
        
        consummo_materia_seca       = consumo total de materia seca kg/dia ( TotalDMFed )
        total_nutrientes_digestibles= TDN en g/dia
        peso_vivo                   = peso vivo en kg
        dias_gestacion              = numero de dias degestacion (para calcular peso del utero gravido)
        peso_cria_al_nacer          = peso en kg de cria (para calcular peso del utero gravido)


    """
    if sin_peso_cria:
        peso_cria_al_nacer = calcular_peso_cria_al_nacer( peso_vivo )

    peso_utero_gravido = calcular_peso_utero_gravido( dias_gestacion , peso_cria_al_nacer )

    requerimiento_urinario          = calcular_requerimiento_urinario(peso_vivo , peso_utero_gravido)
    requerimiento_dermico           = calcular_requerimiento_dermico(peso_vivo , dias_gestacion)
    requerimiento_proteína_fecal    = calcular_requerimiento_proteína_fecal(consumo_materia_seca , total_nutrientes_digestibles )
    requerimiento_proteina_endogena = calcular_requerimiento_proteina_endogena( consumo_materia_seca ) 

    return requerimiento_urinario + requerimiento_dermico +requerimiento_proteína_fecal + requerimiento_proteina_endogena



###### vrequerimiento proteina v######

def calcular_requerimiento_urinario(peso_vivo , peso_utero_gravido):
    """
    Descripción:
        la funcion calcula el requerimiento de proteina por perdida urinaria

    Parametros:
        peso_vivo           = peso vivo del animal en kg  ( BW ) en el modelo del NRC 
        peso_utero_gravido  = peso del utero en crecimiento "CW" en el modelo del NRC
    
        retorna:
            requerimiento_urinario 
    """
    return 4.1 * (peso_vivo - peso_utero_gravido)**0.5



####### requerimiento proteina dermica ##########

def calcular_requerimiento_dermico(peso_vivo , dias_gestacion):
    """
    Descripción:
        la funcion calcula el requerimiento de proteina por la perdida de problemas dermicos del animal

    Parametros:
        peso_vivo               = peso vivo del animal en kg  ( BW ) en el modelo del NRC
        dias_gestacion          = dias en gestacion  
        x peso_utero_gravido    = peso del utero en crecimiento "CW" en el modelo del NRC
    
    retorna:
        requerimiento_dermico 
    """
    peso_cria_al_nacer = calcular_peso_cria_al_nacer(peso_vivo)
    peso_utero_gravido = calcular_peso_utero_gravido(dias_gestacion , peso_cria_al_nacer)
    print(peso_utero_gravido)
    return 0.3 * (peso_vivo - peso_utero_gravido)**0.6



#### Requerimiento de proteína fecal metabólical ####

def calcular_requerimiento_proteína_fecal(consummo_materia_seca , total_nutrientes_digestibles=None ,proteina_metabolizable_microbial=None , proteina_cruda_microbiana=None  ):
    """
    Descripción:
        calcula el requerimiento total de proteina fecal usando la Materia seca consumida y el TDN
    
    Parametros:
        consumo_materia_seca                    = materia seca consumida en kg/dia
        total_nutrientes_digestibles (opcional) = TDN en g/dia
        proteina_metabolizable_microbial        = 
    """
    proteina_cruda_microbiana           = calcular_proteina_cruda_microbiana( total_nutrientes_digestibles )
    proteina_metabolizable_microbial    = calcular_proteina_metabolizable_microbial( proteina_cruda_microbiana )
    
    return consummo_materia_seca * 1000 * 0.03 -0.5 * ((proteina_metabolizable_microbial/0.8) - proteina_metabolizable_microbial) 


# MPBact
def calcular_proteina_metabolizable_microbial( proteina_cruda_microbiana ):
    """
    Descripcion:
        "MPBact"
        El concepto de proteína metabolizable se refiere a la proteína verdadera absorbida como aminoácidos a nivel intestinal 
        y que es suplida por la proteína microbial.

        Se asume que la proteína microbial contiene 80% de proteína verdadera y que 80% de esa proteína verdadera es 
        digerida en el intestino delgado, de ahí el factor 0,64.
    
    Parametros:
        total_proteina_cruda_microbiana = "MCP_Total" en g/día es la cantidad total de proteína microbiana producida en 
                                                        el rumen de un animal en un día determinado.
    retorna:
        proteina_metabolizable_microbial (en g/día)
    """
    return 0.64 * proteina_cruda_microbiana

# 
def calcular_proteina_cruda_microbiana(total_nutrientes_digestibles):
    """
    Descripción:
        proteína microbiana sintetizada en el rumen a partir de sustratos fermentables presentes en la dieta del animal
    
    Parametros:
       nutrientes_digestibles_totales = TDN en g/dia

    Retorna:
        total_proteina_cruda_microbiana 
    """
    return 0.13 * total_nutrientes_digestibles




##### Proteina metabolica requeridad para la proteina endogena   ###### 

# MPEndoReq
def calcular_requerimiento_proteina_endogena(consumo_materia_seca , proteina_endogena_metabolizable = None ):
    """
    Descripción:
        calcular la cantidad en gr/dia de proteína dietética necesaria para suministrar la proteína endógena

    Parametros:
        consumo_materia_seca = materia seca en kg/dia " TotalDMFed "
        proteina_endogena_metabolizable = en g/dia " MPEndo "

    Return:
        proteina_endogena_requerida en g/dia
    """        
    proteina_endogena_cruda         = calcular_proteina_endogena_cruda( consumo_materia_seca )
    proteina_endogena_metabolizable = calcular_proteina_endogena_metabolizable( proteina_endogena_cruda )

    return proteina_endogena_metabolizable / 0.67

# MPEndo
def calcular_proteina_endogena_metabolizable( proteina_endogena_cruda ):
    return 0.4 * proteina_endogena_cruda

# EndCP
def calcular_proteina_endogena_cruda( consumo_materia_seca ):
    return 11.8 * consumo_materia_seca




####  Calculo para peso de la cria si no esta disponible el #####

# CBW
def calcular_peso_cria_al_nacer(peso_vivo):
    """
    descripcion:
        calcula el peso del ternero al nacer en base a peso de vaca
        se llama en el modelo del NRC "CBW"

    parametros:
        peso_vivo = peso de vaca adulta kg "BW"

    retorna:
        peso estimado de la cria al nacer en kg
    """
    return peso_vivo * 0.06275

def sin_peso_cria(peso_cria_al_nacer):
    return peso_cria_al_nacer == None

def con_peso_cria(peso_cria_al_nacer):
    return peso_cria_al_nacer != None




def calcular_peso_utero_gravido(dias_gestacion, peso_cria_al_nacer):
    """
    descripción:
        calcula el peso del utero en crecimiento "CW" en el modelo del NRC

    parametros:
        dias_gestacion : numero de dias de gestación
        peso_cria_al_nacer: peso del ternero al nacer
    """
    return (18 + ((dias_gestacion - 190) * 0.665)) * (peso_cria_al_nacer/ 45)