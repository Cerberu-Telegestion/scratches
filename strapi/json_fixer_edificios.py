import json

# Cargar el archivo JSON
json_path = "edificios.json"
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Obtener los nombres de los edificios desde la primera fila (las claves excepto "Unnamed: 0")
edificios_nombres = list(data[0].keys())[1:]

# Transformar los datos en una lista de objetos (edificios como filas)
edificios_lista = []
for nombre in edificios_nombres:
    edificio = {"nombre": nombre}
    for fila in data:
        clave = fila["Unnamed: 0"]
        valor = fila.get(nombre, None)  # Obtener el valor correspondiente al edificio
        edificio[clave] = valor
    edificios_lista.append(edificio)

# Guardar el JSON corregido
json_output_path = "edificios_transformados.json"
with open(json_output_path, "w", encoding="utf-8") as file:
    json.dump(edificios_lista, file, indent=4, ensure_ascii=False)

json_output_path
