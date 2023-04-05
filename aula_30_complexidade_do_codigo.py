""""
CONSTANTE == VARIÁVEIS QUE NAO VAO MUDAR, SEMPRE SEU NOME SERÁ DIGITADO EM MAIÚSCULO
Muitas condições no mesmo if causa cofusões de leitura
Sempre realizar o codigo da melhor forma a entender o codigo
Quanto mais blocos de codigo dentro de blocos de codigo, mais complexo o codigo
EX:
a
    a
        a
            a
                a
Complexidade não é bom.
"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_excedida_carro = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
if velocidade_excedida_carro:
    print('Velocidade excedida no radar 1')
                                            #CONTRABARRA USADO PARA QUEBRA DE LINHA 
if carro_multado_radar_1 and velocidade_excedida_carro:
    print('Carro multado em radar 1')