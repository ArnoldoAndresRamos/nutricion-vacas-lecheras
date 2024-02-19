from requerimientos.vaca_lactante.energia_mantencion import calcular_peso_cria_al_nacer

def calcular_energia_metabolizable_gestacion(dias_gestacion , peso_vivo):
    """
    la funcion estima los requisitos de energia los ultimos 100 dias de gestacion 
    dias_gestacion = entre 190 a 279
    peso_vivo      = peso vivo de vaca en gestación en kg
    """
    if dias_gestacion >190:
        return 0
    
    if dias_gestacion < 190 and dias_gestacion >279:
        peso_cria_al_nacer = calcular_peso_cria_al_nacer(peso_vivo)
        return 1
    