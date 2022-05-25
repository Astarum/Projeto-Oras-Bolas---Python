import io
import math
import matplotlib.pyplot

#constantes
const_velMax = 2.8
const_raio = 0.3
PI_ = 3.14159265358979323
vel_max = 2.3


def leitura_arquivos(nome_arquivo):
  arquivo = open(nome_arquivo,"r")
  lista = arquivo.readlines()
  arquivo.close()
  lista_dados = []
  for linha in lista:
    dado = linha.strip()
    lista_dados.append(float(dado))
  return lista_dados


#função que calcula a distância 1ponto = robo, 2ponto = bola
def dist(bolaX, distancia, bolaY, roboX,roboY, i):
  #print(f"{bolaY}")
  auxiliarX = (bolaX[i] - roboX[i+1])
  auxiliarY = (bolaY[i] - roboY[i+1])
  
  aux = math.sqrt((math.pow(auxiliarX,2) + math.pow(auxiliarY,2)))
  distancia.insert(i,aux)



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
def angulo(ang, bolaX, bolaY, roboX,roboY, i):
  global PI_     
  #oposto = eixo y      
  oposto = (bolaY[i] - roboY[i])
  #adjacente = eixo x
  adjacente = (bolaX[i] - roboX[i])
  
  #evitar que faça divisão com denominador 0
  if (adjacente != 0):

    #calcula o arcotangente e já converte em graus
    auxiliar = (math.atan(oposto / adjacente)) * 180 / PI_
  else:
    #caso o adjacente seja 0, verifica se o Y da bola é menor que o Y do robo
    if (bolaY[i] < roboY[i]):
      #se sim, o vetor tem que ter direção de 270 graus (para baixo)
      auxiliar = 270
    else:
      #se não, o vetor será virado para cima, com 90 graus
      auxiliar = 90
  
  #tratar caso o Y da bola seja igual ao Y do robo
  if (oposto == 0):
    #verifica se o X da bola é maior que o X do robo
    if (bolaX[i]>roboX[i]):
      #se sim, significa que a direção do vetor será 360, ou seja, para a direita
      auxiliar = 360
    else:
      #se não, a direção sera 180 graus, para a esquerda
      auxiliar = 180    
  #insere o valor em uma lista chamada ang
  ang.insert(i,auxiliar)

#função quadrante para fazer correções no angulo
def quadrante(bolaX,bolaY,roboX,roboY,i,ang):
  #se o X da bola for menor que o X do robo
  if (bolaX<roboX):
    #se o Y da bola for diferente do Y do robo, adiciona 180 graus ao angulo
    if (bolaY<roboY or bolaY>roboY):
      ang[i] += 180
  #se o X da bola for maior que o X do robo e o Y da bola for menor que o Y do robo, o vetor está no quarto quadrante
  # logo adiciona 360
  elif(bolaX>roboX and bolaY<roboY):
    ang[i]+=360
  

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
def deslocamento_RoboX(deslX, acelX,velocidadeX, i,tempo): 
    #*auxiliarX = deslX[i] + velocidadeX * tempo + 0.5 * acelX * tempo;
    #*auxiliarY = deslY[i] + velocidadeY * tempo + 0.5 * acelY * tempo;
    auxiliarX = deslX[i] + velocidadeX * tempo + 0.5 * acelX * tempo
    return auxiliarX
#calcula o deslocamento em Y 
def deslocamento_RoboY(deslY,acelY, velocidadeY, i,tempo): 
    #*auxiliarX = deslX[i] + velocidadeX * tempo + 0.5 * acelX * tempo;
    #*auxiliarY = deslY[i] + velocidadeY * tempo + 0.5 * acelY * tempo;
    
    auxiliarY = deslY[i] + velocidadeY * tempo + 0.5 * acelY * tempo
    return auxiliarY
#movimento uniforme    
# def deslocamento_uniforme_roboX(deslX,velocidadeX,i,tempo):
#   return deslX[i] + velocidadeX * tempo
# def deslocamento_uniforme_roboY(deslY,velocidadeY,i,tempo):
#   return deslY[i] + velocidadeY * tempo  

    
#funções para os graficos    
def gerar_graficoDistancia(grafico_tempo, grafico_distancia):
  #distancia do robo e da bola.
  matplotlib.pyplot.title('Distancia entre o robo e a bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Distancia')
  matplotlib.pyplot.ylabel('TEMPO')

  matplotlib.pyplot.plot(grafico_distancia, grafico_tempo)

  matplotlib.pyplot.show()

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
  matplotlib.pyplot.title('trajetória do robo e da bola até o momento da interceptação \n em função do tempo')

  matplotlib.pyplot.xlabel('Azul = robo em x  Lar = robo em y  Verde = bola em x verm = bola em y')

#posição do robo
  matplotlib.pyplot.plot(grafico_roboX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_roboY, grafico_tempo)
#posição da bola
  matplotlib.pyplot.plot(grafico_bolaX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_bolaY, grafico_tempo)

  matplotlib.pyplot.show()

def gera_graficoPosicaoXY(grafico_bolaX,grafico_bolaY,grafico_roboX,grafico_roboY):
    #distancia do robo e da bola.
    matplotlib.pyplot.title('trajetória do robo e da bola até o momento da interceptação \n em um plano XY')

    matplotlib.pyplot.xlabel('Azul = robo, Laranja = bola')

  #posição do robo
    matplotlib.pyplot.plot(grafico_roboX, grafico_roboY)
  #posição da bola
    matplotlib.pyplot.plot(grafico_bolaX, grafico_bolaY)
    
    matplotlib.pyplot.xlim([0,9])
    matplotlib.pyplot.ylim([0,6])
    matplotlib.pyplot.show()    


def gera_graficoVelocidadeRobo(grafico_veloRoboX, grafico_veloRoboY, grafico_tempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade do robo em x  Laranja = velocidade do robo em y ')


  matplotlib.pyplot.plot(grafico_veloRoboX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_veloRoboY, grafico_tempo)
  matplotlib.pyplot.show()

def gera_graficoAceleracaoRobo(grafico_acelX, grafico_acelY, grafico_tempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração do robo em x  Laranja = aceleração do robo em y ')
  matplotlib.pyplot.plot(grafico_acelX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_acelY, grafico_tempo)

  matplotlib.pyplot.show()


def gera_graficoVelocidadeBola(grafico_velo_bolaX, grafico_velo_bolaY, grafico_tempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade da bola em x  Laranja = velocidade da bola em y ')


  matplotlib.pyplot.plot(grafico_velo_bolaX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_velo_bolaY, grafico_tempo)
  matplotlib.pyplot.show()

def gera_graficoAceleracaoBola(grafico_acel_bolaX, grafico_acel_bolaY, grafico_tempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração da bola em x  Laranja = aceleração da bola em y ')
  matplotlib.pyplot.plot(grafico_acel_bolaX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_acel_bolaY, grafico_tempo)

  matplotlib.pyplot.show()

def gera_grafico_Velocidade_RoboBola(grafico_veloRoboX, grafico_veloRoboY,grafico_velo_bolaX, grafico_velo_bolaY, grafico_tempo):
  matplotlib.pyplot.title('Velocidade do robo e da bola \n em função do tempo')

  matplotlib.pyplot.xlabel('Azul = robo_vx,  Lar = robo_vy, Verde = bola_vy verm = bola_vy')

  #posição do robo
  matplotlib.pyplot.plot(grafico_veloRoboX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_veloRoboY, grafico_tempo)
  
  #posição da bola
  matplotlib.pyplot.plot(grafico_velo_bolaX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_velo_bolaY, grafico_tempo)
 

  matplotlib.pyplot.show()    

def gera_grafico_Aceleracao_RoboBola(grafico_acelX, grafico_acelY,grafico_acel_bolaX, grafico_acel_bolaY, grafico_tempo):
  matplotlib.pyplot.title('Aceleracao e velocidade do robo e da bola \n em função do tempo')

  matplotlib.pyplot.xlabel('Azul = robo_ax,  Lar = robo_ay, Verde = bola_ax verm = bola_ay')

  #posição do robo
 
  matplotlib.pyplot.plot(grafico_acelX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_acelY, grafico_tempo)
  #posição da bola
  
  matplotlib.pyplot.plot(grafico_acel_bolaX, grafico_tempo)
  matplotlib.pyplot.plot(grafico_acel_bolaY, grafico_tempo)

  matplotlib.pyplot.show()        


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

