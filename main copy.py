from tkinter import messagebox
import funcoes
import math
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext



#criação da interface grafica
janela = Tk()
janela.title("Projeto Ora Bolas")
janela.geometry("900x500")

#variáveis globais para a interface gráfica
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
grafico_velocidadeMedia_BolaX = []
grafico_velocidadeMedia_BolaY = []
grafico_aceleracaoMedia_BolaX = []
grafico_aceleracaoMedia_BolaY = []


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
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracaoMedia_BolaX, grafico_aceleracaoMedia_BolaY,grafico_velocidadeMedia_BolaX
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
  grafico_velocidadeMedia_BolaX = []
  grafico_velocidadeMedia_BolaY = []
  grafico_aceleracaoMedia_BolaX = []
  grafico_aceleracaoMedia_BolaY = []
  coord_X = posicao_X.get()
  coord_Y = posicao_Y.get()
  conta_X = 0
  conta_Y = 0
  liberado = False
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
      tempoFloat = []
      bolaX = []
      bolaY = []

      tempoFloat = funcoes.leitura_arquivos("bola_tempo.txt")
      bolaX = funcoes.leitura_arquivos("bola_posX.txt")
      bolaY = funcoes.leitura_arquivos("bola_posY.txt")
            
      

      
      deslocamentoX = [xI]
      deslocamentoY= [yI]
      roboX = [xI]
      roboY = [yI]


      velocidade_BolaX,velocidade_BolaY,aceleracao_BolaX,aceleracao_BolaY = funcoes.calculo_velocidade_aceleracao_Bola(tempoFloat)

      executar = False
      #loop até o momento de interceptação
      for i in range(len(tempoFloat)):
        #calcula o angulo
        funcoes.angulo(ang,bolaX,bolaY,roboX,roboY,i)  
        #corrige se necessario
        funcoes.quadrante(bolaX[i],bolaY[i],roboX[i],roboY[i],i,ang)
        #calcula a velocidade e a aceleração
        funcoes.velocidade_aceleracao_Robo(velTotal,velX,velY,aX,aY,funcoes.a,ang[i],i,tempoFloat[i])
        #decompoe o raio de interceptação
        funcoes.decomposicao_RaioInterceptacao(ang[i],i,raioX,raioY,funcoes.const_raio)
        grafico_velocidadeMedia_BolaX.append(velocidade_BolaX[i])
        grafico_velocidadeMedia_BolaY.append(velocidade_BolaY[i])
        grafico_aceleracaoMedia_BolaX.append(aceleracao_BolaX[i])
        grafico_aceleracaoMedia_BolaY.append(aceleracao_BolaY[i])




        #listas para o grafico
        graficoTempo.insert(i,tempoFloat[i])
        grafico_bolaX.insert(i,bolaX[i])
        grafico_bolaY.insert(i,bolaY[i])

        #variavel que guarda a "próxima" posição do robo
        
        aux2X = funcoes.deslocamento_RoboX(deslocamentoX,aX[i],velX[i],i,tempoFloat[i])
        aux2Y = funcoes.deslocamento_RoboY(deslocamentoY,aY[i],velY[i],i,tempoFloat[i])
        
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
        
      
        #imprime no terminal algumas informações relevantes    
        # print("------------------------------------------")
        # print("A bola está em (%.2f,%.2f)"% (bolaX[i],bolaY[i]))
        # print("O robo está em (%.2f,%.2f)"% (deslocamentoX[i],deslocamentoY[i]))
        # print("O robo deve ir para (%.2f,%.2f)"% (aux2X, aux2Y))
        # print("O angulo do vetor posição atual é %.2f"% ang[i])
        # print("Instante atual de tempo: %.2f"% tempoFloat[i])
        # print("Quando o robo se mover, a distancia entre o robo e a bola será: %f"% distancia[i])
        # print("raioX: %f, raioY %f"% (raioX[i], raioY[i]))
        # print("raio total: %f"% (math.sqrt(math.pow(raioX[i],2)+math.pow(raioY[i],2))))
        # print("velocidadeX: %f,velocidadeY %f"% (velX[i], velY[i]))
        # print("velocidade total: %f" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2))))
        # #print("aux2x: %f,aux2Y %f\n"% (aux2X, aux2Y))
        # print("aceleracaoX: %f, aceleracaoY %f"% (aX[i], aY[i]))
        # print("aceleração total: %f"% (math.sqrt(math.pow(aX[i],2)+math.pow(aY[i],2))))

        # print("------------------------------------------")
        # print(f"O robo se moveu para: X: %.2f, Y: %.2f"% (aux2X,aux2Y))
          #verifica se a distancia é menor ou igual ao raio de interceptação 
        if (distancia[i] <= funcoes.const_raio+(funcoes.const_raio*0.1)):
          #remove o último elemento das listas de velocidade, já que a função sempre calcula a velocidade do próximo movimento
          velX.pop(-1)
          velY.pop(-1)
          velTotal.pop(-1)
          roboX.pop(0)
          roboY.pop(0)
          
          txt.insert(END,("Enconstou na bola na posição: X: %f, Y: %f\n" % (aux2X, aux2Y)))
          txt.insert(END,("\nPosição da bola: X: %f, Y: %f\n" % (bolaX[i],bolaY[i])))
          txt.insert(END,("\nInstante de tempo: %.2fs\n" % (tempoFloat[i])))
          txt.insert(END,("\nDistancia entre o robo e a bola: %f\n"% distancia[i]))
          txt.insert(END,("\nvelocidadeX: %f,velocidadeY %f\n"% (velX[i], velY[i])))
          txt.insert(END,("\nvelocidade total: %f\n" % (math.sqrt(math.pow(velX[i],2)+math.pow(velY[i],2)))))
          
          
          break
          # #gera os graficos       
        posicao_X.delete(0,END)
        posicao_Y.delete(0,END)
def graficos():
  global velX,velY,graficoTempo,grafico_bolaX,grafico_bolaY,roboX,roboY,distancia,aX, aY,grafico_aceleracaoMedia_BolaX, grafico_aceleracaoMedia_BolaY,grafico_velocidadeMedia_BolaX
          
  funcoes.gera_graficoVelocidadeRobo(velX, velY, graficoTempo)
  # geraGraficoVeloBola(gveloBolax, gveloBolay, tempoFloat)
  funcoes.gera_graficoPosicaoTempo(grafico_bolaX,grafico_bolaY,roboX,roboY, graficoTempo)
  # geraGraficoposicao(gbolaBx,gbolaBy,groboRx,tempoFloaty)
  funcoes.gerar_graficoDistancia(graficoTempo, distancia)
  funcoes.gera_graficoAceleracaoRobo(aX, aY, graficoTempo)
  # geraGraficoAceleracaoBola(gacelacaoBolaX, gacelacaoBolay, tempoFloat)
  funcoes.gera_graficoAceleracaoBola(grafico_aceleracaoMedia_BolaX, grafico_aceleracaoMedia_BolaY, graficoTempo)
  funcoes.gera_graficoVelocidadeBola(grafico_velocidadeMedia_BolaX, grafico_aceleracaoMedia_BolaY, graficoTempo)           

#botao de pesquisar
botPesquisar = Button(janela,text="Pesquisar!",font=("Arial",16),command=pesquisar)
botPesquisar.place(relx=0.5,rely=0.1)
bot_gerarGraficos = Button(janela,text="Gerar gráficos",font=("Arial",16),command=graficos)
bot_gerarGraficos.place(relx=0.5,rely=0.3)

#campo de entrada da palavra
posicao_X = Entry(janela,width=20,font=("Arial",16))
posicao_X.place(relx=0.2,rely=0.1)

#campo de entrada da frequencia
posicao_Y = Entry(janela,width=20,font=("Arial",16))
posicao_Y.place(relx=0.2,rely=0.15)


janela.mainloop()


