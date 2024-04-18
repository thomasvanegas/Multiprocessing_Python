# Importacion de paquetes, librerias y clases.
import multiprocessing
import time

# Función count().
def count(num: int):
    cnt = 0
    for i in range(num):
        cnt += 1
        time.sleep(0.1) # argumento -> segundos
    print("--- Fin del CONTADOR ---")

# Análisis del algoritmo con ejecución serial.
start = time.time()

count(10)
count(15)
count(20)
count(25)

print("--- Tiempo de ejecución SERIAL: ", time.time()-start, " ---\n")

# Análisis del algoritmo con ejecución en multiprocesamiento.
start = time.time()

process_1 = multiprocessing.Process(target=count, args=[10])
process_2 = multiprocessing.Process(target=count, args=[15])
process_3 = multiprocessing.Process(target=count, args=[20])
process_4 = multiprocessing.Process(target=count, args=[25])

# Inicializacion de los procesos.
process_1.start()
process_2.start()
process_3.start()
process_4.start()

# Esperar la finalizacion de los procesos.
process_1.join()
process_2.join()
process_3.join()
process_4.join()

print("--- Tiempo de ejecución PARALELO: ", time.time()-start, " ---\n")