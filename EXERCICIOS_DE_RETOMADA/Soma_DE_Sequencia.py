'''
Soma De Sequencia
Criado Por: O BRUXO PYTHON
13/12/2024
'''
soma=0

for i in range(1,101):

    soma+=i

    print(soma)

multiplos=[]

# acumulador = 0

for i in range(1,101):

    # acumulador = i % 3

    if i %3 == 0:

        multiplos.append(i)

        print(multiplos)
