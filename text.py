from re import template
import funcoes

tempoFloat = []
bolaX = []
bolaY = []

vmax = 2.8

tempoFloat = funcoes.leitura_arquivos("bola_tempo.txt")
bolaX = funcoes.leitura_arquivos("bola_posX.txt")
bolaY = funcoes.leitura_arquivos("bola_posY.txt")

velocidade = [0]
for i in range(len(tempoFloat)):
    velocidade.insert(i+1,(velocidade[i]+0.7*tempoFloat[i]))
    if velocidade[i+1]>=vmax:
        print(tempoFloat[i])
        break

velocidade.pop(0)

#print(velocidade)