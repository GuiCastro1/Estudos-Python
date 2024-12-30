'''
Criado: Dario o MAGO DO PYTHON
Data:01/09/22
Progama: adivinha números
'''


print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

#variaveis do programa
int_numeroSecreto =40
int_aux = 0
str_SaiDoPrograma =''
int_numero =0

'controla o sistema, sendo controlado pelo if de numero 01
while True: # while 01

    while True:# while 02

        int_numero = int(input('\nDigite um numero entre 0 à 100\n'))
        
        if int_numero <=100 and int_numero>=0:

            if int_numero == int_numeroSecreto:

                print("acertou o numero!!")

                #variavel int_aux somada int_numeroSecreto para alterar o numero secreto! 
                int_numeroSecreto+= int_aux

                break #sai do while 02

            elif int_numero > int_numeroSecreto:
                print("Você errou!! número digitado é maior que o número secreto!!")
                
                #variavel auxiliar para alterar o numero secreto!
                int_aux+= 2

            elif int_numero < int_numeroSecreto:
                print("Você errou!! número digitado é menor que o número secreto!!")
                #variavel auxiliar para alterar o número secreto!
                int_aux-= 5

        else:
            print('Número inválido!!')

    print(int_numeroSecreto)

    #controla o while 01
    str_SaiDoPrograma = input('S para jogar novamente, N para sair!')

    if str_SaiDoPrograma.upper() == 'N': # if 01
        break
    
        
