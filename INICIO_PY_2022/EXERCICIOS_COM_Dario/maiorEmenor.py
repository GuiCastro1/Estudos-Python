#Desenvolva um programa que apresente o maior e o menor valores da sequência


lista = [54, 10, 29, 87, 7, 64,100,150,2,6,8]


lista_ordenadas = sorted(lista)


print (lista)


print (lista_ordenadas)


    






lista = [54, 10, 29, 87, 7, 64,100,150,2,6,8]

maior = 0
menor = 100
aux = 0

for i in lista:

    if i >= aux and i >= maior:

        maior = i

    if i <= maior and i <= menor:

        menor = i
        
    if i <= menor and i >=aux:

        aux = i


print (menor)

print (maior)
 
