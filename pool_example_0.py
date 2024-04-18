# Importación de librerias, paquetes y clases.
from multiprocessing import Pool, cpu_count
import time

# determinar el numero de procesadores
procesadores = cpu_count()

# Función que retorna el cubo de un número.
def cube(num):
    return num ** 3

# definicion de numbers.
numbers = range(100)

# Instanciamiento de la clase Poll.
pool = Pool() # Entregar como parámetros el numero de cpus

# pool.map(function, iterable)
start = time.time()
result = pool.map(cube, numbers)

# terminar pool
pool.close()

# esperar a que termine las operaciones con el pool para imprimir el resultado
pool.join()

print(f'\nNúmero de procesadores: {procesadores}\n')
print(result, f'\n\nTiempo total de la ejecución: {time.time() - start}\n')