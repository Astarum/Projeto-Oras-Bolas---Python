

arquivo  = open('aba.txt','r')

file = arquivo.readlines()

arquivo.close()

certo = []

for i in file:
    
    i =i.replace(",",".")
    a = i.strip().split()       
    certo.append(a)




arquivo = open("bola_tempo.txt","w")
for i in range(len(certo)):
    arquivo.write(certo[i][0]+"\n")

arquivo = open("bola_posX.txt","w")
for i in range(len(certo)):
    arquivo.write(certo[i][1]+"\n")    

arquivo = open("bola_posY.txt","w")
for i in range(len(certo)):
    arquivo.write(certo[i][2]+"\n")








        
    




