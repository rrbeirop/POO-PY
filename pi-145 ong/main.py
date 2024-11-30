import funcoes as f
import views 
import os
cat = []
while True:
    views.menu_principal()
    lin = ('_'*30)
    op = int(input(" < INFORME SUA OPÇÃO:\n "))
    os.system("cls")
    if 1 == op:
          nome= input("NOME DA ONG :")
          tipo= input("TIPO DE ONG :")
          cnpj= int(input("CNPJ DA ONG :"))
          print("ONG Cadrastada com Sucesso")

          ong = f.create_ong(nome,tipo,cnpj)

    elif 2 == op:
        nome = input("NOME DO PROJETO:")
        descricao = input("DESCRIÇÃO:")
        projeto = f.create_projeto(nome, descricao)
      #  ong = f.localizar_ong()
        nome_ong = input("Informe o nome da ONG:")
        print("Projeto Cadrastrado com Sucesso")
        index = f.localizar_ong_index(nome_ong,cat)
        if index is None:
             print("NAO EXISTE RAFAEL")
    
        else:
            ong['projetos'].append(projeto)
            cat.append(ong)
            break

        
    elif 3 == op:
        nome_ong = input("nome da ong:")
        index = f.localizar_ong_index(nome_ong,cat)
        if index is None:
                 print("NAO EXISTE RAFAEL")
                 break
        cat[index]['nome'] = input('novo nome')
         