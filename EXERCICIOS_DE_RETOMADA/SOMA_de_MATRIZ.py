

def soma(M1,M2):
    
    soma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    
    print(soma)
    
    
def subtrai(M1,M2):
    
    subtrai = [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))] 
    
    print(subtrai)
    
def multiplica(M1,M2):
    
    multiplica = [[matriz1[i][j] * matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    
    print(multiplica)
    
def divide(M1,M2):
    
    divide = [[matriz1[i][j] / matriz2[i][j] for j in range(len(matriz1[0]))]for i in range(len(matriz1))]
    
    print(divide)
    
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

soma(matriz1,matriz2)

subtrai(matriz1,matriz2)

multiplica(matriz1,matriz2)

divide(matriz1,matriz2)
