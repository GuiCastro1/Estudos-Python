'''
Fibonacci
Criado Por: O BRUXO PYTHON
13/12/2024
'''
Armazenamento = [0,1]

PegadorDeNumero =20

# Index = 2
while len(Armazenamento) <= PegadorDeNumero:

    resultado = Armazenamento[-1]+Armazenamento[-2]    

    Armazenamento.append(resultado)


print(Armazenamento)




#Pegar input de Termo da sequencia
#Definir como range
#Primeiro range tem que somar 1+0 
#Colocar resultado no Array 
#E somar o resustado mais o ultimo numero
#Realizar isso ate que renge seja === 0

