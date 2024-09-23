from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta


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

    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtraos = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtraos)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtraos:
                print(v)
        else:
            for v in vehiculos:
                print(v)

    catalogar(vehiculo)
    catalogar(vehiculo, 0)
    catalogar(vehiculo, 2)
    catalogar(vehiculo, 4)
        


