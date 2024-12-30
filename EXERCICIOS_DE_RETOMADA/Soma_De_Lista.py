'''
Soma_De_Lista
Criado Por: O BRUXO PYTHON
27/12/2024
'''
print("Soma_De_Lista")

# lista = [10,20,30,40,50,60,70,80,90,100]
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(lista)

total = 0

resultado=[]

for i in lista:
    
    total = total + i
    
    resultado.append(total)
    
print("_________________________") 
print(f" A soma da Lista é:{resultado[-1]}")
    
   
