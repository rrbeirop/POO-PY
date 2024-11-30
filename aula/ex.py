#X = int(input())
#Y = int(input())
#s = X + Y 
#print(s) 

A, B = map(float, input().split())
S =  A + B
M = S//2  

if M >=7:

    print('Aprovado')

elif M <7 and M >=4:
      print("Recuperacao")

else:
     print("Reprovado")