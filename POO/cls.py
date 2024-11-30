
class Base():
     marca = ''
     modelo= ''
     ano = 1950
     cor = ''

class Carro(Base):
  
    status_motor=False
    velocidade = 0

    def __init__(self,_marca,_modelo,_ano,_cor):
      self.marca = _marca
      self.modelo = _modelo
      self.ano = _ano
      self.cor=  _cor


    def  ligar_motor(self):
        print("motor ligado!")
        self.status_motor= True
    
    def desligar_motor(self):
        print("motor desligado!")
        self.status_motor = False
    
    def status_motor_painel(self):
        print("carro acelerando")
        print(self.status_motor)

    def acelerar(self):
        if self.status_motor!= False:
            print("Acelerando")
        else:
            print("Carro Desligado")
