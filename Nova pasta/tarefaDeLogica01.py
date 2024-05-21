
Lst_lista = ['330344','349344','336549344','336554244','00365','10365','600365','63442344','43245644','39234423444','88888888444','56666444','594444944','5944494']

for i in Lst_lista:
#if i is not '8' :
#print('secretaria', i)
   
    

    if  '44' in i :
        print('secretaria', i)

    elif i[0]=='3' and i[1]=='3' or i[1]=='4' and i[3]=='3':
        print('cliente', i)

    elif i[0]=='3' and i[1]=='3' and i[2]=='6' and i[3]=='5':
        print('garçon', i)

        
    elif i[0]=='0' or i[0]=='1' or i[0]=='2' : #3 na lista
        print('manobrista',i)

    elif  i[0]=='6' and  i[2] != '7' and i[3]!='9':
        print('faxineira',i)

    elif i[0]!= '5' and i[2] != '8' and i[3]!='8':
        print('manutenção',i)

    elif i[1] not in '9':
        print('piloto de caça',i)

