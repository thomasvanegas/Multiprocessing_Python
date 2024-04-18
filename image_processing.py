# Importación de librerias, paquetes y clases.
from multiprocessing import Pool, cpu_count
from PIL import Image, ImageFilter
import time
import os

# Definicion del archivo de entrada
input_dir = 'val2017/' # => ruta relativa al directorio multiprocessing
output_dir = 'processed_images/'

# Declaración del método processing
def processing(file):
    image = Image.open(input_dir + file)
    image = image.filter(ImageFilter.GaussianBlur(2)) # Difuminar la imagen
    image = image.rotate(180, expand=True) # => Rotar la imagen a 180 grados (poner de cabezas)
    image = image.convert('L') # => Convertir la imagen a escala de grises
    image = image.transpose(Image.FLIP_LEFT_RIGHT)  # Espejo horizontal
    image.save(output_dir + file)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

list_files = os.listdir(input_dir)

# --- --- Procesamiento de imagenes secuencialmente --- ---
start = time.time()
for file in list_files: # => ciclo de 5000 iteraciones
    processing(file)

print(f'\n--- El tiempo total de la ejecución secuencial (SERIAL) fue de: {time.time()-start} segundos ---\n')


# --- --- Procesamiento de imagenes utilizando el MULTIPROCESSING o programación en PARALELO --- ---
num_cpus = cpu_count()

start_0 = time.time()

pool = Pool(num_cpus) # Se le entrega el número de CPUs disponibles en la máquina

pool.map(processing, list_files)
pool.close()
pool.join()

print(f'\n--- El tiempo total de la ejecución en PARALELO fue de: {time.time()-start_0} segundos---\n')