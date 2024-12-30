
'''
import math

def converter(num):
    
    Celcius = (num * 1.8) + 32
    
    Fahrenheit = (num - 32) / 1.8
    
    print (f" A temperatura {num} é igual:")
    
    print (f"Celcius:{Celcius}°C")
    
    print (f"Fahrenheit:{Fahrenheit}°F")
        
gui = int (input("Digite a temperatura que deseja converter para Celcius e Fahrenheit"))

converter(gui)
'''
def convt():
    
    while True:
        
        conversao = input("Digite F para converter Fahrenheit para Celcius \n&\n C para converter de Celcius para Fahrenheit")
    
        if conversao == "F" or conversao =="f":
        
            num = int (input("Digite a temperatura em Fahrenheit para converter em Celcius"))
        
            Celcius = (num - 32) / 1.8
    
            print (f" A temperatura {num} em Fahrenheit é igual:{Celcius}°C Graus Celcius")
        
        if conversao == "C" or conversao =="c":
        
            num = int (input("Digite a temperatura em Celcius para converter em Fahrenheit"))
        
            Fahrenheit = (num * 1.8) + 32
        
            print (f" A temperatura {num} em Celcius é igual:{Fahrenheit}°F Graus Fahrenheit")
            
        rodar = input("Deseja Converter Novamente?\nY ou N")
    
        if rodar == "Y" or rodar =="y":
    
            convt()   
            
        else:  
            break

convt() 
'''
O motivo pelo qual o None está sendo impresso após os resultados é que sua função converter() não retorna nenhum valor explicitamente. Em Python, quando uma função não tem um return, ela retorna None por padrão.

Você pode corrigir isso removendo o print(r) fora da função, já que a função já está imprimindo os resultados internamente. Aqui está a versão corrigida:

python
Copiar código
def converter(num):
    Celcius = (num * 1.8) + 32
    Fahrenheit = (num - 32) / 1.8
    print(f"A temperatura {num} é igual:")
    print(f"{Celcius}°C")
    print(f"{Fahrenheit}°F")
        
gui = int(input("Digite a temperatura que deseja converter para Celsius e Fahrenheit: "))

converter(gui)
Agora, a função converter() vai imprimir diretamente os resultados e o None não será mais mostrado. Você não precisa usar print(r) após a chamada da função, pois os resultados já são exibidos dentro da função.


O código está funcional, mas há algumas áreas que podem ser melhoradas para torná-lo mais eficiente e organizado. Aqui estão os pontos principais:

Evitar recursão desnecessária: Embora a recursão funcione, não é ideal em situações onde o número de chamadas pode ser indefinido (como um loop contínuo). Isso pode levar a um estouro de pilha. Em vez disso, você já tem um loop while True que é suficiente para lidar com a repetição.

Melhorar a legibilidade: Variáveis e mensagens podem ser mais claras. Por exemplo, usar lower() para comparar entradas sem se preocupar com maiúsculas ou minúsculas.

Validação de entrada: O programa pode validar melhor as entradas do usuário, garantindo que sejam números válidos ou opções corretas.

Evitar redundância: O código pode ser reorganizado para evitar duplicação de lógica.

Segue uma versão melhorada, mas sem recursão:

python
Copiar código
def converter_temperatura():
    while True:
        # Solicita a conversão desejada
        conversao = input("Digite 'F' para converter Fahrenheit para Celsius\nou 'C' para converter Celsius para Fahrenheit: ").strip().lower()
        
        if conversao == "f":
            try:
                num = float(input("Digite a temperatura em Fahrenheit para converter em Celsius: "))
                celsius = (num - 32) / 1.8
                print(f"A temperatura {num}°F é igual a {celsius:.2f}°C.")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif conversao == "c":
            try:
                num = float(input("Digite a temperatura em Celsius para converter em Fahrenheit: "))
                fahrenheit = (num * 1.8) + 32
                print(f"A temperatura {num}°C é igual a {fahrenheit:.2f}°F.")
            except ValueError:
                print("Por favor, insira um número válido.")
        else:
            print("Opção inválida. Tente novamente.")
        
        # Pergunta ao usuário se ele quer continuar
        rodar = input("Deseja converter novamente? (Y/N): ").strip().lower()
        if rodar != "y":
            print("Encerrando o programa. Até logo!")
            break

converter_temperatura()
Implementação com Recursão (Sem Código)
Sim, é possível usar recursão. Em vez de usar um while, você pode fazer a função se chamar novamente ao final, desde que gerencie bem os casos de término para evitar loops infinitos. Para evitar pilhas excessivas, seria necessário usar um limite ou configurar condições claras de saída.

Se precisar, posso detalhar os conceitos para adaptar a recursão ao seu código!
'''