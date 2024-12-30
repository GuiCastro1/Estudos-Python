'''
ConversorDeBinarios
Criado Por: O BRUXO PYTHON
13/12/2024
'''

#Pegar numero decimal
decimal =  int(input("Digite um número para converter em Binário"))
binario = " "
listaDeNumeros =[]


while decimal > 0 :

#dividir por 2
    binario = decimal % 2 
#pegar resto e por no ARRAY
    listaDeNumeros.append(binario)
#continuar dividindo o coeficiente por 2 ate chegar em 0
    decimal = decimal//2
#Exibir o ARRAY com os binarios 
    # print(listaDeNumeros)
    print(listaDeNumeros[::-1])