#nome = "texto.txt"
#valor_cripto =1
#frase = input("digite: " )
#new_frase = ''

def cript(nome,frase,valor_cripto):
    
    discritor = open(nome,"a")
    new_frase = ''
    for letra in frase:
        new_frase += chr((ord(letra)+valor_cripto)%127)
    discritor.write(new_frase + '\n')
    return new_frase

def descript(nome, valor_cripto):


    discritor = open(nome, "r")
    new_frase = ''
    numero = chr((10)%127)
    for letra in discritor.read():
        
        if numero == letra: 
            new_frase += " \n"

        else :new_frase += chr((ord(letra) - valor_cripto)%127)
       #new_frase += chr((ord(letra) + valor_cripto)%127)
    print(new_frase)


    #for salto in range(0,128):
     #   new_frase = ''
      #  discritor = open(nome, "r")
  
        # for letra in discritor.read():

         # new_frase += chr((ord(letra) - salto))
         # print(new_frase)
