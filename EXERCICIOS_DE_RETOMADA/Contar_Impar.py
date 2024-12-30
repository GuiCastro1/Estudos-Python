

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
par = []
impar = []

for i in lista:
    
    if i % 2 == 1:
        impar.append(i)
        
    else:
        par.append(i)
        
print(impar)

print(f"Existem {len(impar)} números impares nessa lista")

print(par)

print(f"Existem {len(par)} números pares nessa lista")
        
        