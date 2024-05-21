
import random


int_teste1 =0

'''
Para gerar o número aleatório utilizamos a biblioteca e chamamos a função randrange() , que
recebe o intervalo de valores que o número aleatório deve estar. Então vamos passar o valor 0
(equivalente à primeira posição da nossa lista) e 4 (lembrando que o número é exclusivo, ou seja, o
número aleatório será entre 0 e 3, equivalente à última posição da nossa lista):
'''
int_randomica = random.randrange(0, 101)

while True: 
    if teste == 100:
        break
    elif teste == teste1:
        teste = random.randrange(0, 101)
        teste1 = 0
        print(teste)
    else:
        
        teste1+=1
