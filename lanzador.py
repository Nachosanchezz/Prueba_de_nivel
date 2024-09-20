from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta
from superclases import vehiculo

def lanzador_main():
    vehiculo = []

    mi_vehiculo1 = Coche("Rojo",4,180,2000)
    vehiculo.append(mi_vehiculo1)
    print(mi_vehiculo1)
    
    mi_vehiculo2 = Bicicleta("Azul", 2,"Deportiva")
    vehiculo.append(mi_vehiculo2)
    print(mi_vehiculo2)
   
    mi_vehiculo3 = Camioneta("Blanca", 6,120,1000,5000)
    vehiculo.append(mi_vehiculo3)
    print(mi_vehiculo3)
    
    mi_vehiculo4 = Motocicleta("Negra", 2,"Yamaha", 220, 1000)
    vehiculo.append(mi_vehiculo4)
    print(mi_vehiculo4)

    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}" )
        for atributo, valor in vehiculo.__dict__.items():
            print(f"{atributo}: {valor}")
        print()

    catalogar(vehiculo)
        



