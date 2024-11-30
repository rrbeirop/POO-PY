cripto = "crip.txt"
descritor = open(cripto, "a")
pulo = 1
digitado = input("digite :")
new_frase = ''


for  i in digitado:
    new_frase += chr((ord(i)+pulo)%128)
    descritor.write(new_frase + "\n")
print(new_frase)


crpito = "crip.txt"  
descritor = open(crpito, "r")

new_frase = ''

for i in digitado:
    new_frase += chr((ord(i)-pulo)%128)
    
print(new_frase)


#digitado = input("letra:")
#print(f"Valor Deslocamento:{pulo}")
#print(f"Tabela: {ord(digitado)}")
#print(f"Soma (Deslocamento + Tabela){pulo + ord(digitado)}")
#print(f"Valor ultilizado %:{((pulo) + ord(digitado))%127}")

