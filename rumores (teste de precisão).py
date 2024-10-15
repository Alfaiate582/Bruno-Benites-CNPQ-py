import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000  # numero de pessoas
de = 0.01  # densidade de espalhadores
tempo = 50
testes = 1
pessoas = {}
pessoas2 = {}

x = 0 
z = 0

w = 0

for lj in range(1, 10):
    for aj in range(1, 10):
        for dj in range(1, 10):


            l = lj / 10
            a = aj / 10
            d = dj / 10

            detalhes = 0

            ##########################################################

            for y in range(testes):

                In = np.zeros(tempo + 1)
                Sn = np.zeros(tempo + 1)
                Rn = np.zeros(tempo + 1)
                Tn = np.zeros(tempo + 1)

                I = 0
                S = 0
                R = 0

                for i in range(n):
                    r = random.uniform(0, 1)
                    if r >= de:
                        pessoas[i] = 0
                        I += 1 / n
                    else:
                        pessoas[i] = 1
                        S += 1 / n
                In[0] += I
                Sn[0] += S

                # 0 = I - Ignorantes
                # 1 = S - Espalhadores
                # 2 = R - Recusadores

                if detalhes == 1:
                    print("Porcentagem de Espalhadores:", Sn[0])
                    print("Porcentagem de Ignorantes:", In[0])
                    print("Porcentagem de Recusadores:", Rn[0])
                    print('################################')
                    print('')

                for t in range(1, tempo + 1):
                    I = 0
                    S = 0
                    R = 0

                    for i in range(n):
                        r1 = random.uniform(0, 1)
                        r2 = random.uniform(0, 1)
                        r3 = random.uniform(0, 1)
                        r4 = random.uniform(0, 1)
                        k = random.randint(0, n - 1)
                        if pessoas[i] == 1:
                            if r4 <= d:
                                pessoas2[i] = 2
                            else:
                                pessoas2[i] = 1
                        if pessoas[i] == 0 and pessoas[k] == 1:
                            if r1 <= l:
                                pessoas2[i] = 1
                            else:
                                pessoas2[i] = 0
                        elif pessoas[i] == 1 and pessoas[k] == 1:
                            if r2 <= a:
                                pessoas2[i] = 2
                            else:
                                pessoas2[i] = 1
                        elif pessoas[i] == 1 and pessoas[k] == 2:
                            if r3 <= a:
                                pessoas2[i] = 2
                            else:
                                pessoas2[i] = 1

                        else:
                            pessoas2[i] = pessoas[i]

                    for c in range(n):
                        if pessoas2[c] == 0:
                            I += 1 / n
                        elif pessoas2[c] == 1:
                            S += 1 / n
                        elif pessoas2[c] == 2:
                            R += 1 / n

                    In[t] += I
                    Sn[t] += S
                    Rn[t] += R
                    pessoas2 = pessoas

            for t in range(tempo + 1):
                Tn[t] = t

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

            ############################################

            I2 = 1 - de
            S2 = de
            R2 = 0

            In2 = np.zeros(tempo + 1)
            Sn2 = np.zeros(tempo + 1)
            Rn2 = np.zeros(tempo + 1)

            In2[0] = I2
            Sn2[0] = S2
            Rn2[0] = R2

            for i in range(1, tempo + 1):
                In2[i] = In2[i - 1] + (-l * In2[i - 1] * Sn2[i - 1])
                Sn2[i] = Sn2[i - 1] + (l * In2[i - 1] * Sn2[i - 1]) - (a * Sn2[i - 1] * (Sn2[i - 1] + Rn2[i - 1])) - (
                        d * Sn2[i - 1])
                Rn2[i] = Rn2[i - 1] + a * Sn2[i - 1] * (Sn2[i - 1] + Rn2[i - 1]) + (d * Sn2[i - 1])

            alfa = a
            St = Sn[6]
            Rt = Rn[6]

            ############################################

            wo = abs(Rn[t-1] - Rn2[t-1])
            if wo > z:
                z = wo
            w += wo
            print(z)
            x+=1
            #print("Test nº", x,"/1331 completed")

we = w/(x)
print("ERROR: " , we,"%")
print("MAX: ", z)