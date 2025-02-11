import os
import json
import csv

# Ruta de la carpeta que contiene los archivos CSV
csv_folder_path = '/Users/david/Downloads/script subida edificios'

# Lista para almacenar los datos de los apartamentos
apartments_data = {}

# Obtener la lista de archivos CSV en la carpeta
csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]

# Procesar cada archivo CSV
for csv_file in csv_files:
    csv_file_path = os.path.join(csv_folder_path, csv_file)
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Leer la primera fila para obtener los identificadores de los apartamentos
        for i, apartment_identifier in enumerate(headers):
            if apartment_identifier:
                apartments_data[apartment_identifier] = {}
        for row in csv_reader:
            for i, apartment_identifier in enumerate(headers):
                if apartment_identifier and i < len(row):
                    key = row[0]
                    value = row[i+1]
                    apartments_data[apartment_identifier][key] = value

# Guardar los datos en un archivo JSON
output_file_path = 'apartamentos.json'
with open(output_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(apartments_data, json_file, ensure_ascii=False, indent=4)

print(f"Datos de apartamentos guardados en {output_file_path}")