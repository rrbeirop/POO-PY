
def create_ong(nome,tipo,cnpj):
    ong ={
    "nome":nome,
    "tipo":tipo,
    "CNPJ":cnpj,
    "projetos":[]
    }
    return ong

def create_projeto(nome,descricao):
    projeto = {
    "nome": nome,
    "descricao" : descricao

    }
    return projeto

def localizar_ong(nome,cat):
    for ong in cat:
        if ong['nome']== nome:
            return ong
    return None

def localizar_ong_index(nome,cat):
    for index in range(0,len(cat)):
        if cat[index]['nome']==nome:
            return index
    return None

