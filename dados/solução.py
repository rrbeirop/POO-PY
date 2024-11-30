for salto in range(0,127):
    new_frase = ''
    descritor = open('dados.txt', 'r')
  

    for  l in descritor.read():
        if ord(l) +salto > 127:
            new_frase += chr((ord(l)+salto)%127)
        else:
            new_frase += chr((ord(l)+salto)%127)
    print(f'tentativa :[{salto}] : {new_frase}')

    save = open("resultados_conferencia.txt","a")
    save.write(new_frase)
    save.close()
    descritor.close()


    

