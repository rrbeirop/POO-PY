# w - write. Gravar - Abre um arquivo para gravação, cria o arquivo se ele não existir
# a - append. Acrescentar - Abre um arquivo para anexar, cria o arquivo se ele não existir
# r - read. Ler - Abre um arquivo para leitura, erro se o arquivo não existir Valor padrão
# t " text - Valor padrão. Modo de texto
# x " creat - Cria o arquivo especificado, retorna um erro se o arquivo existir
# b "  binary -- Binário - Modo binário (por exemplo, imagens)

#lista = []
nome = "dados.txt"
valor_cripto =1
descritor = open(nome, "a")
frase = input("digite: " )
new_frase = ''

for letra in frase:
    new_frase += chr(ord(letra)+valor_cripto)
descritor.write(new_frase + "\n")

nome = "dados.txt"
descritor = open(nome, "r")
new_frase = ''
for letra in descritor.read():
    new_frase += chr(ord(letra)-valor_cripto)

print(new_frase)









