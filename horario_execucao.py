from datetime import datetime
import pytz
import time

HORARIO_FUNCIONAMENTO = {
    'ole': ('07:00', '22:00'),
    'bradesco': ('07:00', '22:00'),
    'bmg': ('07:00', '22:00'),
    'safra': ('07:00', '22:00'),
    'panamericano': ('07:00', '22:00'),
    'daycoval': ('07:00', '21:00'),  # 07h às 21h sab e dom 07h às 19h
    'daycoval_cartao': ('07:00', '21:00'),  # 07h às 21h sab e dom 07h às 19h
    'itau': ('07:00', '20:00'),  # 07h às 20h sab 07h às 19h
    'banrisul': ('07:00', '22:00'),
    'cetelem': ('07:00', '22:00'),
    'c6bank': ('07:00', '22:00'),
}

data_hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo'))
hora = int (data_hora_atual.hour)
minuto = int (data_hora_atual.minute)

#print (HORARIO_FUNCIONAMENTO['ole'])

