vagas =[
    ['O','O','O'],
    ['O','O','O'],
    ['O','O','O']
]

placa = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
""" for i in range(0,len(vagas)):
  print(vagas[i]) """
import os
def imprimir_estacionamento():
    for i in range(0,len(vagas)):
        print(vagas[i], end=" ")
        print(placa[i])



        
def menu():
    print ("SEJA BEM VINDO")
    
    print('1 - Estacionar')
    print('2 - Retirar')
    print('3 - Adicionar Setor')
    print('4 - Remover Setor')
    print('5 - Sair')

          
while True:
    imprimir_estacionamento()
    menu()
    op = (input("Selecione uma opção :")) 
    if op == '1': 
        setor = int (input("informe o setor:"))
        vaga = int (input("informe a vaga:"))
        p1 = input("informe a placa do carro :").upper()
        

        if vagas[setor][vaga]== 'X':
            os.system('cls')
            print("Vaga Ocupada:")

        else:
            vagas[setor][vaga] = 'X'
            placa[setor][vaga] = p1
            os.system('cls')
            print (f" CARRO: {placa[setor][vaga]} - Estacionou")
            

    elif op == '2':
        setor = int (input("informe o setor:"))
        vaga = int (input("informe a vaga:"))

        if vagas[setor][vaga]== 'X':
            os.system('cls')
            print("Vaga Livre:")
            vagas[setor][vaga] = 'O'
            placa[setor][vaga] = ' '

        else:
            os.system('cls')
            print ("Nenhum carro estacionado!")
           
    elif op == '3':
        
        vagas.append (['O','O','O'])
        placa.append ([" ", " ", " "])

    elif op == '4':
    
        vagas.remove (['O','O','O'])
        placa.remove ([" ", " ", " "])

    elif op == '5' :
        print("VOLTE NUNCA MAIS!!")

        break
        
    
    

    
