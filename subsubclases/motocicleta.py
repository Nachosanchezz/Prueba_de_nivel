from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Bicicleta.__str__(self)+" {} km/h, {} cc".format(self.velocidad,self.cilindrada)
    
    def arrancar(self):
        return "Arrancando la motocicleta"
    
    def pedalear(self):
        return "No puedo pedalear, soy una motocicleta"