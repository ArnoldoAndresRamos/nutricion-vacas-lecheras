from tipo_animal.novilla_reemplazo import energia_mantencion as novilla_reemplazo
from tipo_animal.novilla_reemplazo import proteina_mantencion as novilla_reemplazo_proteina
from tipo_animal.vaca_lactante import energia_mantencion as vaca_lactante

from tipo_animal.vaca_seca import proteina_mantencion as proteina_vaca_seca


peso_vivo                   = 400
temperatura_previa          = 20
dias_gestacion              = 220
grado_condicion_corporal_5  = 3
pastoreo                    = False
relieve_irregular           = True
peso_cria_al_nacer          = 30


def requerimientos_novilla_reemplazo( ):
   
    energia_mantencion = novilla_reemplazo.calcular_energia_neta_mantencion_sin_estres(

        peso_vivo, 
        temperatura_previa,   
        dias_gestacion,
        peso_cria_al_nacer, 
        grado_condicion_corporal_5, 
        pastoreo, 
        relieve_irregular        
    )

    proteina = 0
    energia_total = energia_mantencion
    return energia_total


energia_mantencion = novilla_reemplazo.calcular_energia_neta_mantencion_sin_estres(
    peso_vivo                   ,
    temperatura_previa          ,
    dias_gestacion              ,
    grado_condicion_corporal_5  ,
    pastoreo                    ,
    relieve_irregular           ,
    peso_cria_al_nacer               
    )


proteina_novilla = novilla_reemplazo_proteina.calcular_proteina_metabolizable_mantenimiento( 
        peso_vivo =540 ,consumo_materia_seca=18.8 ,total_nutrientes_digestibles= 10900 ,dias_gestacion= 75) 
#vaca_lactancia = vaca_lactante.calcular_energia_neta_mantencion(650,1232,5,200)
proteina_vaca_seca = proteina_vaca_seca.calcular_proteina_metabolizable_mantenimiento(18.8,10900,540,0)

print(proteina_novilla)
print(proteina_vaca_seca)