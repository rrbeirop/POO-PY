try:
    import funcoes
    import os
  
    while True:
     nome = "dados.txt"
     valor_cripto = 10
  
    lin = "-"*30
    opcao = int (input(f"1- CRIPTAR:\n{lin}\n2- DESCRIPTAR:\n{lin}\n3- SAIR:\n{lin}\nDIGITE SUA OPÇÃO :"))
    
    #texto = input("DIGITE SUA OPÇÃO : ")
    if opcao ==1:
      texto = input("DIGITE SUA FRASE :")
      os.system('cls')
      
      funcoes.cript(nome,texto,valor_cripto)
    
    elif opcao ==2:
      funcoes.descript(nome,valor_cripto)
      
    
    elif opcao ==3:
      break
    
    else: 
      print("OPÇÃO INVALIDA")
except:
    #  print("ARQUIVO NÃO ENCONTRADO")
