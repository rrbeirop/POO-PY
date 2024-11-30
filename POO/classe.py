class Banco():
    pe = ''
    assento = ''
    pe_com_rodas = False
    def __init__(self, _pe, _assento):
    
        self.pe = _pe
        self.assento = _assento

       # super.__init__(_pe, _assento)
    
    def giratorio (self):
       self.pe_com_rodas = True

class Cadeira(Banco):
    encosto = ''
    def __init__(self, _encosto, _pe, _assento):
     self.encosto = _encosto
     self.pe = _pe
     self.assento = _assento
     super.__init__(_encosto, _pe, _assento)


banco = Banco ('ruim', 'duro')
banco_ = Banco ('horrivel', 'durasso')
print(banco.pe, banco.assento)
print(banco_.pe, banco.assento)

cadeira = Cadeira ("mole", "duro", "fofo")
print(cadeira.encosto, cadeira.pe, cadeira.assento)

#
#    def adicionar(self):
       
  #     if self.pe: False
   #    print("Adicionar ")

    




