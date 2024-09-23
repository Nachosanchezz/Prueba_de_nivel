from subclases.coche import Coche

class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga=carga
    def __str__(self):
        return f'Camioneta(color={self.color},ruedas={self.ruedas},velocidad={self.velocidad},cilindrada={self.cilindrada},carga={self.carga})'
