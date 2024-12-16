import os
from bs4 import BeautifulSoup

years = [str(year) for year in range(2016, 2024)]

for year in years:
    # Procesar archivo HTML correspondiente al año
    html_file = f"{year}.html"
    folder_path = f"./{year}/"

    if not os.path.exists(html_file):
        print(f"El archivo {html_file} no existe. Continuando...")
        continue

    if not os.path.exists(folder_path):
        print(f"La carpeta {folder_path} no existe. Continuando...")
        continue

    # Leer y parsear el archivo HTML
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Obtener todos los links del archivo
    links = soup.find_all('a', href=True)

    # Obtener los nombres de los archivos dentro de la carpeta del año
    html_files_in_folder = {os.path.splitext(f)[0]: f for f in os.listdir(folder_path) if f.endswith('.html')}

    for link in links:
        href = link['href']

        # Buscar coincidencia entre href y los archivos en la carpeta
        for file_name, full_file_name in html_files_in_folder.items():
            if file_name in href:
                # Reemplazar el href con la ruta correcta
                link['href'] = f"./{year}/{full_file_name}"
                break

    # Guardar los cambios en el archivo HTML
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Archivo {html_file} procesado correctamente.")