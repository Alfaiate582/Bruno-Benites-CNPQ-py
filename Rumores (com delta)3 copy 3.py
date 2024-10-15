import random
import math
import numpy as np
import matplotlib.pyplot as plt

n = 1000 #numero de pessoas
de = 0.01 #densidade de espalhadores
tempo = 50
testes = 1
pessoas = {}
pessoas2 = {}

x = 0 #VARIAVEL DE TESTE DE SOMATORIO

l = 0.9
a = 0.8
d = 0

In = np.zeros(tempo + 1)
Sn = np.zeros(tempo + 1)
Rn = np.zeros(tempo + 1)
Tn = np.zeros(tempo + 1)



detalhes = 1

##########################################################

for y in range(testes):


    I = 0
    S = 0
    R = 0

    for i in range(n):
        if i > n*de:
            pessoas[i] = 0
            I += 1 /n
        else:
            pessoas[i] = 1
            S += 1 /n

    In[0] += I
    Sn[0] += S

    # 0 = I - Ignorantes
    # 1 = S - Espalhadores
    # 2 = R - Recusadores

    #if detalhes == 1:
    #    print("Porcentagem de Espalhadores:", Sn[0])
    #    print("Porcentagem de Ignorantes:", In[0])
    #    print("Porcentagem de Recusadores:", Rn[0])
    #    print('################################')
    #    print('')

    for t in range(1, tempo + 1):
        I = 0
        S = 0
        R = 0

        for i in range(n):
            r2 = random.uniform(0,1)
            r3 = random.uniform(0,1)
            r4 = random.uniform(0,1)
            k = random.randint(0,n-1)
            if pessoas[i] == 0:
                if pessoas[k] == 1:
                    if r2 <= l:
                        pessoas2[i] = 1
                    else:
                        pessoas2[i] = 0
                else:
                    pessoas2[i] = 0
            elif pessoas[i] == 1:
                if r3 <= d:
                    pessoas2[i] = 2
                elif (pessoas[k] == 1 or pessoas[k] == 2):
                    if r4 <= a:
                        pessoas2[i] = 2
                    else:
                        pessoas2[i] = 1
                else:
                    pessoas2[i] = 1
            elif pessoas[i] == 2:
                pessoas2[i] = 2
                


        for c in range(n):
            if pessoas2[c] == 0:
                I += 1 / n
            elif pessoas2[c] == 1:
                S += 1 / n
            elif pessoas2[c] == 2:
                R += 1 / n

        pessoas = pessoas2
        

        In[t] += I
        Sn[t] += S
        Rn[t] += R
    print("Test number ", y + 1, "/",testes," completed")


for t in range(tempo + 1):
    Tn[t] = t

In = In/testes
Sn = Sn/testes
Rn = Rn/testes
Tn = Tn/testes

if detalhes == 1:
    print("--------------------------------------------")
    print("I")
    print(In)
    print("--------------------------------------------")
    print("S")
    print(Sn)
    print("--------------------------------------------")
    print("R")
    print(Rn)

print(x)

############################################

I2 = 1-de
S2 = de
R2 = 0

In2 = np.zeros(tempo + 1)
Sn2 = np.zeros(tempo + 1)
Rn2 = np.zeros(tempo + 1)

In2[0] = I2
Sn2[0] = S2
Rn2[0] = R2

for i in range(1, tempo + 1):
    In2[i] = In2[i-1]+(-l*In2[i-1]*Sn2[i-1])
    Sn2[i] = Sn2[i-1]+ (l*In2[i-1]*Sn2[i-1]) - (a*Sn2[i-1]*(Sn2[i-1] + Rn2[i-1])) - (d*Sn2[i-1])
    Rn2[i] = Rn2[i-1]+ a*Sn2[i-1]*(Sn2[i-1] + Rn2[i-1]) + (d*Sn2[i-1])


alfa = a
St = Sn[6]
Rt = Rn[6]

############################################



plt.plot(Tn, In, color='blue', linewidth=0.5, marker='.', markerfacecolor='black', markersize=3, label= 'I')
plt.plot(Tn, Sn, color='orange', linewidth=0.5, marker='.', markerfacecolor='black', markersize=3, label= 'S')
plt.plot(Tn, Rn, color='grey', linewidth=0.5, marker='.', markerfacecolor='black', markersize=3, label= 'R')



# x-axis label
plt.xlabel('Tempo')
# frequency label
plt.ylabel('Densidade')
# plot title
plt.title('Disseminação de Rumores 1')

plt.legend(loc="best")

# function to show the plot
plt.show()


