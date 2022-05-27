from re import template
import funcoes

tempoFloat = []
bolaX = []
bolaY = []

vmax = 2.3
aceleracao = 1.5
veloAlvo = 1.52
tempoFloat = funcoes.leitura_arquivos("bola_tempo.txt")
bolaX = funcoes.leitura_arquivos("bola_posX.txt")
bolaY = funcoes.leitura_arquivos("bola_posY.txt")

tempo =(velocidade_atual*0.54)/velocidade_maxima


#velocidade maxima = 0.54
#velocidade_atual = x


#v = v0+at
#(v-v0)/a
tempoFreio = (vmax-veloAlvo)/aceleracao
indice = tempoFreio/0.02
arredonda = int(indice)

print(tempoFreio)

freando = False
velocidade = [0]
for i in range(len(tempoFloat)):
    velocidade.insert(i+1,(velocidade[i]+aceleracao*0.02))
    if velocidade[i+1]>=vmax:
        velocidade[i+1] = vmax
        aceleracao*=-1
        freando = True
        print(f"Atingiu a {velocidade[i+1]} no tempo {tempoFloat[i]} ")
    if velocidade[i+1] <= veloAlvo and freando == True:
        velocidade[i+1] = veloAlvo
        print(f"Atingiu a {velocidade[i+1]} no tempo {tempoFloat[i]} ")
        
        break


velocidade.pop(0)

#print(velocidade)


#x = destinoX - roboX[i] = v0x*t + 0.5*aX*t
#destinoX - roboX[i]
