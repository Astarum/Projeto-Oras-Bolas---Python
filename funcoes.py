import io
import math
import matplotlib.pyplot as plt

#constantes
const_raio = 0.33
const_aceleracao = 1.5
PI_ = 3.14159265358979323
vel_max = 2.3
const_pasta_graficos = "graficos/"
vel_alvo = 1
const_variacao_tempo = 0.02
const_modulo_bola = math.sqrt(math.pow(0.015,2)+math.pow(0.016,2))


#função para ler os arquivos e retornar já lista com os valores em números reais
def leitura_arquivos(nome_arquivo):
  arquivo = open(nome_arquivo,"r")
  lista = arquivo.readlines()
  arquivo.close()
  lista_dados = []
  for linha in lista:
    dado = linha.strip()
    lista_dados.append(float(dado))
  return lista_dados


#função que calcula a distância entre 2 pontos -> no caso ponto 1 = Robo; ponto 2 = Bola
def dist(bolaX, bolaY, roboX,roboY):
  auxiliarX = (bolaX - roboX)
  auxiliarY = (bolaY - roboY)
  
  aux = math.sqrt((math.pow(auxiliarX,2) + math.pow(auxiliarY,2)))
  return aux


#calculo de todas velocidades da bola, tanto em X como em Y
def calculo_velocidade_aceleracao_Bola(tempo):
    velocidade_X = []
    velocidade_Y = []
    aceleracao_X = []
    aceleracao_Y = []
    for i in range(len(tempo)):
      aceleracao_X.append(-0.015)
      aceleracao_Y.append(-0.016)
      velocidade_X.append(aceleracao_X[i]*tempo[i] +0.5)
      velocidade_Y.append(aceleracao_Y[i]*tempo[i] +0.4)
      

    return velocidade_X,velocidade_Y,aceleracao_X,aceleracao_Y

    



#função que calcula o angulo  
def angulo(bolaX, bolaY, roboX,roboY):
  global PI_     
  #oposto = eixo y      
  oposto = (bolaY - roboY)
  #adjacente = eixo x
  adjacente = (bolaX - roboX)
  
  #evitar que faça divisão com denominador 0
  if (adjacente != 0):

    #calcula o arcotangente e já converte em graus
    ang = (math.atan(oposto / adjacente)) * 180 / PI_
  else:
    #caso o adjacente seja 0, verifica se o Y da bola é menor que o Y do robo
    if (bolaY < roboY):
      #se sim, o vetor tem que ter direção de 270 graus (para baixo)
      ang = 270
    else:
      #se não, o vetor será virado para cima, com 90 graus
      ang = 90
  
  #tratar caso o Y da bola seja igual ao Y do robo
  if (oposto == 0):
    #verifica se o X da bola é maior que o X do robo
    if (bolaX>roboX):
      #se sim, significa que a direção do vetor será 360, ou seja, para a direita
      ang = 360
    else:
      #se não, a direção sera 180 graus, para a esquerda
      ang = 180    
  #insere o valor em uma lista chamada ang
    #se o X da bola for menor que o X do robo
  if (bolaX<roboX):
    #se o Y da bola for diferente do Y do robo, adiciona 180 graus ao angulo
    if (bolaY<roboY or bolaY>roboY):
      ang+= 180
  #se o X da bola for maior que o X do robo e o Y da bola for menor que o Y do robo, o vetor está no quarto quadrante
  # logo adiciona 360
  elif(bolaX>roboX and bolaY<roboY):
    ang+=360

  return ang

def angulo2(bolaX, bolaY, roboX,roboY):
  global PI_     
  #oposto = eixo y      
  oposto = (bolaY + roboY)
  #adjacente = eixo x
  adjacente = (bolaX + roboX)
  
  #evitar que faça divisão com denominador 0
  if (adjacente != 0):

    #calcula o arcotangente e já converte em graus
    ang = (math.atan(oposto / adjacente)) * 180 / PI_
  else:
    #caso o adjacente seja 0, verifica se o Y da bola é menor que o Y do robo
    if (bolaY < roboY):
      #se sim, o vetor tem que ter direção de 270 graus (para baixo)
      ang = 270
    else:
      #se não, o vetor será virado para cima, com 90 graus
      ang = 90
  
  #tratar caso o Y da bola seja igual ao Y do robo
  if (oposto == 0):
    #verifica se o X da bola é maior que o X do robo
    if (bolaX>roboX):
      #se sim, significa que a direção do vetor será 360, ou seja, para a direita
      ang = 360
    else:
      #se não, a direção sera 180 graus, para a esquerda
      ang = 180    
  #insere o valor em uma lista chamada ang
    #se o X da bola for menor que o X do robo
  if (bolaX<roboX):
    #se o Y da bola for diferente do Y do robo, adiciona 180 graus ao angulo
    if (bolaY<roboY or bolaY>roboY):
      ang+= 180
  #se o X da bola for maior que o X do robo e o Y da bola for menor que o Y do robo, o vetor está no quarto quadrante
  # logo adiciona 360
  elif(bolaX>roboX and bolaY<roboY):
    ang+=360

  return ang  

  

#função que calcula o raio de interceptação  
def decomposicao_RaioInterceptacao(angulo,i,raioX,raioY,raioTotal):
  #converte o angulo pra radianos
  angulo = angulo * PI_ / 180
  #insere os valores nas lista X e Y
  raioX.insert(i,(raioTotal * math.cos(angulo)))
  raioY.insert(i,(raioTotal * math.sin(angulo)))

#função que calcula a aceleração e a velocidade em X e Y
def velocidade_aceleracao_Robo(velTotal,velX, velY, aX, aY, a,angulo, i,tempo):
  global vel_max
  
  #converte o angulo pra radianos
  angulo = angulo * PI_ / 180
  #insere na lista da aceleração X o valor
  aX.insert(i,(a * math.cos(angulo)))
  #insere na lista da aceleração em Y o valor
  aY.insert(i,(a * math.sin(angulo)))
  calculo_prox_velX = (velTotal[i]*math.cos(angulo) + aX[i] * tempo)
  calculo_prox_velY = (velTotal[i]*math.sin(angulo) + aY[i] * tempo)
  calculo_velTotal = math.sqrt(math.pow(calculo_prox_velX,2)+math.pow(calculo_prox_velY,2))
  if calculo_velTotal>=vel_max:
    #insere na lista da velocidade em X o valor
    velX.insert(i+1,(vel_max*math.cos(angulo)))
    #insere na lista da velocidade em Y o valor 
    velY.insert(i+1,(vel_max*math.sin(angulo)))
    velTotal.insert(i+1,vel_max)
  else:
    #insere na lista da velocidade em X o valor
    velX.insert(i+1,(calculo_prox_velX))
    #insere na lista da velocidade em Y o valor 
    velY.insert(i+1,(calculo_prox_velY))
    velTotal.insert(i+1,calculo_velTotal) 

#função que calcula o deslocamento em X S = S0+v0t+0.5*at
def deslocamento_RoboX(deslX, acelX,velocidadeX, tempo): 
    #*auxiliarX = deslX[i] + velocidadeX * tempo + 0.5 * acelX * tempo;
    #*auxiliarY = deslY[i] + velocidadeY * tempo + 0.5 * acelY * tempo;
    auxiliarX = deslX + velocidadeX * tempo + 0.5 * acelX * math.pow(tempo,2)
    return auxiliarX
#calcula o deslocamento em Y 
def deslocamento_RoboY(deslY,acelY, velocidadeY, tempo): 
    #*auxiliarX = deslX[i] + velocidadeX * tempo + 0.5 * acelX * tempo;
    #*auxiliarY = deslY[i] + velocidadeY * tempo + 0.5 * acelY * tempo;
    
    auxiliarY = deslY + velocidadeY * tempo + 0.5 * acelY * math.pow(tempo,2)
    return auxiliarY




    
#funções para os graficos    
def gerar_graficoDistancia(grafico_tempo, grafico_distancia):
  #distancia do robo e da bola.
  plt.title('Distancia entre o robo e a bola até o momento da interceptação')
  plt.xlabel('Distancia (m)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_distancia,grafico_tempo,label="Distancia")
  
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoDistanciaTempo.png")
  plt.show()

# def gera_graficoPosicao(grafico_bolaX,grafico_bolaY,grafico_roboX,grafico_roboY):
#   # esse grafico marca o instante da interceptação, sobre o tempo 
#   matplotlib.pyplot.title('coordenadas do robo e da bola até o momento da interceptação')
#   matplotlib.pyplot.xlabel('Azul = Posição do robo Laranja = Posição da bola')
#   #posição em x.
#   matplotlib.pyplot.plot(grafico_roboX, grafico_roboY)
#   #posição em y.
#   matplotlib.pyplot.show()

def gera_graficoPosicaoTempo(grafico_bolaX,grafico_bolaY,grafico_roboX,grafico_roboY, grafico_tempo):
  #distancia do robo e da bola.
  plt.title('trajetória do robo e da bola até o momento da interceptação \n em função do tempo')
  
  plt.xlabel('Deslocamento (m)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_roboX,grafico_tempo,label="RoboX")
  ax.plot(grafico_roboY,grafico_tempo,label="RoboY")
  ax.plot(grafico_bolaX,grafico_tempo,label="BolaX")
  ax.plot(grafico_bolaY,grafico_tempo,label="BolaY")
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoPosicaoTempo.png")

  

  plt.show()

def gera_graficoPosicaoXY(grafico_bolaX,grafico_bolaY,grafico_roboX,grafico_roboY):
    #distancia do robo e da bola.
  plt.title('trajetória do robo e da bola até o momento da interceptação \n em um plano XY')

  plt.xlabel('Deslocamento (m)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_roboX,grafico_roboY,label="Robo")
  
  ax.plot(grafico_bolaX,grafico_bolaY,label="Bola")
 
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    
  plt.xlim([0,9])
  plt.ylim([0,6])
  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoPosicaoXY.png")
  plt.show()    


def gera_graficoVelocidadeRobo(grafico_veloRoboX, grafico_veloRoboY, grafico_tempo):
  #velocidade do robo.
  plt.title('velocidade do robo até o momento da interceptação')

  plt.xlabel('Velocidade (m/s)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_veloRoboX,grafico_tempo,label="Robo_vx")
  ax.plot(grafico_veloRoboY,grafico_tempo,label="Robo_vy")

  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoVelocidadeRobo.png")
  plt.show()

def gera_graficoAceleracaoRobo(grafico_acelX, grafico_acelY, grafico_tempo):
  #aceleração.
  plt.title('aceleração do robo até o momento da interceptação')

  plt.xlabel('Aceleração (m/s²)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_acelX,grafico_tempo,label="Robo_aX")
  ax.plot(grafico_acelY,grafico_tempo,label="Robo_aY")
  
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoAceleracaoRobo.png")

  plt.show()


def gera_graficoVelocidadeBola(grafico_velo_bolaX, grafico_velo_bolaY, grafico_tempo):
  #velocidade do robo.
  plt.title('velocidade da bola até o momento da interceptação')
  
  plt.xlabel('Velocidade (m/s)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  

  ax.plot(grafico_velo_bolaX,grafico_tempo,label="Bola_vx")
  ax.plot(grafico_velo_bolaY,grafico_tempo,label="Bola_vy")
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoVelocidadeBola.png")
  plt.show()

def gera_graficoAceleracaoBola(grafico_acel_bolaX, grafico_acel_bolaY, grafico_tempo):
  #aceleração.
  plt.title('aceleração da bola até o momento da interceptação')
  plt.xlabel('Aceleração (m/s²)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)

  ax.plot(grafico_acel_bolaX,grafico_tempo,label="Bola_aX")
  ax.plot(grafico_acel_bolaY,grafico_tempo,label="Bola_aY")
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoAceleracaoBola.png")
  plt.show()

def gera_grafico_Velocidade_RoboBola(grafico_veloRoboX, grafico_veloRoboY,grafico_velo_bolaX, grafico_velo_bolaY, grafico_tempo):
  plt.title('Velocidade do robo e da bola \n em função do tempo')
  plt.xlabel('Velocidade (m/s)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_veloRoboX,grafico_tempo,label="Robo_vx")
  ax.plot(grafico_veloRoboY,grafico_tempo,label="Robo_vy")
  ax.plot(grafico_velo_bolaX,grafico_tempo,label="Bola_vx")
  ax.plot(grafico_velo_bolaY,grafico_tempo,label="Bola_vy")
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoVelocidadeRoboBola.png")

  plt.show()    

def gera_grafico_Aceleracao_RoboBola(grafico_acelX, grafico_acelY,grafico_acel_bolaX, grafico_acel_bolaY, grafico_tempo):
  plt.title('Aceleracao e velocidade do robo e da bola \n em função do tempo')
  plt.xlabel('Aceleração (m/s²)')
  plt.ylabel('Tempo (s)')
  
  ax = plt.subplot(111)
  
  ax.plot(grafico_acelX,grafico_tempo,label="Robo_aX")
  ax.plot(grafico_acelY,grafico_tempo,label="Robo_aY")
  ax.plot(grafico_acel_bolaX,grafico_tempo,label="Bola_aX")
  ax.plot(grafico_acel_bolaY,grafico_tempo,label="Bola_aY")
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
  
  
  # Put a legend to the right of the current axis
  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

  plt.savefig(f"./ora bolas animacao/{const_pasta_graficos}/graficoAceleracaoRoboBola.png")
  plt.show()        


def angulo_referencia(bolaX, bolaY, roboX,roboY):
  global PI_     
  #oposto = eixo y      
  oposto = (bolaY - roboY)
  #adjacente = eixo x
  adjacente = (bolaX - roboX)
  
  #evitar que faça divisão com denominador 0
  if (adjacente != 0):

    #calcula o arcotangente e já converte em graus
    auxiliar = (math.atan(oposto / adjacente)) * 180 / PI_
  else:
    #caso o adjacente seja 0, verifica se o Y da bola é menor que o Y do robo
    if (bolaY < roboY):
      #se sim, o vetor tem que ter direção de 270 graus (para baixo)
      auxiliar = 270
    else:
      #se não, o vetor será virado para cima, com 90 graus
      auxiliar = 90
  
  #tratar caso o Y da bola seja igual ao Y do robo
  if (oposto == 0):
    #verifica se o X da bola é maior que o X do robo
    if (bolaX>roboX):
      #se sim, significa que a direção do vetor será 360, ou seja, para a direita
      auxiliar = 360
    else:
      #se não, a direção sera 180 graus, para a esquerda
      auxiliar = 180    
  #insere o valor em uma lista chamada ang
  ang = auxiliar
    #se o X da bola for menor que o X do robo
  if (bolaX<roboX):
    #se o Y da bola for diferente do Y do robo, adiciona 180 graus ao angulo
    if (bolaY<roboY or bolaY>roboY):
      ang += 180
  #se o X da bola for maior que o X do robo e o Y da bola for menor que o Y do robo, o vetor está no quarto quadrante
  # logo adiciona 360
  elif(bolaX>roboX and bolaY<roboY):
    ang=360
  return ang  
