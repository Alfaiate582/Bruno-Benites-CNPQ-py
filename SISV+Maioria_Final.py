import random
import numpy as np
import matplotlib.pyplot as plt


do = 0.55
de = 0.99 #densidade de suscetíveis

n = 10000 #numero de individuos
tempo = 100 #tempoSISV + Maioria3.py
testes = 20
opinion = {}
opinion2 = {}
pessoas = {}
pessoas2 = {}

l = 0.95
a = 0.2
g = 0.5
p = 0.2

S = 0
I = 0
V = 0

pro = np.zeros(tempo + 1)
proreg = np.zeros(tempo + 1)
anti = np.zeros(tempo + 1)
antireg = np.zeros(tempo + 1)
    
Tn = np.zeros(tempo + 1)
    
Sn = np.zeros(tempo + 1)
In = np.zeros(tempo + 1)
Vn = np.zeros(tempo + 1)

for j in range(testes):

    
    details = "n"


    ###################SORTEIOS###################################
    # OPINIÕES
    # Provacina = 1
    # antivacina = 0

    provacina = 0
    antivacina = 0
    for i in range(0, n):
        if (random.uniform(0, 1) > do):
            opinion[i] = 0
            antivacina += 1
        else:
            opinion[i] = 1
            provacina += 1

    pro[0] = (provacina / (provacina + antivacina))
    anti[0] = (antivacina / (provacina + antivacina))

    # SUSCETÍVEIS
    for i in range(0, n):
        if random.uniform(0, 1) <= de:
            pessoas[i] = 0
            S += 1
        else:
            pessoas[i] = 1
            I += 1
    Sn[0] += S / (S + I + V)
    In[0] += I / (S + I + V)

    print("PróVacina: ", pro[0]/j)
    print("Antivacina: ", anti[0]/j)
    print('-----------------------------------------')
    print("Suscetíveis: ", Sn[0])
    print("Infectados: ", In[0])
    print('-----------------------------------------')
    ###########################################################

    ###########################################################

    for t in range(1, tempo + 1):
        opinion2 = opinion
        for i in range(0, n):
            if opinion[i] == 1:
                if (anti[t - 1] * anti[t - 1]) >= random.uniform(0, 1):
                    opinion2[i] = 0
            elif opinion[i] == 0:
                if (pro[t - 1] * pro[t - 1]) >= random.uniform(0, 1):
                    opinion2[i] = 1

        pessoas2 = pessoas
        S = 0
        I = 0
        V = 0
        for i in range(0, n):
            r = random.uniform(0, 1)
            k = random.uniform(0, 1)
            if opinion[i] == 1:
                if pessoas[i] == 1:
                    if r <= a:
                        pessoas2[i] = 0
                elif pessoas[i] == 2:
                    if r <= p:
                        pessoas2[i] = 0
                elif pessoas[i] == 0:
                    if r <= g:
                        pessoas2[i] = 2
                    else:
                        v = random.randint(0, n - 1)
                        if pessoas[v] == 1:
                            if k <= l * (1 - g) * (1 / (1 - g)):
                                pessoas2[i] = 1

            elif opinion[i] == 0:
                if pessoas[i] == 1:
                    if r <= a:
                        pessoas2[i] = 0
                elif pessoas[i] == 2:
                    if r <= p:
                        pessoas2[i] = 0
                elif pessoas[i] == 0:
                    v = random.randint(0, n - 1)
                    if pessoas[v] == 1:
                        if k <= l:
                            pessoas2[i] = 1

        for i in range(n):
            if pessoas2[i] == 0:
                S += 1 / n
            if pessoas2[i] == 1:
                I += 1 / n
            if pessoas2[i] == 2:
                V += 1 / n
            pessoas[i] = pessoas2[i]

        if details == "y":
            print('-----------------------------------------')
            print('Tempo: ', t)
            print("S= ", S)
            print("I= ", I)
            print("V= ", V)
        Sn[t] += S
        In[t] += I
        Vn[t] += V

        provacina = 0
        antivacina = 0
        for i in range(0, n):
            if opinion2[i] == 0:
                antivacina += 1
            else:
                provacina += 1
        pro[t] = (provacina / (provacina + antivacina))
        anti[t] = (antivacina / (provacina + antivacina))
        opinion = opinion2
    
    for c in range(tempo+1):
        proreg[c] += pro[c]
        antireg[c] += anti[c]
    

for i in range(tempo+1):
    Sn[i] = Sn[i]/testes
    In[i] = In[i]/testes
    Vn[i] = Vn[i]/testes
    proreg[i] = proreg[i]/testes
    antireg[i] = antireg[i]/testes
    

for t in range(tempo + 1):
    Tn[t] = t


print(Sn)
print("##########")
print(In)
print("##########")
print(Vn)
print("##########")


#plt.plot(Tn, pro, color='green', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3)
#plt.plot(Tn, anti, color='red', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3)

#plt.xlabel('Tempo')
#plt.ylabel('Densidade')
#plt.title('Regra da maioria')

#plt.show()



#####################################################
print("#################################")
Re = (1-g*do) * (de*(l/a))
print("Re = ", Re)
if Re >= 1:
    print("Epidemic Outbreak detected")
else:
    print("No Epidemic Outbreak")
print("Highest I = ", np.max(In))
print("Time of the highest I = ", np.argmax(In))
    
print("##################################")
if de > 0.5:
    lc = a*((g+p)/(p*(1-g)))
elif de < 0.5:
    lc = a
elif de == 0.5:
    lc = "unknown"
print("Lc = ", lc)
print("#################################")


plt.plot(Tn, Sn, color='blue', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label='S')
plt.plot(Tn, In, color='red', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label='I')
plt.plot(Tn, Vn, color='green', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label="V")
plt.plot(Tn, proreg, color='black', linestyle='dotted', linewidth=1, marker='', markerfacecolor='black', markersize=3, label="pro-vacine")
#plt.plot(Tn, antireg, color='purple', linestyle='dotted', linewidth=1, marker='', markerfacecolor='black', markersize=3, label="anti-vacine")


plt.ylim(-0.01, 1.01)

# x-axis label
plt.xlabel('Time')
# frequency label
plt.ylabel('Density')
# plot title
plt.title('SISV + Major rule')

plt.legend(loc="upper right")

# function to show the plot
plt.show()
