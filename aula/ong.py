doacao_valor= []
doacao_nome= []
import os
def informacoes_doacao(valor):
    sub_opcao = int (input("Doação Anonima ?\n1 - para sim \n2 - para não: "))
    if sub_opcao ==1:
        print("A Sua doação sera anonima, obrigado")
        doacao_nome.append("Anonimo") 
    else :
        nome = input("digite seu nome :")
        cpf = int(input ("informe seu cpf"))
        email = input("informe seu email:")
        doacao_nome.append(nome) 
    doacao_valor.append(valor)
    
    print(f"valor doado foi: {valor}")
    os.system('cls')
      
opcao = 7
while opcao !=6:
      total = 0
      for i in range (0,len(doacao_valor)):
          print (f"Nome: {doacao_nome[i]} | Valor:R$ {doacao_valor[i]}")
          
          total = total + doacao_valor [i]

      print (f"Total doado R$: {total}")

      print ("""OPÇÕES DE MENU: \n1 - R$50,00\n2 - R$100,00\n3 - R$200,00\n4 - R$300,00\n5 Outros valores:\n6 Sair:\n""")
      opcao = int (input("QUAL SUA OPÇÃO :"))
      os.system('cls')
      print ("MUITO OBRIGADO PELA SUA DOAÇÃO")
      
      if opcao == 1:
        informacoes_doacao(50)
      elif opcao == 2:
        informacoes_doacao(100)
      elif opcao == 3:
        informacoes_doacao(200)
      elif opcao == 4:
        informacoes_doacao(300)
      elif opcao == 5:
        pass
      elif opcao == 6:
        pass
      else:
         print ("Essa opcão é inválida.")
             
