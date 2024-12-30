'''
Escreva um programa em Python que calcule a soma de todos os números ímpares entre 1 e N
(onde N é um número inteiro positivo fornecido pelo usuário).
''' 

def SomaDeImpar(num):
    
    lista = []
    total = 0
    
    for i in range(1,num+1):
     
     if i %2 == 1:   
         lista.append(i)
    print(f"existem {len(lista)} de números de 1 a {num} que são impares")
          
    for x in lista:
        
        total += x
        
    return total


teste = int(input("Digite um Número para saber a soma de todos os impares ate esse numero."))

teste =SomaDeImpar(teste)

print(f"E a soma deles é igual a:{teste}")

