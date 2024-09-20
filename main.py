from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta

# main.py

if __name__ == "__main__":
    mi_vehiculo1 = Coche("Rojo",4,180,2000)
    print(mi_vehiculo1)
    mi_vehiculo2 = Bicicleta("Azul", 2,"Deportiva")
    print(mi_vehiculo2)
    mi_vehiculo3 = Camioneta("Blanca", 6,120,1000,5000)
    print(mi_vehiculo3)
    mi_vehiculo4 = Motocicleta("Negra", 2,"Yamaha", 220, 1000)
    print(mi_vehiculo4)