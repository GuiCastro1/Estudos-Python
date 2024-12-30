'''
Fatorial
Criado Por: O BRUXO PYTHON
27/12/2024
'''

def fat1(n):
    if n <= 1:
        return 1
    return n*fat1(n-1)

def fat2(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

valor01 = 5
valor02 = 5

resultado01=fat1(valor01)
resultado02=fat2(valor02)

print(resultado01)
print(resultado02)

def fat3(n):
    
    i =1
    resultado = 1

    while i <= n:
     
        resultado *= i

        i+=1
    
    print(resultado)
    
valor03 = 5

resultado03=fat3(valor03)

def fat4(n):
    i = 1
    aux = 1
    
    while i <= n:
        
        aux *= i
        
        i += 1
        
    return aux  

valor04 = 5

resultado04=fat4(valor04)

print(resultado04)