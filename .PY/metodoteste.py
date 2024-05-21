
def metodosoma (num01,num02):
    
    print('a soma de ' + num01 +' mais ' + num02 + " é igual: ", int(num01) + int(num02))


def metodosubtracao (num01,num02):

    print('a subtração de ' + num01 +' nemos ' + num02 + " é igual: ", int(num01) - int(num02))


def metodoporcemtagem (num01,num02):

    print((((int(num01) + int( num02))*15)/100) + int(num01) + int(num02))



   

    #print(((int(num01) + int( num02))*1.10))
    print('ksdlfk') 
    
    
def funcmultiplicao (num01,num02):

    i = (int(num01) * int(num02))

    return i

def funcdivivao (num01,num02):

    i = (int(num01) / int(num02))

    return i


i = 0
tatu =''
while True:

    tatu = input("\n\n digite\n so para somar,\n d divisão,\n su subtração,\n m multiplicção,\n p porcemtagem")

    num01 = 0
    num02 = 0
    resultado = 0

    num01 = input("Digite um numero: ")
    num02 = input("Digite outro numero: ")

    if tatu == "so":
        
        metodosoma (num01,num02)

    if tatu == "su":

        metodosubtracao (num01,num02)
        
    if tatu == "m":
        
        i=funcmultiplicao (num01,num02)
        
        print('a multiplicação de ' + num01 +' por ' + num02 + " é igual: ", i)

    if  tatu == "d":
         
        i=funcdivivao (num01,num02)
        
        print('a divisão de ' + num01 +' por ' + num02 + " é igual: ", i)


    if tatu == "p":
        
        metodoporcemtagem (num01,num02)
        
        print ("teste")                 

    tatu01 = input("digite S para um novo calculo ou N para sair")


    if tatu01 == "s" or tatu == "S":

        print("teste")

    
    #tatu01 = input("digite S para um novo calculo ou N para sair")    

    else:

        
        break


