import cls
carros = []
while True:
    print('1 - Criar Carro\n2 - Selecionar Carro\n0 - Sair')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        _marca = input('Marca: ')
        _modelo = input('Modelo: ')
        _ano = int(input('Ano: '))
        _cor = input('Cor: ')
     #   print(f"{_marca,_modelo,_ano,_cor}")
        carro = carro(_marca,_modelo,_ano,_cor)
        carros.append(carro)
    elif op == 2:
        op = int(input('Selecione um carro: '))
        carro_selecionado = carro[op-1]
        op_2 = int(input('1 - Ligar Motor\n2 - Desligar Motor\n3 - Painel\nEscolha uma opção: '))
        if op_2 == 1:
            carro_selecionado.ligar_motor()
        elif op_2 == 2:
            carro_selecionado.desligar_motor()
        elif op_2 == 3:
            carro_selecionado.status_motor_painel()

