'''
Tabela_De_Multiplicacao
Criado Por: O BRUXO PYTHON
27/12/2024
'''

def TabelaDeMultiplicacao(valor):
    
    for i in range(1,11):
        
        teste = i * valor
        
        print(f"{i} x {valor} é = {teste}")

        
valor = int(input("Digito um número para exibir a tabuada ate o 10"))

TabelaDeMultiplicacao(valor)


def tabuada(valor):
    
    resultado = []
    
    for i in range(1,11):
        resultado.append(i * valor)
        
    return resultado

valor = int(input("Digito um número para exibir a tabuada ate o 10"))

resposta = tabuada(valor)

print(resposta)