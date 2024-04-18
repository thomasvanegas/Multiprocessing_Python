# Importacion de paquetes, librerias y clases.
from multiprocessing import Queue, Process
import time

# Declaracion de la función Square().
def square (numbers, queue):
    for i in numbers:
        queue.put(i*i)
        
# Declaracion de la función Square().
def make_negative (numbers, queue):
    for i in numbers:
        queue.put(i*-1)
        
# Declaracion de la función Cube().
def cube (numbers, queue):
    for i in numbers:
        queue.put(i*i*i)

# Declaracion de la función add_one().
def add_one (numbers, queue):
    for i in numbers:
        queue.put(i + 1)

# Instanciando la clase Queue -> FIFO
queue_1 = Queue()
nums = range(1, 8) # 1 al 7 == [1, 7] Intervalo

# Instanciando (creando) procesos
process_1 = Process(target=square, args=(nums, queue_1))
process_2 = Process(target=make_negative, args=(nums, queue_1))
process_3 = Process(target=cube, args=(nums, queue_1))
process_4 = Process(target=add_one, args=(nums, queue_1))

# Inicializacion de los procesos.
process_1.start()
process_2.start()
process_3.start()
process_4.start()

# Esperar a la finalizacion de los procesos.
process_1.join()
process_2.join()
process_3.join()
process_4.join()

# Extraccion de los argumentos
while not queue_1.empty():
    print(queue_1.get())