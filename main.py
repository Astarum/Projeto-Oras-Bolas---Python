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

#lista do tempo, bolaX e bolaY do arquivo
tempoFloat = funcoes.leitura_arquivos("bola_tempo.txt")
bolaX = funcoes.leitura_arquivos("bola_posX.txt")
bolaY = funcoes.leitura_arquivos("bola_posY.txt")


#todas listas utilizadas ao longo do codigo
#deslocamento
deslocamentoX = []
deslocamentoY= []
#posição do robo
roboX = []
roboY = []

#distancia robo->destino dele
distancia=[]

#todos angulos robo->destino
ang = []

#decomposição da aceleração do robo
aY_robo = []
aX_robo = []

#velocidades do robo (inicia parado)
velY_robo = [0]
velX_robo = [0]
velTotal_robo = [0]

#lista para guardar as informações que vão para os graficos
graficoTempo = []
grafico_bolaX = []
grafico_bolaY = []
grafico_velocidade_BolaX = []
grafico_velocidadeMedia_BolaY = []
grafico_aceleracao_BolaX = []
grafico_aceleracao_BolaY = []

#decomposição do raio de interceptação
raioX = []
raioY = []

#velocidades e aceleração da bola
velocidade_BolaX = []
velocidade_BolaY = []
aceleracao_BolaX = []
aceleracao_BolaY = []

#variável para bloquear os botoes se não há dados
existem_dados = False

#variável para os botoes da interface de proximo e anterior
interacao_entre_botoes = 0
#logica para os botoes de proximo e anterior
primeira_interacao_anterior = True
primeira_interacao_proximo = True
frearX = False
velocidade_recuo = 0
#inicializando as variáveis de posição inicial do robo
xI=0
yI=0

###Construção da interface

#titulo da interface
titulo = Label(janela,text="Digite a posição inicial do robo",font=("Arial",20))
titulo.place(relx=0.5,rely=0,anchor=NE)

#posição X do robo
posicao_X = Label(janela,text="Posição X:",font=("Arial",16))
posicao_X.place(relx=0.2,rely=0.1,anchor=NE)

#posição Y do robo
posicao_Y = Label(janela,text="Posição Y:",font=("Arial",16))
posicao_Y.place(relx=0.2,rely=0.15,anchor=NE)

#informações do movimento do robo e da bola até a interceptação
informacoes = Label(janela,text="Informações da trajetória do robô até a interceptação:",font=("Arial",16))
informacoes.place(relx=0.30,rely=0.35,anchor=CENTER)

#área onde será escrito as informações
txt = scrolledtext.ScrolledText(janela,width=90,height=15,font=("Arial Bold",13))
txt.place(relx=0.01,rely=0.4)


#função para o botao de inicio do algoritmo
def iniciar():
  #limpa a área de texto
  txt.delete(1.0,END)
  #todas variáveis globais que serão utilizadas
  global velocidade_recuo,frearY,frearX,velTotal_robo,xI,yI,velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_aceleracao_BolaY,grafico_velocidade_BolaX,grafico_velocidade_BolaY,bolaX,bolaY,tempoFloat,grafico_aceleracao_BolaY,grafico_aceleracao_BolaY,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,existem_dados,interacao_entre_botoes

  #aceleração do robo
  aceleracaoRobo = funcoes.const_aceleracao
  #todas as listas anteriores
  deslocamentoX = []  
  deslocamentoY= []
  roboX = []
  roboY = []
  distancia=[]
  ang = []
  aY_robo = []
  aX_robo = []
  velY_robo = [0]
  velX_robo = [0]
  velTotal_robo = [0]
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
  
  #variáveis para coletar o que foi escrito nos campo X e Y
  coord_X = posicao_X.get()
  coord_Y = posicao_Y.get()

  #variáveis para fazer o controle dos caracteres digitados
  conta_X = 0
  conta_Y = 0
  liberado = False

  #variável que bloqueia accesso aos botoes
  existem_dados = False

  #interação entre os botoes
  interacao_entre_botoes = 0
  primeira_interacao_anterior = True
  primeira_interacao_proximo = True

  #variável para o freio do robo
  frearX = False
  frearY = False
 

  #verifica se existe ponto no número
  for c in coord_X:
    if c == ".":
      conta_X+=1
  for c in coord_Y:
    if c == ".":
      conta_Y+=1 
  #verifica sem apenas 1 ponto nos números       
  if conta_X ==1:    
    coord_X = coord_X.replace(".","")
  if conta_Y ==1:    
    coord_Y = coord_Y.replace(".","")
  #verifica se após substituir os pontos por nada, se existem apenas números   
  if coord_X.isnumeric() == False:
    messagebox.showerror("Error","Coordenada X deve conter apenas números!")
  if coord_Y.isnumeric() == False:
    messagebox.showerror("Error","Coordenada Y deve conter apenas números!")  

  #se sim, prossegue o programa
  if coord_X.isnumeric() and coord_Y.isnumeric():
    #atribui os valores ao x inicial e ao y inicial
    global xI
    global yI
    xI = float(posicao_X.get())
    yI = float(posicao_Y.get())
    
    #se os valores estiverem entre 0 e 9 para o x, e 0 e 6 para o y, ele executa o codigo
    if xI>=0 and xI<=9 and yI>=0 and yI<=6:
      liberado = True
    else:
      messagebox.showerror("Error","Os valores de X e Y devem estar entre 0 e 9 e 0 e 6, respectivamente.")   
 

    if liberado == True:

      #atribui as posições iniciais ao deslocamento inicial, e a posição inicial do robo  
      deslocamentoX = [xI]
      deslocamentoY= [yI]
      roboX = [xI]
      roboY = [yI]
      
      #atribui todos os valores das velocidades e acelerações da bola para as 4 listas
      velocidade_BolaX,velocidade_BolaY,aceleracao_BolaX,aceleracao_BolaY = funcoes.calculo_velocidade_aceleracao_Bola(tempoFloat)

      #loop até o momento de interceptação
      for i in range(len(tempoFloat)):

        #calcula o angulo durante a trajetoria da bola ;ponto 1 = instante atual; ponto 2 = proximo instante
        anguloBola = funcoes.angulo(bolaX[i+1],bolaY[i+1],bolaX[i],bolaY[i])

        #calcula qual seria a posição do robo baseando-se nesse angulo
        destinoX = bolaX[i] + funcoes.const_raio*math.cos(math.radians(anguloBola))
        destinoY = bolaY[i] + funcoes.const_raio*math.sin(math.radians(anguloBola))

        
        #calcula o angulo entre essa posição destino e o robo
        ang.append(funcoes.angulo(destinoX,destinoY,roboX[i],roboY[i]))  
        #calcula a velocidade e a aceleração
        funcoes.velocidade_aceleracao_Robo(velTotal_robo,velX_robo,velY_robo,aX_robo,aY_robo,aceleracaoRobo,ang[i],i,0.02)
        
        #decompoe o raio de interceptação em X e Y
        funcoes.decomposicao_RaioInterceptacao(ang[i],i,raioX,raioY,funcoes.const_raio)

        #adiciona os valores da velocidade e aceleração da bola as listas dos graficos
        grafico_velocidade_BolaX.append(velocidade_BolaX[i])
        grafico_velocidade_BolaY.append(velocidade_BolaY[i])
        grafico_aceleracao_BolaX.append(aceleracao_BolaX[i])
        grafico_aceleracao_BolaY.append(aceleracao_BolaY[i])




        #listas para o grafico
        graficoTempo.insert(i,tempoFloat[i])
        grafico_bolaX.insert(i,bolaX[i])
        grafico_bolaY.insert(i,bolaY[i])


        #verifica se a  proxima velocidade do robo é iguala velocidade máxima do robo, se sim, a aceleração passa a ser 0
        if velTotal_robo[i+1] == funcoes.vel_max:
          aceleracaoRobo = 0 
        else:
          aceleracaoRobo = 1.5   
        aux2X = funcoes.deslocamento_RoboX(deslocamentoX[i],aX_robo[i],velX_robo[i],funcoes.const_variacao_tempo)
        aux2Y = funcoes.deslocamento_RoboY(deslocamentoY[i],aY_robo[i],velY_robo[i],funcoes.const_variacao_tempo)
      
        #verifica se o raio inicial é maior q 0, se sim, significa que o robo está indo de baixo para cima, logo
        #o ponto de parada em Y será quando o valor do robo for maior ou igual, ao da bola em Y - o raio em Y
        if (raioY[0] > 0 and aux2Y >= destinoY):
          aux2Y = destinoY
        #mesma coisa quando o robo estiver indo de cima para baixo, nesse caso ele verifica se a posição é menor ou igual
        # a posição da bola em Y + o raio em Y  
        elif (raioY[0] < 0 and aux2Y <= destinoY ):
          aux2Y = destinoY 

        #em X acontece a mesma coisa, verifica se o robo está indo da esquerda para a direita, e nesse caso, o ponto de parada será
        # a posição da bola em X - o raio em X    
        if (raioX[0] > 0 and aux2X >= destinoX ):
          aux2X = destinoX 
        #verifica se o robo está indo da direita para a esquerda e aqui, 
        # a parada será  quando a posição dele for menor ou igual a da bola em X + o raio em X  
        elif (raioX[0] < 0 and aux2X <= destinoX ):
          aux2X = destinoX

        

        #atribui movimento ao robo
        deslocamentoX.insert(i+1,aux2X)
        deslocamentoY.insert(i+1,aux2Y)
        roboX.insert(i+1,aux2X)
        roboY.insert(i+1,aux2Y) 
        #calcula a distancia entre o robo e a  após o movimento do robo
        distancia.append(funcoes.dist(bolaX[i],bolaY[i],roboX[i+1],roboY[i+1]))
        
        #supondo que o robo mantenha a velocidade atual, quanto tempo demoraria para ele frear
        tempo_freio = ((velTotal_robo[i+1]-funcoes.vel_alvo))/1.5
        
        

        #supondo que o robo mantenha a velocidade atual e q a bola esteja parada, quanto tempo demorará para ele chegar no destino
        estimativaX = (destinoX-deslocamentoX[i])/velX_robo[i+1]
        estimativaY = (destinoY-deslocamentoY[i])/velY_robo[i+1]

        #se o tempo da estimativa for menor ou igual ao do freio, ele começa a frear  
        if estimativaX <= tempo_freio:
          frearX = True

        #inverte a direção da aceleração
        if frearX == True:
          aceleracaoRobo=1.5
          aceleracaoRobo*=-1
        #corrige os valores da velocidade para quando ele atinge a velocidade desejada
        if velTotal_robo[i+1]<= funcoes.vel_alvo:
          velTotal_robo[i+1] = funcoes.vel_alvo
          velX_robo[i+1] = velTotal_robo[i+1]*math.cos(math.radians(ang[i]))
          velY_robo[i+1] = velTotal_robo[i+1]*math.sin(math.radians(ang[i]))
        
       
        if (distancia[i] <= funcoes.const_raio+(funcoes.const_raio*0.1)):
          #o primeiro elemento das listas para retirar a folga
          velX_robo.pop(0)
          velY_robo.pop(0)
          velTotal_robo.pop(0)
          roboX.pop(0)
          roboY.pop(0)
          deslocamentoX.pop(0)
          deslocamentoY.pop(0)

          #escreve na interface gráfica
          txt.insert(END,("Enconstou na bola na posição: X: %f, Y: %f\n" % (aux2X, aux2Y)))
          txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
          txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
          txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
          txt.insert(END,("\nVelocidades do robô:"))
          txt.insert(END,("\nvelocidadeX: %f,velocidadeY %f\n"% (velX_robo[i], velY_robo[i])))
          txt.insert(END,("\nvelocidade total: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
          #guarda qual foi o ultimo elemento das listas
          ultimo_elemento = i

          #troca o valor da variavel de bloqueio
          existem_dados = True

          #velocidade de recuo da bola após a interceptação, como os vetores são exatamente opostos, subtrai o módulo das duas
          #nesse caso, a maior (velocidade do robo) - a menor (velocidade da bola)
          #a direção será a direção da maior para o restante dos calculos
          velocidade_recuo =  math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)) - math.sqrt(math.pow(velocidade_BolaX[i],2)+math.pow(velocidade_BolaY[i],2))
          break
         
        #deleta os campos de escrita da interface   
        posicao_X.delete(0,END)
        posicao_Y.delete(0,END)
#gera os graficos        
def graficos():
  global velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX

  #verifica se há dadosg
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados")
  else: 
    #gera o grafico da distancia 
    funcoes.gerar_graficoDistancia(graficoTempo, distancia)

    #gera o grafico da posição da bola e do robo em um plano XY
    funcoes.gera_graficoPosicaoXY(grafico_bolaX,grafico_bolaY,roboX,roboY)  
    #gera o grafico da posição dos dois em função do tempo 
    funcoes.gera_graficoPosicaoTempo(grafico_bolaX,grafico_bolaY,roboX,roboY, graficoTempo)  

    #gera um grafico da velocidade do robo em função do tempo
    funcoes.gera_graficoVelocidadeRobo(velX_robo, velY_robo, graficoTempo) 

    #gera um grafico da aceleração do robo em função do tempo
    funcoes.gera_graficoAceleracaoRobo(aX_robo, aY_robo, graficoTempo)

    #gera um grafico da aceleracao da bola em função do tempo
    funcoes.gera_graficoAceleracaoBola(grafico_aceleracao_BolaX, grafico_aceleracao_BolaY, graficoTempo)

    #grafico da velocidade da bola em função do tempo
    funcoes.gera_graficoVelocidadeBola(grafico_velocidade_BolaX, grafico_velocidade_BolaY, graficoTempo) 

    #grafico da velocidade do robo e da bola em função do tempo
    funcoes.gera_grafico_Velocidade_RoboBola(velX_robo,velY_robo,grafico_velocidade_BolaX,grafico_velocidade_BolaY,graficoTempo)

    #grafico da aceleração da bola e do robo em função do tempo
    funcoes.gera_grafico_Aceleracao_RoboBola(aX_robo,aY_robo,grafico_aceleracao_BolaX,grafico_aceleracao_BolaY,graficoTempo)          
  
#função para o botao de inicio
def inicio():
  global xI,yI,velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,interacao_entre_botoes
  #limpa a área de escrita
  txt.delete(1.0,END)
  i = 0
  #inicia no dado com indice 0
  if existem_dados == True:
    txt.insert(END,("A bola está em (%.3f,%.3f)\n"% (bolaX[i],bolaY[i])))
    txt.insert(END,("\nO robo está em (%.3f,%.3f)\n"% (xI,yI)))
    txt.insert(END,("\nO angulo do vetor posição atual é %.2f\n"% ang[i]))
    txt.insert(END,("\nInstante atual de tempo: %.2f\n"% tempoFloat[i]))
    txt.insert(END,("\nraioX: %f, raioY %f\n"% (raioX[i], raioY[i])))
    txt.insert(END,("\nraio total: %f\n"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2)))))
    txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX_robo[i], aY_robo[i])))

    #troca o valor das variaveis de bloqueio
    primeira_interacao_anterior = False
    primeira_interacao_proximo = False
    #atribui o valor do indice atual para a variável de interação entre botoes
    interacao_entre_botoes = i
  else:
    messagebox.showerror("Error","Não há dados")   

#função que mostra o ultimo dado  
def ultimo():
  global velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,primeira_interacao_anterior,primeira_interacao_proximo,interacao_entre_botoes
  txt.delete(1.0,END)
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados") 
  else:  
    #aqui o indice é o ultimo elemento registrado
    i = ultimo_elemento
    txt.insert(END,("Posição do robo na interceptação: X: %f, Y: %f\n" % (roboX[i],roboY[i])))
    txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
    txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
    txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
    txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
    #troca o valor das variáveis de bloqueio
    primeira_interacao_anterior = True
    primeira_interacao_proximo = True
    interacao_entre_botoes = i
  
#função do botao de anterior
def anterior():
  global velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,interacao_entre_botoes,primeira_interacao_anterior,primeira_interacao_proximo
  txt.delete(1.0,END)
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados") 
  
  else:  
    #bloco para caso seja o ultimo elemento
    if primeira_interacao_anterior == True and primeira_interacao_proximo == True:
      i = ultimo_elemento
      #troca o valor da variável
      primeira_interacao_anterior = False
      primeira_interacao_proximo = False
    else:
      i = interacao_entre_botoes  
    #retorna 1 indice  
    i-=1
    

    if i == 0:
      txt.insert(END,("Posição do robo na interceptação: X: %f, Y: %f\n" % (roboX[i],roboY[i])))
      txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
      txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
      txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
      #txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
      interacao_entre_botoes = i
    #bloqueia abaixo do primeiro dado
    elif i<0:
      messagebox.showerror("Error","Não há dados")
      interacao_entre_botoes = 0
    else:
        #se for qualquer indice acima do 0
        txt.insert(END,("A bola está em (%.2f,%.2f)"% (bolaX[i],bolaY[i])))
        txt.insert(END,("\nO robo está em (%.2f,%.2f)\n"% (deslocamentoX[i-1],deslocamentoY[i-1])))
        txt.insert(END,("\nO angulo do vetor posição atual é %.2f\n"% ang[i]))
        txt.insert(END,("\nInstante atual de tempo: %.2f\n"% tempoFloat[i]))
        txt.insert(END,("\nraioX: %f, raioY %f\n"% (raioX[i], raioY[i])))
        txt.insert(END,("\nraio total: %f\n"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2)))))
        txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX_robo[i], aY_robo[i])))
        txt.insert(END,("\n---------------------------------------------"))  
        txt.insert(END,("\nO robo se moveu para (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i])))
        txt.insert(END,("\nVelocidade após o movimento: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
        interacao_entre_botoes = i

#função do botao de proximo faz o contrario da função do anterior
def proximo():
  global velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_velocidade_BolaY,grafico_velocidade_BolaX,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,interacao_entre_botoes,primeira_interacao_proximo,primeira_interacao_anterior
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
      txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
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
        txt.insert(END,("\naceleracaoX: %f, aceleracaoY %f"% (aX_robo[i], aY_robo[i])))
        txt.insert(END,("\n---------------------------------------------"))  
        txt.insert(END,("\nO robo se moveu para (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i])))
        txt.insert(END,("\nVelocidade no momento do contato: %f\n" % (math.sqrt(math.pow(velX_robo[i],2)+math.pow(velY_robo[i],2)))))
        interacao_entre_botoes = i
           
   
def javascript():
  global velocidade_recuo,frearX,velTotal_robo,velX_robo,velY_robo,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX_robo, aY_robo,grafico_aceleracao_BolaX, grafico_aceleracao_BolaY,grafico_velocidade_BolaX,grafico_velocidade_BolaY,bolaX,bolaY,tempoFloat,grafico_aceleracao_BolaY,grafico_aceleracao_BolaY,ultimo_elemento,deslocamentoX,deslocamentoY,ang,raioX,raioY,existem_dados,primeira_interacao_anterior,primeira_interacao_proximo,existem_dados,interacao_entre_botoes
  if existem_dados == False:
    messagebox.showerror("Error","Não há dados")
  else:  
    #indice do ultimo elemento
    i = ultimo_elemento

    #novas listas para a nova trajetoria
    novo_angulo = []
    novo_roboX = []
    novo_roboY = []
    aX_movimentando_bola = []
    aY_movimentando_bola = []
    #atribui todos valores iniciais das listas, se necessário
    pos_bolaX = [bolaX[i]]
    pos_bolaY = [bolaY[i]]
    nova_vel_X = [velX_robo[i]]
    nova_vel_Y = [velY_robo[i]]
    nova_velTotal = [math.sqrt(math.pow(nova_vel_X[0],2)+math.pow(nova_vel_Y[0],2))]

    
    novo_roboX.append(roboX[i])
    novo_roboY.append(roboY[i])
    novo_angulo.append(funcoes.angulo(pos_bolaX[0],pos_bolaY[0],novo_roboX[0],novo_roboY[0]))
    bola_vel_recuoX = [velocidade_recuo*math.cos(math.radians(novo_angulo[0]))]
    bola_vel_recuoY = [velocidade_recuo*math.sin(math.radians(novo_angulo[0]))]
    bola_desaleracaoX = math.cos(math.radians(novo_angulo[0]))*funcoes.const_modulo_bola*-1
    bola_desaleracaoY = math.sin(math.radians(novo_angulo[0]))*funcoes.const_modulo_bola*-1
    
    aceleracaoRobo = funcoes.const_aceleracao
    #referencia de condução da bola é a posição 1 e 3 do campo
    ang_referencia = funcoes.angulo_referencia(1,3,bolaX[i],bolaY[i])
    diferenca =  math.fabs(novo_angulo[0]-ang_referencia)

    

    #sentido de rotação do robo
    horario = False
    #verifica se o angulo atual é maior q o de referencia, e se a diferença entre eles é menor ou igual a 180
    #se sim horario é mais rapido
    if novo_angulo[0]>ang_referencia and diferenca <=180:
      horario = True
    #verifica se o angulo atual é menor que o angulo de referencia, e se a diferença entre eles é maior ou igual a 180
    elif novo_angulo[0]<ang_referencia and diferenca >=180:
      horario = True

    
    j = 0
    #verifica se ja chegou no fim
    fim = False
    #verifica se deu uma volta 360
    volta = False
    #sentido anti horario
    antiHora = False


    #verifica se o angulo atual é menor que o de referencia, e se não é horario  
    if novo_angulo[0]<ang_referencia and horario == False:
      antiHora = True  


    bola_desaleracaoX = math.cos(math.radians(novo_angulo[0]))*funcoes.const_modulo_bola*-1
    bola_desaleracaoY = math.sin(math.radians(novo_angulo[0]))*funcoes.const_modulo_bola*-1
    ###TRAJETORIA APOS A INTERCEPTAÇAO, ROTACIONA AO REDOR DA BOLA
    #enquanto não chegar no fim  
    while fim == False:

      #incrementa nos angulos  
      if horario == True:
        calculo = novo_angulo[j]-5
      else:
        #ou decremenda
        calculo = novo_angulo[j]+5
        
        #verifica se deu uma volta
        if calculo>=360:
          volta = True
          #reseta o valor
          calculo -=360 
      #verifica se chegou no valor    
      if calculo<= ang_referencia and horario == True:
        calculo = ang_referencia
        fim = True
      elif calculo >=ang_referencia and volta == True:
        calculo = ang_referencia
        fim = True  
      elif calculo >=ang_referencia and antiHora == True:
        calculo = ang_referencia
        fim = True   
      #adiciona a lista de angulos    
      novo_angulo.insert(j+1,calculo)
  
      #velocidade constante nesse momento
      #a = 0
      aX_movimentando_bola.append(0)
      aY_movimentando_bola.append(0)

      #adiciona o movimento de recuo na bola
      bola_vel_recuoX.append(bola_vel_recuoX[j]+bola_desaleracaoX*funcoes.const_variacao_tempo)
      bola_vel_recuoY.append(bola_vel_recuoY[j]+bola_desaleracaoY*funcoes.const_variacao_tempo)
      pos_bolaX.append(funcoes.deslocamento_RoboX(pos_bolaX[j],bola_desaleracaoX,bola_vel_recuoX[j],funcoes.const_variacao_tempo))
      pos_bolaY.append(funcoes.deslocamento_RoboX(pos_bolaY[j],bola_desaleracaoY,bola_vel_recuoY[j],funcoes.const_variacao_tempo))

      ang_final = math.radians(novo_angulo[j+1])

      #calcula o deslocamento do robo (velocidade é constante)
      distancia_finalX = -funcoes.const_raio* math.cos(ang_final)+pos_bolaX[j]
      distancia_finalY = -funcoes.const_raio*math.sin(ang_final)+pos_bolaY[j]
      nova_vel_X.append((distancia_finalX-novo_roboX[j])/0.02)
      nova_vel_Y.append((distancia_finalY-novo_roboY[j])/0.02)

      #adiciona os valores nas de velocidade
      nova_velTotal.append((math.sqrt(math.pow(nova_vel_X[j+1],2)+math.pow(nova_vel_Y[j+1],2))))
      novo_roboX.insert(j+1,distancia_finalX)
      novo_roboY.insert(j+1,distancia_finalY)


      
    
      
      if fim == True:
        pass
      j+=1
    



    chegou = False
    chegouX = False
    chegouY = False
    frearX = False
    ang_referencia = funcoes.angulo_referencia(1,3,pos_bolaX[-1],pos_bolaY[-1])
    
    ##TRAJETORIA - CONDUZ A BOLA

    while chegou == False:
      funcoes.velocidade_aceleracao_Robo(nova_velTotal,nova_vel_X,nova_vel_Y,aX_movimentando_bola,aY_movimentando_bola,aceleracaoRobo,novo_angulo[-1],j,0.02)
      aux2X = funcoes.deslocamento_RoboX(novo_roboX[j],aX_movimentando_bola[j],nova_vel_X[j],funcoes.const_variacao_tempo)
      aux2Y = funcoes.deslocamento_RoboY(novo_roboY[j],aY_movimentando_bola[j],nova_vel_Y[j],funcoes.const_variacao_tempo)
      novo_angulo.append(ang_referencia)
      aX_movimentando_bola.append(10)
      aY_movimentando_bola.append(10)
      #print(novo_angulo[j])
      auxiliar = math.radians(novo_angulo[-1])
      bola_vel_recuoX.append(nova_vel_X[j+1]*0.8)
      bola_vel_recuoY.append(nova_vel_Y[j+1]*0.8)
      

      calculo_posicao_bolaX = funcoes.const_raio* math.cos(auxiliar)+aux2X
      calculo_posicao_bolaY = funcoes.const_raio*math.sin(auxiliar)+aux2Y

      
      
      
        
    
        #corrige os valores da velocidade caso seja menor q a minima
      if nova_velTotal[j+1]<= funcoes.vel_alvo:
        nova_velTotal[j+1] = funcoes.vel_alvo
        nova_vel_X[j+1] = nova_velTotal[j+1]*math.cos(math.radians(novo_angulo[j]))
        nova_vel_Y[j+1] = nova_velTotal[j+1]*math.sin(math.radians(novo_angulo[j]))

      





      if calculo_posicao_bolaX <=1.5 :
        #calculo_posicao_bolaX = 2
        #aux2X = 2-funcoes.const_raio* math.cos(auxiliar)
        chegouX= True
      if calculo_posicao_bolaY>=2:
        #calculo_posicao_bolaY = 2
        chegouY = True
        #aux2Y = 3- funcoes.const_raio*math.sin(auxiliar)
      novo_roboX.insert(j+1,aux2X)
      novo_roboY.insert(j+1,aux2Y)

      pos_bolaX.insert(j+1,calculo_posicao_bolaX )
      pos_bolaY.insert(j+1,calculo_posicao_bolaY)

      
    
      
      
      if chegouX == True and chegouY == True:
        chegou = True
        break
      j+=1

    
    
    angulo_momentum = novo_angulo[-1]
    j = len(novo_roboX)-1
    ang_referencia_gol = funcoes.angulo_referencia(0,3,pos_bolaX[-1],pos_bolaY[-1])
    diferenca =  math.fabs(novo_angulo[-1]-ang_referencia_gol)
    if novo_angulo[-1]>ang_referencia_gol and diferenca <=angulo_momentum+180:
      horario = True
    elif novo_angulo[-1]<ang_referencia_gol and diferenca >=angulo_momentum+180:
      horario = True
    horario = False  
    fim = False
    volta = False
    antiHora = False
    calculo = 0
    if novo_angulo[-1]<ang_referencia_gol and horario == False:
      antiHora = True
    primeiro = True
  
    


    #TRAJETORIA - FAZ A VOLTA AO REDOR DA BOLA PARA SE PREPARAR PARA CHUTAR
    while fim == False:
      ##referencia = dentro do gol
      ang_referencia_gol = funcoes.angulo_referencia(0,3,pos_bolaX[j],pos_bolaY[j])
      

      #compara o vetor da bola para o gol, e o vetor do robo para a bola, quando o valor for 10 graus a mais, termina o loop

      if horario == True:

        calculo = novo_angulo[j]-3
      else:
        calculo = novo_angulo[j]+3
        if calculo>=360:
          volta = True
          calculo -=360 
      if calculo<= ang_referencia_gol-10 and horario == True:
        # calculo = ang_referencia_gol
        fim = True
      elif calculo >=ang_referencia_gol+10 and volta == True:
        # calculo = ang_referencia_gol
        fim = True    
      elif calculo >=ang_referencia_gol+10 and antiHora == True:
        # calculo = ang_referencia_gol
        fim = True   
      
      novo_angulo.insert(j+1,calculo)
      
      


      ##FAZ A TRAJETORIA -> velocidade constante variando apenas os graus
      ang_final = math.radians(novo_angulo[j+1])
      if primeiro == True:
        distancia_finalX = -funcoes.const_raio* math.cos(ang_final)+pos_bolaX[j]
      else:  
        distancia_finalX = (-funcoes.const_raio* math.cos(ang_final))+pos_bolaX[j]
      distancia_finalY = -funcoes.const_raio*math.sin(ang_final)+pos_bolaY[j]
      nova_vel_X.append((distancia_finalX-novo_roboX[j])/0.02)
      nova_vel_Y.append((distancia_finalY-novo_roboY[j])/0.02)
      #distancia_bola = math.sqrt((math.pow((bolaX[i] - novo_roboX[j]),2) + math.pow((bolaY[i] - novo_roboY[j]),2)))
      nova_velTotal.append((math.sqrt(math.pow(nova_vel_X[j],2)+math.pow(nova_vel_Y[j],2))))
      novo_roboX.insert(j+1,distancia_finalX)
      novo_roboY.insert(j+1,distancia_finalY)

      #a bola continua a se mover com a velocidade de recuo, já que não esta mais sendo guiada pelo robo
      bola_vel_recuoX.append(bola_vel_recuoX[j]+bola_desaleracaoX*funcoes.const_variacao_tempo)
      bola_vel_recuoY.append(bola_vel_recuoY[j]+bola_desaleracaoY*funcoes.const_variacao_tempo)
      pos_bolaX.append(funcoes.deslocamento_RoboX(pos_bolaX[j],bola_desaleracaoX,bola_vel_recuoX[j],funcoes.const_variacao_tempo))
      pos_bolaY.append(funcoes.deslocamento_RoboX(pos_bolaY[j],bola_desaleracaoY,bola_vel_recuoY[j],funcoes.const_variacao_tempo))

      aX_movimentando_bola.append(aX_movimentando_bola[-1])
      aY_movimentando_bola.append(aY_movimentando_bola[-1])
      
      angulus = funcoes.angulo(pos_bolaX[j],pos_bolaY[j],novo_roboX[j],novo_roboY[j])  
      
      primeiro = False
      j+=1

    
    
    #loop que faz o recuo do robo levando em conta uma posição destino acima da bola, com distancia de 1 m a 60 graus

    #quanto mais aumenta o conta no while, maior é o recuo
    conta = 2
    #print(novo_roboX)
    while conta <5:
      anguloBola = 60
      destinoX = pos_bolaX[j] + 1*math.cos(math.radians(anguloBola))

      destinoY =pos_bolaY[j] +1*math.sin(math.radians(anguloBola))

      direc = funcoes.angulo(destinoX,destinoY,novo_roboX[j],novo_roboY[j])


      funcoes.velocidade_aceleracao_Robo(nova_velTotal,nova_vel_X,nova_vel_Y,aX_movimentando_bola,aY_movimentando_bola,aceleracaoRobo,direc,j,0.02)
      aux2X = funcoes.deslocamento_RoboX(novo_roboX[j],aX_movimentando_bola[j],nova_vel_X[j],funcoes.const_variacao_tempo)
      aux2Y = funcoes.deslocamento_RoboY(novo_roboY[j],aY_movimentando_bola[j],nova_vel_Y[j],funcoes.const_variacao_tempo)
      
      
      bola_vel_recuoX.append(bola_vel_recuoX[j]+bola_desaleracaoX*funcoes.const_variacao_tempo)
      bola_vel_recuoY.append(bola_vel_recuoY[j]+bola_desaleracaoY*funcoes.const_variacao_tempo)
      pos_bolaX.append(funcoes.deslocamento_RoboX(pos_bolaX[j],bola_desaleracaoX,bola_vel_recuoX[j],funcoes.const_variacao_tempo))
      pos_bolaY.append(funcoes.deslocamento_RoboX(pos_bolaY[j],bola_desaleracaoY,bola_vel_recuoY[j],funcoes.const_variacao_tempo))

      novo_roboX.insert(j+1,aux2X)  
      novo_roboY.insert(j+1,aux2Y)
      novo_angulo.append(direc)

      
      conta+=1 
      j+=1

    
      
    
    chute = False
    chuteX = False
    chuteY = False
    

    #realiza o movimento de aproximação até a bola para chutar
    while chute == False:
      #angulo de referencia dentro do gol, com y valendo 5
      angulus = funcoes.angulo(0,5,novo_roboX[j],novo_roboY[j])
      angulus_a = funcoes.angulo(pos_bolaX[j],pos_bolaY[j],novo_roboX[j],novo_roboY[j])
      


      
      funcoes.velocidade_aceleracao_Robo(nova_velTotal,nova_vel_X,nova_vel_Y,aX_movimentando_bola,aY_movimentando_bola,aceleracaoRobo,angulus_a,j,0.02)
      aux2X = funcoes.deslocamento_RoboX(novo_roboX[j],aX_movimentando_bola[j],nova_vel_X[j],funcoes.const_variacao_tempo)
      aux2Y = funcoes.deslocamento_RoboY(novo_roboY[j],aY_movimentando_bola[j],nova_vel_Y[j],funcoes.const_variacao_tempo)
      auxiliar = math.radians(angulus_a)
      
    

      calculo_posicao_bolaX = -funcoes.const_raio* math.cos(auxiliar)+aux2X
      calculo_posicao_bolaY = funcoes.const_raio*math.sin(auxiliar)+aux2Y
      pos_bolaX.append(funcoes.deslocamento_RoboX(pos_bolaX[j],-0.015,bola_vel_recuoX[j],funcoes.const_variacao_tempo)) 
      bola_vel_recuoX.append(bola_vel_recuoX[j]-0.015*funcoes.const_variacao_tempo)
      pos_bolaY.append(funcoes.deslocamento_RoboX(pos_bolaY[j],-0.016,bola_vel_recuoY[j],funcoes.const_variacao_tempo))
      bola_vel_recuoY.append(bola_vel_recuoY[j]-0.016*funcoes.const_variacao_tempo) 
      
      ang_final = auxiliar
      if aux2Y <= -funcoes.const_raio*math.sin(ang_final)+pos_bolaY[j]:
        aux2Y = -funcoes.const_raio*math.sin(ang_final)+pos_bolaY[j]
        chuteY = True
        
        
        
      if aux2X <= -funcoes.const_raio* math.cos(ang_final)+pos_bolaX[j]:
        aux2X = -funcoes.const_raio* math.cos(ang_final)+pos_bolaX[j]   
        chuteX = True

        
      

      
        
      
        
        
      novo_roboX.append(aux2X)  
      novo_roboY.append(aux2Y)
      novo_angulo.append(angulus)

      
      if chuteX and chuteY:
        chute = True
      j+=1  
  
    gol = False

  
    

    velocidadeX = (nova_vel_X[-1]+bola_vel_recuoX[-1])
    velocidadeY = (nova_vel_Y[-1]+bola_vel_recuoY[-1])
    direcao = funcoes.angulo2(nova_vel_X[j] ,nova_vel_Y[j] ,bola_vel_recuoX[j] ,bola_vel_recuoY[j])
    modulo_velocidade = math.sqrt(math.pow(velocidadeX,2)+math.pow(velocidadeY,2))

    aceleracaoRobo*=-1
    while gol == False:
      funcoes.velocidade_aceleracao_Robo(nova_velTotal,nova_vel_X,nova_vel_Y,aX_movimentando_bola,aY_movimentando_bola,aceleracaoRobo,180,j,0.02)
      
      if(nova_velTotal[j+1]<=0):
        nova_velTotal[j+1] = 0
        nova_vel_X[j+1] = 0
        nova_vel_Y[j+1] = 0
        aceleracaoRobo = 0
      aux2X = funcoes.deslocamento_RoboX(novo_roboX[j],aX_movimentando_bola[j],nova_vel_X[j],funcoes.const_variacao_tempo)
      aux2Y = funcoes.deslocamento_RoboY(novo_roboY[j],aY_movimentando_bola[j],nova_vel_Y[j],funcoes.const_variacao_tempo)
      

      bola_vel_recuoX.append(velocidadeX+0.015*funcoes.const_variacao_tempo)
      bola_vel_recuoY.append(velocidadeY+0.016*funcoes.const_variacao_tempo)
      pos_bolaX.append(funcoes.deslocamento_RoboX(pos_bolaX[j],+0.015,bola_vel_recuoX[j],funcoes.const_variacao_tempo))
      pos_bolaY.append(funcoes.deslocamento_RoboX(pos_bolaY[j],+0.016,bola_vel_recuoY[j],funcoes.const_variacao_tempo))
      novo_roboX.append(aux2X)  
      novo_roboY.append(aux2Y)
      
      
      novo_angulo.append(novo_angulo[-1])

      if pos_bolaX[j+1] <= 0:
        gol = True
      j+=1

      

    

  #aux2X = 3-funcoes.const_raio* math.cos(auxiliar)
    arquivo = open("instrucoes-javascript.txt","w")
    for m in range(len(roboX)):
      
      arquivo.write("%2.2f %2.2f %2.2f %2.2f %2.2f %2.2f\n"% (tempoFloat[m],bolaX[m],bolaY[m],roboX[m],roboY[m],ang[m]))


    for l in range(len(novo_roboX)):
      arquivo.write("%2.2f %2.2f %2.2f %2.2f %2.2f %2.2f\n"% (tempoFloat[i+l],pos_bolaX[l],pos_bolaY[l],novo_roboX[l],novo_roboY[l],novo_angulo[l]))
      #arquivo.write(f"{tempoFloat[i+l]}.2f {pos_bolaX[l]} {pos_bolaY[l]} {novo_roboX[l]} {novo_roboY[l]} {novo_angulo[l]}\n")
    
    arquivo.close()

      


          



#botao de pesquisar
bot_iniciar = Button(janela,text="Iniciar",font=("Arial",16),command=iniciar)
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


