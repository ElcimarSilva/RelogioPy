from datetime import datetime
import pytz
import time

class Computador:
    def __init__(self):
        self.marca = 'asus'
        self.memoria_ram = '8gb'
        self.placa_de_video = 'Nvidia'
    pass

computador1 = Computador()
#print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)

class Tempo:
    def __init__(self) -> None:
        self.data = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.minuto = self.data.minute
        self.hora = self.data.hour
        self.segundo = self.data.second

