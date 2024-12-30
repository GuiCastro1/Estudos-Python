# '''
# Maior_&_Menor
# Criado Por: O BRUXO PYTHON
# 27/12/2024
# '''
print("--Maior_&_Menor--")
lista =[10,23,25,33,79,100,130,125,4312,1,2,3,5,4,9]

Maior = lista[0]
Menor = lista[0]

for i in lista:
    
    if i > Maior:
        Maior = i
        
    if i < Menor:
        Menor = i 
        
        print(f"Menor: {Menor}")
        print(f"Maior: {Maior}")

        print("O programa acabou!!!")

