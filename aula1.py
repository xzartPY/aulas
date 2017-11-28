var_ = raw_input('Digite seu nome: ')
                 
var_1 = raw_input('Qual comida voce gosta?: ')

print(var_ + ' gosta de ' + var_1)

var_2 = raw_input('Gostaria de deixar outra pessoa responder? sim/nao: ')



if var_2 == 'sim':
                 nome = raw_input('Digite seu nome: ')

                 comida = raw_input('Qual comida voce gosta?: ')

                 print(nome + ' gosta de ' + comida)
                 print('obrigado por usar ' + var_ + ", e " + nome)
                           


else:
                 print('obrigado por usar ' + var_)
                 

    
