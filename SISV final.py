import random
import numpy as np
import matplotlib.pyplot as plt

n = 10000
tempo = 100
testes = 10
d = 0.95

pessoas = {}
pessoas2 = {}

l = 0.9
a = 0.3
g = 0.2
p = 0.3

S = 0
I = 0
V = 0

Sn = np.zeros(tempo + 1)
In = np.zeros(tempo + 1)
Vn = np.zeros(tempo + 1)
Tn = np.zeros(tempo + 1)

####################################################
details = "n"
#details = input("Show details? (y or n): ")
if details == "y":
    print("You chose to show details")
elif details == "n":
    print("You chose to not show details")
else:
    print("ERROR!")
    exit()

####################################################
for y in range(testes):
    S = 0
    I = 0
    V = 0
    for i in range(n):
        r = random.uniform(0, 1)
        if r <= d:
            pessoas[i] = 0
            S += 1 / n
        else:
            pessoas[i] = 1
            I += 1 / n
    Sn[0] += S
    In[0] += I

    if details == "y":
        print('Porcentagem de suscetiveis:', S / ((S + I) * 100), '%')
        print('################################')
        print('')
    ####################################################

    for t in range(1, tempo + 1):
        S = 0
        I = 0
        V = 0
        for i in range(n):
            pessoas2[i] = pessoas[i]
            r = random.uniform(0, 1)
            k = random.uniform(0, 1)
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
    print("Test number ", y + 1, " completed")
###################################
for t in range(0, tempo + 1):
    Sn[t] = Sn[t] / testes
    In[t] = In[t] / testes
    Vn[t] = Vn[t] / testes

###################################
for t in range(tempo + 1):
    Tn[t] = t

##################################
print("--------------------------------------------")
print("S")
print(Sn)
print("--------------------------------------------")
print("I")
print(In)
print("--------------------------------------------")
print("V")
print(Vn)

IMaior = 0
TMaior = 0
for i in range(tempo+1):
    if In[i] >= IMaior:
        IMaior = In[i]
        TMaior = i

print('-------------------------------')
if (d*(1-g)*l)/a > 1:
    print("COM SURTO EPIDEMICO!")
else:
    print("SEM SURTO EPIDEMICO!")
print("Re: ", (d*(1-g)*l)/a)
print("Maior I: ", IMaior)
print("Tempo do Pico: ", TMaior)
print('-------------------------------')

plt.plot(Tn, Sn, color='blue', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label= 'S')
plt.plot(Tn, In, color='orange', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label= 'I')
plt.plot(Tn, Vn, color='grey', linestyle='dashed', linewidth=1, marker='.', markerfacecolor='black', markersize=3, label= 'V')

# x-axis label
plt.xlabel('Tempo')
# frequency label
plt.ylabel('Densidade')
# plot title
plt.title('SISV Model')

plt.legend(loc="best")

# function to show the plot
plt.show()
