tabela_dados =[
    ['Nome:' , 'Vitor,''Gean'', "Carlos", "Bruna' ],
    ['Valor:' , "20","19","18","17,"],
    ['Cpf:', "1", "2", "3", "4"],
    ['Email:', "@", "@@", '@@@',"@@@@"],
    ['Telefone:',"67",'66','65,"64" '], 
    ]


for i in range(0, len(tabela_dados[0])):
    linha = ''

for i in range(0, len(tabela_dados)):
    linha = linha + str(tabela_dados[i][0])+''
print(linha)

for i in range(0, len(tabela_dados[0])):
    linha = ''

for i in range(0, len(tabela_dados[0])):
    linha = linha + str(tabela_dados[i][1])+''
print(linha)

#for i in range(0,len(tabela_dados)):
    #print(tabela_dados[i][0],tabela_dados[i][1])
