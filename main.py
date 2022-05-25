from re import template
from tkinter import messagebox
import funcoes
import math
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext



#criação da interface grafica
janela = Tk()
janela.title("Projeto Ora Bolas")
janela.geometry("900x600")




#variáveis globais para a interface gráfica
tempoFloat = []
bolaX = []
bolaY = []

tempoFloat = funcoes.leitura_arquivos("bola_tempo.txt")
bolaX = funcoes.leitura_arquivos("bola_posX.txt")
bolaY = funcoes.leitura_arquivos("bola_posY.txt")


deslocamentoX = []
deslocamentoY= []
roboX = []
roboY = []
distancia=[]
ang = []
aY = []
aX = []
velY = [0]
velX = [0]
velTotal = [0]
graficoTempo = []
grafico_bolaX = []
grafico_bolaY = []
raioX = []
raioY = []
velocidade_BolaX = []
velocidade_BolaY = []
aceleracao_BolaX = []
aceleracao_BolaY = []
grafico_velocidade_BolaX = []
grafico_velocidadeMedia_BolaY = []
grafico_aceleracao_BolaX = []
grafico_aceleracao_BolaY = []
existem_dados = False
interacao_entre_botoes = 0
primeira_interacao_anterior = True
primeira_interacao_proximo = True

xI=0
yI=0
#palavra suspeita parte escrita
titulo = Label(janela,text="Digite a posição inicial do robo",font=("Arial",20))
titulo.place(relx=0.5,rely=0,anchor=NE)
posicao_X = Label(janela,text="Posição X:",font=("Arial",16))
posicao_X.place(relx=0.2,rely=0.1,anchor=NE)
#frequencia parte escrita
posicao_Y = Label(janela,text="Posição Y:",font=("Arial",16))
posicao_Y.place(relx=0.2,rely=0.15,anchor=NE)
#ocorrencias parte escrita
ocorrencias = Label(janela,text="Informações do momento de interceptação:",font=("Arial",16))
ocorrencias.place(relx=0.30,rely=0.35,anchor=CENTER)
#area de rolagem
txt = scrolledtext.ScrolledText(janela,width=90,height=15,font=("Arial Bold",13))
txt.place(relx=0.01,rely=0.4)
def pesquisar():
  txt.delete(1.0,END)
  global xI,yI,velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_aceleracao_BolaY,grafico_velocidade_BolaX,grafico_velocidade_BolaY,bolaX,bolaY,tempoFloat,grafico_aceleracao_BolaY,grafico_aceleracao_BolaY,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,existem_dados,interacao_entre_botoes

  aceleracaoRobo = 1.5
  deslocamentoX = []  
  deslocamentoY= []
  roboX = []
  roboY = []
  distancia=[]
  ang = []
  aY = []
  aX = []
  velY = [0]
  velX = [0]
  velTotal = [0]
  graficoTempo = []
  grafico_bolaX = []
  grafico_bolaY = []
  raioX = []
  raioY = []
  velocidade_BolaX = []
  velocidade_BolaY = []
  aceleracao_BolaX = []
  aceleracao_BolaY = []
  grafico_velocidade_BolaX = []
  grafico_velocidade_BolaY = []
  grafico_aceleracao_BolaX = []
  grafico_aceleracao_BolaY = []
  coord_X = posicao_X.get()
  coord_Y = posicao_Y.get()
  conta_X = 0
  conta_Y = 0
  liberado = False
  existem_dados = False
  interacao_entre_botoes = 0
  primeira_interacao_anterior = True
  primeira_interacao_proximo = True

  for c in coord_X:
    if c == ".":
      conta_X+=1
  for c in coord_Y:
    if c == ".":
      conta_Y+=1    
  if conta_X ==1:    
    coord_X = coord_X.replace(".","")
  if conta_Y ==1:    
    coord_Y = coord_Y.replace(".","")
     
  if coord_X.isnumeric() == False:
    messagebox.showerror("Error","Coordenada X deve conter apenas números!")
  if coord_Y.isnumeric() == False:
    messagebox.showerror("Error","Coordenada Y deve conter apenas números!")  
  if coord_X.isnumeric() and coord_Y.isnumeric():
    global xI
    global yI
    xI = float(posicao_X.get())
    yI = float(posicao_Y.get())
    if xI>=0 and xI<=9 and yI>=0 and yI<=6:
      liberado = True
    else:
      messagebox.showerror("Error","Os valores de X e Y devem estar entre 0 e 9 e 0 e 6, respectivamente.")   
  #apaga todos campos de digitação

    if liberado == True:

      deslocamentoX = [xI]
      deslocamentoY= [yI]
      roboX = [xI]
      roboY = [yI]
      

      velocidade_BolaX,velocidade_BolaY,aceleracao_BolaX,aceleracao_BolaY = funcoes.calculo_velocidade_aceleracao_Bola(tempoFloat)

      #loop até o momento de interceptação
      for i in range(len(tempoFloat)):
        #calcula o angulo
        funcoes.angulo(ang,bolaX,bolaY,roboX,roboY,i)  
        #corrige se necessario
        funcoes.quadrante(bolaX[i],bolaY[i],roboX[i],roboY[i],i,ang)
        #calcula a velocidade e a aceleração
        funcoes.velocidade_aceleracao_Robo(velTotal,velX,velY,aX,aY,aceleracaoRobo,ang[i],i,0.02)
        
        #decompoe o raio de interceptação
        funcoes.decomposicao_RaioInterceptacao(ang[i],i,raioX,raioY,funcoes.const_raio)
        grafico_velocidade_BolaX.append(velocidade_BolaX[i])
        grafico_velocidade_BolaY.append(velocidade_BolaY[i])
        grafico_aceleracao_BolaX.append(aceleracao_BolaX[i])
        grafico_aceleracao_BolaY.append(aceleracao_BolaY[i])




        #listas para o grafico
        graficoTempo.insert(i,tempoFloat[i])
        grafico_bolaX.insert(i,bolaX[i])
        grafico_bolaY.insert(i,bolaY[i])

        #variavel que guarda a "próxima" posição do robo
        if velTotal[i] == funcoes.vel_max:
          aceleracaoRobo = 0 
        else:
          aceleracaoRobo = 1.5   
        aux2X = funcoes.deslocamento_RoboX(deslocamentoX,aX[i],velX[i],i,0.02)
        aux2Y = funcoes.deslocamento_RoboY(deslocamentoY,aY[i],velY[i],i,0.02)
      
        #verifica se o raio inicial é maior q 0, se sim, significa que o robo está indo de baixo para cima, logo
        #o ponto de parada em Y será quando o valor do robo for maior ou igual, ao da bola em Y - o raio em Y
        if (raioY[0] > 0 and aux2Y >= bolaY[i] - raioY[i]):
          aux2Y = bolaY[i] - raioY[i]
        #mesma coisa quando o robo estiver indo de cima para baixo, nesse caso ele verifica se a posição é menor ou igual
        # a posição da bola em Y + o raio em Y  
        elif (raioY[0] < 0 and aux2Y <= bolaY[i] + math.fabs(raioY[i])):
          aux2Y = bolaY[i] + math.fabs(raioY[i])

        #em X acontece a mesma coisa, verifica se o robo está indo da esquerda para a direita, e nesse caso, o ponto de parada será
        # a posição da bola em X - o raio em X    
        if (raioX[0] > 0 and aux2X >= bolaX[i] - raioX[i]):
          aux2X = bolaX[i] - raioX[i]
        #verifica se o robo está indo da direita para a esquerda e aqui, 
        # a parada será  quando a posição dele for menor ou igual a da bola em X + o raio em X  
        elif (raioX[0] < 0 and aux2X <= bolaX[i] + math.fabs(raioX[i])):
          aux2X = bolaX[i] + math.fabs(raioX[i])

        # deslocamentoX.insert(i+1,aux2X)
        # deslocamentoY.insert(i+1,aux2Y)
        # roboX.insert(i+1,aux2X)
        # roboY.insert(i+1,aux2Y)
        

        #atribui movimento ao robo
        deslocamentoX.insert(i+1,aux2X)
        deslocamentoY.insert(i+1,aux2Y)
        roboX.insert(i+1,aux2X)
        roboY.insert(i+1,aux2Y) 
        #calcula a distancia entre o robo e a bola
        funcoes.dist(bolaX,distancia,bolaY,roboX,roboY,i) 
        if distancia[i] <= distancia[0]/5.15:
          aceleracaoRobo = 1.5
          aceleracaoRobo*=-1
        
      
        #imprime no terminal algumas informações relevantes    
        print("------------------------------------------")
        print("A bola está em (%.2f,%.2f)"% (bolaX[i],bolaY[i]))
        print("O robo está em (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i]))
        print("O robo deve ir para (%.2f,%.2f)"% (aux2X, aux2Y))
        print("O angulo do vetor posição atual é %.2f"% ang[i])
        print("Instante atual de tempo: %.2f"% tempoFloat[i])
        print("Quando o robo se mover, a distancia entre o robo e a bola será: %f"% distancia[i])
        print("raioX: %f, raioY %f"% (raioX[i], raioY[i]))
        print("raio total: %f"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2))))
        print("velocidadeX: %f,velocidadeY %f"% (velX[i], velY[i]))
        print("velocidade total: %f" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2))))
        #print("aux2x: %f,aux2Y %f\n"% (aux2X, aux2Y))
        print("aceleracaoX: %f, aceleracaoY %f"% (aX[i], aY[i]))
        print("aceleração total: %f"% (math.sqrt(math.pow(aX[i],2)+math.pow(aY[i],2))))

        print("------------------------------------------")
        print("O robo se moveu para: X: %.2f, Y: %.2f"% (aux2X,aux2Y))
        print("Com velocidade em X de: %f, e velocidade Y %f."%(velX[i+1],velY[i+1]))
        print("Com velocidade total: %f"%(velTotal[i+1]))
          #verifica se a distancia é menor ou igual ao raio de interceptação 
        if (distancia[i] <= funcoes.const_raio+(funcoes.const_raio*0.1)):
          #o primeiro elemento das listas para retirar a folga
          velX.pop(0)
          velY.pop(0)
          velTotal.pop(0)
          roboX.pop(0)
          roboY.pop(0)
          deslocamentoX.pop(0)
          deslocamentoY.pop(0)
          #escreve na interface gráfica
          txt.insert(END,("Enconstou na bola na posição: X: %f, Y: %f\n" % (aux2X, aux2Y)))
          txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
          txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
          txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
          txt.insert(END,("\nvelocidadeX: %f,velocidadeY %f\n"% (velX[i], velY[i])))
          txt.insert(END,("\nvelocidade total: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
          ultimo_elemento = i
          existem_dados = True
          break
          # #gera os graficos

        posicao_X.delete(0,END)
        posicao_Y.delete(0,END)
#gera os graficos        
def graficos():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX

  funcoes.gerar_graficoDistancia(graficoTempo, distancia)

  funcoes.gera_graficoPosicaoXY(grafico_bolaX,grafico_bolaY,roboX,roboY)   
  funcoes.gera_graficoPosicaoTempo(grafico_bolaX,grafico_bolaY,roboX,roboY, graficoTempo)  

  funcoes.gera_graficoVelocidadeRobo(velX, velY, graficoTempo) 
  funcoes.gera_graficoAceleracaoRobo(aX, aY, graficoTempo)
  funcoes.gera_graficoAceleracaoBola(grafico_aceleracao_BolaX, grafico_aceleracao_BolaY, graficoTempo)
  funcoes.gera_graficoVelocidadeBola(grafico_velocidade_BolaX, grafico_velocidade_BolaY, graficoTempo) 
  funcoes.gera_grafico_Velocidade_RoboBola(velX,velY,grafico_velocidade_BolaX,grafico_velocidade_BolaY,graficoTempo)
  funcoes.gera_grafico_Aceleracao_RoboBola(aX,aY,grafico_aceleracao_BolaX,grafico_aceleracao_BolaY,graficoTempo)          
  
def inicio():
  global xI,yI,velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,interacao_entre_botoes
  txt.delete(1.0,END)
  i = 0
  
  if existem_dados == True:
    txt.insert(END,("A bola está em (%.2f,%.2f)\n"% (bolaX[i],bolaY[i])))
    txt.insert(END,("\nO robo está em (%.2f,%.2f)\n"% (xI,yI)))
    txt.insert(END,("\nO angulo do vetor posição atual é %.2f\n"% ang[i]))
    txt.insert(END,("\nInstante atual de tempo: %.2f\n"% tempoFloat[i]))
    txt.insert(END,("\nraioX: %f, raioY %f\n"% (raioX[i], raioY[i])))
    txt.insert(END,("\nraio total: %f\n"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2)))))
    txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX[i], aY[i])))
    primeira_interacao_anterior = False
    primeira_interacao_proximo = False
    interacao_entre_botoes = i
  else:
    messagebox.showerror("Error","Não há dados")   
  
def ultimo():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,primeira_interacao_anterior,primeira_interacao_proximo,interacao_entre_botoes
  txt.delete(1.0,END)
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados") 
  else:  
    i = ultimo_elemento
    txt.insert(END,("Posição do robo na interceptação: X: %f, Y: %f\n" % (roboX[i],roboY[i])))
    txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
    txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
    txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
    txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
    primeira_interacao_anterior = True
    primeira_interacao_proximo = True
    interacao_entre_botoes = i
  
    
  # print("O robo se moveu para: X: %.2f, Y: %.2f"% (deslocamentoX[i]))
  # print("Com velocidade em X de: %f, e velocidade Y %f."%(velX[i],velY[i]))
  # print("Com velocidade total: %f"%(velTotal[i]))

def anterior():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,interacao_entre_botoes,primeira_interacao_anterior,primeira_interacao_proximo
  txt.delete(1.0,END)
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados") 
  
  else:  
    if primeira_interacao_anterior == True and primeira_interacao_proximo == True:
      i = ultimo_elemento
      primeira_interacao_anterior = False
      primeira_interacao_proximo = False
    else:
      i = interacao_entre_botoes  
    i-=1
    
    if i == 0:
      txt.insert(END,("Posição do robo na interceptação: X: %f, Y: %f\n" % (roboX[i],roboY[i])))
      txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
      txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
      txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
      txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
      interacao_entre_botoes = i
    elif i<0:
      messagebox.showerror("Error","Não há dados")
      interacao_entre_botoes = 0
    else:
        txt.insert(END,("A bola está em (%.2f,%.2f)"% (bolaX[i],bolaY[i])))
        txt.insert(END,("\nO robo está em (%.2f,%.2f)\n"% (deslocamentoX[i-1],deslocamentoY[i-1])))
        txt.insert(END,("\nO angulo do vetor posição atual é %.2f\n"% ang[i]))
        txt.insert(END,("\nInstante atual de tempo: %.2f\n"% tempoFloat[i]))
        txt.insert(END,("\nraioX: %f, raioY %f\n"% (raioX[i], raioY[i])))
        txt.insert(END,("\nraio total: %f\n"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2)))))
        txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX[i], aY[i])))
        txt.insert(END,("\n---------------------------------------------"))  
        txt.insert(END,("\nO robo se moveu para (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i])))
        txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
        interacao_entre_botoes = i

def proximo():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,interacao_entre_botoes,primeira_interacao_proximo,primeira_interacao_anterior
  txt.delete(1.0,END)
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados") 
  else:  
    if primeira_interacao_proximo == True and primeira_interacao_anterior == True:
      i = ultimo_elemento
      primeira_interacao_proximo = False
      primeira_interacao_anterior = False

    else:
      i = interacao_entre_botoes  
    i+=1
    if i == ultimo_elemento:
      txt.insert(END,("Posição do robo na interceptação: X: %f, Y: %f\n" % (roboX[i],roboY[i])))
      txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
      txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
      txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
      txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
      interacao_entre_botoes = i
    elif i>ultimo_elemento:
    
      messagebox.showerror("Error","Não há dados")
      interacao_entre_botoes = ultimo_elemento
    else:
        txt.insert(END,("A bola está em (%.2f,%.2f)"% (bolaX[i],bolaY[i])))
        txt.insert(END,("\nO robo está em (%.2f,%.2f)\n"% (deslocamentoX[i-1],deslocamentoY[i-1])))
        txt.insert(END,("\nO angulo do vetor posição atual é %.2f\n"% ang[i]))
        txt.insert(END,("\nInstante atual de tempo: %.2f\n"% tempoFloat[i]))
        txt.insert(END,("\nraioX: %f, raioY %f\n"% (raioX[i], raioY[i])))
        txt.insert(END,("\nraio total: %f\n"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2)))))
        txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX[i], aY[i])))
        txt.insert(END,("\n---------------------------------------------"))  
        txt.insert(END,("\nO robo se moveu para (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i])))
        txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
        interacao_entre_botoes = i
           
   
def javascript():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracao_BolaX, grafico_aceleracao_BolaY,grafico_velocidade_BolaX,grafico_velocidade_BolaY,bolaX,bolaY,tempoFloat,grafico_aceleracao_BolaY,grafico_aceleracao_BolaY,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,existem_dados,interacao_entre_botoes
  arquivo = open("instrucoes-javascript.txt","w")
  i = ultimo_elemento
  novo_angulo = []
  novo_roboX = []
  novo_roboY = []
  aX_movimentando_bola = []
  aY_movimentando_bola = []
  pos_bolaX = [bolaX[i]]
  pos_bolaY = [bolaY[i]]
  nova_vel_X = [velX[i]]
  nova_vel_Y = [velY[i]]
  nova_velTotal = [math.sqrt(math.pow(nova_vel_X[0],2)+math.pow(nova_vel_Y[0],2))]
  horario = False
  novo_angulo.append(ang[i])
  novo_roboX.append(roboX[i])
  novo_roboY.append(roboY[i])
  aceleracaoRobo = 1.5
  ang_referencia = funcoes.angulo_referencia(3,3,bolaX[i],bolaY[i])
  diferenca =  math.fabs(novo_angulo[0]-ang_referencia)
  if novo_angulo[0]>ang_referencia and diferenca <=180:
    horario = True
  elif novo_angulo[0]<ang_referencia and diferenca >=180:
    horario = True

  j = 0
  fim = False
  volta = False
  antiHora = False
  if novo_angulo[0]<ang_referencia and horario == False:
    antiHora = True
  while fim == False:

    if horario == True:
      calculo = novo_angulo[j]-10
    else:
      calculo = novo_angulo[j]+10
      if calculo>=360:
        volta = True
        calculo -=360 
    if calculo<= ang_referencia and horario == True:
      calculo = ang_referencia
      fim = True
    elif calculo >=ang_referencia and volta == True:
      calculo = ang_referencia
      fim = True  
    elif calculo >=ang_referencia and antiHora == True:
      calculo = ang_referencia
      fim = True     
    novo_angulo.insert(j+1,calculo)
 
    aX_movimentando_bola.append(0)
    aY_movimentando_bola.append(0)
    pos_bolaX.append(bolaX[i])
    pos_bolaY.append(bolaY[i])
    ang_final = math.radians(novo_angulo[j+1])
    distancia_finalX = -funcoes.const_raio* math.cos(ang_final)+bolaX[i]
    distancia_finalY = -funcoes.const_raio*math.sin(ang_final)+bolaY[i]
    nova_vel_X.append((distancia_finalX-novo_roboX[j])/0.02)
    nova_vel_Y.append((distancia_finalY-novo_roboY[j])/0.02)
    #distancia_bola = math.sqrt((math.pow((bolaX[i] - novo_roboX[j]),2) + math.pow((bolaY[i] - novo_roboY[j]),2)))
    nova_velTotal.append((math.sqrt(math.pow(nova_vel_X[j],2)+math.pow(nova_vel_Y[j],2))))
    novo_roboX.insert(j+1,distancia_finalX)
    novo_roboY.insert(j+1,distancia_finalY)
    print(tempoFloat[i+j])
    if fim == True:
      break
    j+=1
 
  
  j=len(nova_velTotal)-1
  #carregando a bola

  chegou = False
  chegouX = False
  chegouY = False
  
  
  while chegou == False:
    funcoes.velocidade_aceleracao_Robo(nova_velTotal,nova_vel_X,nova_vel_Y,aX_movimentando_bola,aY_movimentando_bola,aceleracaoRobo,novo_angulo[-1],j,0.02)
    aux2X = funcoes.deslocamento_RoboX(novo_roboX,aX_movimentando_bola[j],nova_vel_X[j],j,0.02)
    aux2Y = funcoes.deslocamento_RoboY(novo_roboY,aY_movimentando_bola[j],nova_vel_Y[j],j,0.02)
    novo_angulo.append(novo_angulo[-1])
    auxiliar = math.radians(novo_angulo[-1])

    calculo_posicao_bolaX = funcoes.const_raio* math.cos(auxiliar)+aux2X
    calculo_posicao_bolaY = funcoes.const_raio*math.sin(auxiliar)+aux2Y
    
    
    if calculo_posicao_bolaX >= 3:
      calculo_posicao_bolaX = 3
      aux2X = 3-funcoes.const_raio* math.cos(auxiliar)
      chegouX= True
    if calculo_posicao_bolaY>=3:
      calculo_posicao_bolaY = 3
      chegouY = True
      aux2Y = 3- funcoes.const_raio*math.sin(auxiliar)
    novo_roboX.insert(j+1,aux2X)
    novo_roboY.insert(j+1,aux2Y)

    pos_bolaX.insert(j+1,calculo_posicao_bolaX )
    pos_bolaY.insert(j+1,calculo_posicao_bolaY)

    auxiliarX = (calculo_posicao_bolaX - aux2X)
    auxiliarY = (calculo_posicao_bolaY - aux2Y)
  
    aux = math.sqrt((math.pow(auxiliarX,2) + math.pow(auxiliarY,2)))
    
    if chegouX == True and chegouY == True:
      chegou = True
      break
    j+=1

  #print(f" bolaX = {pos_bolaX[-1]}, bolaY = {pos_bolaY[-1]}  ")

 
  j = len(novo_roboX)-1
  ang_referencia_gol = funcoes.angulo_referencia(0,3,pos_bolaX[-1],pos_bolaY[-1])
  diferenca =  math.fabs(novo_angulo[-1]-ang_referencia_gol)
  if novo_angulo[-1]>ang_referencia_gol and diferenca <=180:
    horario = True
  elif novo_angulo[-1]<ang_referencia_gol and diferenca >=180:
    horario = True
  horario = False  
  fim = False
  volta = False
  antiHora = False
  calculo = 0
  if novo_angulo[-1]<ang_referencia_gol and horario == False:
    antiHora = True

  while fim == False:
    
    if horario == True:
      calculo = novo_angulo[j]-10
    else:
      calculo = novo_angulo[j]+10
      if calculo>=360:
        volta = True
        calculo -=360 
    if calculo<= ang_referencia_gol and horario == True:
      calculo = ang_referencia_gol
      fim = True
    elif calculo >=ang_referencia_gol and volta == True:
      calculo = ang_referencia_gol
      fim = True    
    elif calculo >=ang_referencia_gol and antiHora == True:
      calculo = ang_referencia_gol
      fim = True   
    
    novo_angulo.insert(j+1,calculo)
    
    ang_final = math.radians(novo_angulo[j+1])
    distancia_finalX = -funcoes.const_raio* math.cos(ang_final)+pos_bolaX[-1]
    distancia_finalY = -funcoes.const_raio*math.sin(ang_final)+pos_bolaY[-1]
    nova_vel_X.append((distancia_finalX-novo_roboX[j])/0.02)
    nova_vel_Y.append((distancia_finalY-novo_roboY[j])/0.02)
    #distancia_bola = math.sqrt((math.pow((bolaX[i] - novo_roboX[j]),2) + math.pow((bolaY[i] - novo_roboY[j]),2)))
    nova_velTotal.append((math.sqrt(math.pow(nova_vel_X[j],2)+math.pow(nova_vel_Y[j],2))))
    novo_roboX.insert(j+1,distancia_finalX)
    novo_roboY.insert(j+1,distancia_finalY)
    pos_bolaX.append(pos_bolaX[-1])
    pos_bolaY.append(pos_bolaY[-1])
    j+=1

  
  for m in range(len(roboX)):
    arquivo.write("%2.2f %2.2f %2.2f %2.2f %2.2f %2.2f\n"% (tempoFloat[m],bolaX[m],bolaY[m],roboX[m],roboY[m],ang[m]))


  for l in range(len(novo_roboX)):
    arquivo.write("%2.2f %2.2f %2.2f %2.2f %2.2f %2.2f\n"% (tempoFloat[i+l],pos_bolaX[l],pos_bolaY[l],novo_roboX[l],novo_roboY[l],novo_angulo[l]))
    #arquivo.write(f"{tempoFloat[i+l]}.2f {pos_bolaX[l]} {pos_bolaY[l]} {novo_roboX[l]} {novo_roboY[l]} {novo_angulo[l]}\n")
  
  arquivo.close()

      


          



#botao de pesquisar
bot_iniciar = Button(janela,text="Iniciar",font=("Arial",16),command=pesquisar)
bot_iniciar.place(relx=0.5,rely=0.1)
bot_gerarGraficos = Button(janela,text="Gerar gráficos",font=("Arial",16),command=graficos)
bot_gerarGraficos.place(relx=0.59,rely=0.1)
bot_gerarGraficos = Button(janela,text="Gerar arquivo .js",font=("Arial",16),command=javascript)
bot_gerarGraficos.place(relx=0.768,rely=0.1)

bot_anterior = Button(janela,text="<",font=("Arial",16),command=anterior)
bot_anterior.place(relx=0.44,rely=0.9)
bot_prox = Button(janela,text=">",font=("Arial",16),command=proximo)
bot_prox.place(relx=0.48,rely=0.9)
bot_inicial = Button(janela,text="Início",font=("Arial",16),command=inicio)
bot_inicial.place(relx=0.36,rely=0.9)
bot_ultimo = Button(janela,text="Último",font=("Arial",16),command=ultimo)
bot_ultimo.place(relx=0.52,rely=0.9)

#campo de entrada da palavra
posicao_X = Entry(janela,width=20,font=("Arial",16))
posicao_X.place(relx=0.2,rely=0.1)

#campo de entrada da frequencia
posicao_Y = Entry(janela,width=20,font=("Arial",16))
posicao_Y.place(relx=0.2,rely=0.15)


janela.mainloop()


