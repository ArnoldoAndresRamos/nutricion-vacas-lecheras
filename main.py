from model_nrc_2001.tipo_animal.vaca_lactante.energia_mantencion import calcular_energia_neta_mantencion



ENL = calcular_energia_neta_mantencion( 
    peso_vivo               =    400 , 
    #distancia_recorrida_dia =   3000,
    #numero_viajes           =   4,
    #dias_gestacion          =   100
)



dias_gestacion  = 220
peso_vivo       = 800
peso_cria       = 44

print("ENL : ", ENL)


from model_nrc_2001.tipo_animal.novilla_reemplazo.energia_mantencion import calcular_energia_neta_mantencion_sin_estres as novilla_energia

ENL_nov = novilla_energia(400,20,200,44,3,True,False )
print(ENL_nov)