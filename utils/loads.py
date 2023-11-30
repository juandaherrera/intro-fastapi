import json

json_path = 'data/movies.json'


def load_json_data(path: str = json_path):
    try:
        with open(path, 'r') as file:
            movies = json.load(file)
    except json.JSONDecodeError:
        print("Error al cargar el archivo JSON: el archivo está vacío o no está en formato JSON válido.")
        movies = {}

    return movies
