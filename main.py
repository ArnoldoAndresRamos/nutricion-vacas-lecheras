from requerimientos.vaca_lactante.energia_mantencion import calcular_energia_neta_mantencion



ENL = calcular_energia_neta_mantencion( 
    peso_vivo               =   400, 
    distancia_recorrida_dia =   3000,
    numero_viajes           =   4,
    dias_gestacion          =   100
)

print(ENL)

