from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta

# main.py

if __name__ == "__main__":
    mi_vehiculo1 = Coche("azul",4,180,2000)
    print(mi_vehiculo1)
    mi_vehiculo2 = Bicicleta("Azul", "Montaña", "Azul","Deportiva")
    print(mi_vehiculo2)
    mi_vehiculo3 = Camioneta("Ford", "Fiesta",120, 1000)
    print(mi_vehiculo3)
    mi_vehiculo4 = Motocicleta("Negra", 2, 220, 1000)
    print(mi_vehiculo4)