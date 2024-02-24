from requerimientos.vaca_lactante.energia_mantencion import calcular_energia_neta_mantencion
from requerimientos.vaca_lactante.energia_gestacion import calcular_energia_metabolizable_gestacion, calcular_energia_neta_lactancia_gestacion
from requerimientos.novilla_reemplazo.energia_mantencion import calcular_energia_neta_mantencion_sin_estres_novilla_reemplazo

peso_vivo                   = 400,
temperatura_previa          = 20,
dias_gestacion              = 220,
grado_condicion_corporal_5  = 3,
pastoreo                    = True,
relieve_irregular           = True,
peso_cria_al_nacer          = 30,
    


def requerimientos_para_novilla_de_reemplazo():
    print(peso_vivo)
    
    energia_neta_mantencion = calcular_energia_neta_mantencion_sin_estres_novilla_reemplazo(
        peso_vivo,temperatura_previa,dias_gestacion,grado_condicion_corporal_5,pastoreo,relieve_irregular,peso_cria_al_nacer          = 30
    )
    proteina = 0

    return energia_neta_mantencion

def requerimientos_para_vaca_en_lactancia():
    calcular_energia_neta_mantencion( 
    peso_vivo               =   400 , 
    #distancia_recorrida_dia =   3000,
    #numero_viajes           =   4,
    #dias_gestacion          =   100
)
    
    return 0








# ejemplos

n=energia_neta_mantencion = calcular_energia_neta_mantencion_sin_estres_novilla_reemplazo(
        peso_vivo                   = 400,
        temperatura_previa          = 20,
        dias_gestacion              = 220,
        grado_condicion_corporal_5  = 3,
        pastoreo                    = True,
        relieve_irregular           = True,
        peso_cria_al_nacer          = 30
    )


ENL = calcular_energia_neta_mantencion( 
    peso_vivo               =   400 , 
    #distancia_recorrida_dia =   3000,
    #numero_viajes           =   4,
    #dias_gestacion          =   100
)



dias_gestacion  = 220
peso_vivo       = 800
peso_cria       = 44

EM_g    = calcular_energia_metabolizable_gestacion(dias_gestacion = 200,peso_cria_al_nacer=44)
ENl_g   = calcular_energia_neta_lactancia_gestacion(dias_gestacion , peso_cria)




print("EM_g: ", EM_g )
print("ENL_g: ",ENl_g )
print("ENL : ", ENL)


