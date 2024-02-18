from tipo_animal.vaca_lactante.requeriminetos_de_energia import  calcular_energia_neta_mantencion , calcular_energia_neta_mantencion_base


ENL = calcular_energia_neta_mantencion( 
    peso_vivo               =   400, 
    distancia_recorrida_dia =   3000,
    numero_viajes           =   4,
    dias_gestacion          =   100,

    )
ENL_base = calcular_energia_neta_mantencion_base(peso_vivo = 400)

print(ENL,ENL_base)


