import os
import zipfile
import shutil
from patterns import patterns_to_folders, patterns_to_circuits

def clasificar_setups(source_dir, iracing_setups_provider=""):
    if not os.path.exists(source_dir):
        print(f"ERROR: El directorio {source_dir} no existe.")
        return

    files = [f for f in os.listdir(source_dir) if f.endswith(".zip") or f.endswith(".sto")]

    if not files:
        print("No se encontraron archivos para clasificar.")
        return

    for file in files:
        file_path = os.path.join(source_dir, file)
        file_name_lower = file.lower()

        # Identificar coche
        car_folder = None
        for pattern, folder in patterns_to_folders.items():
            if pattern in file_name_lower:
                car_folder = os.path.join(source_dir, folder) + iracing_setups_provider
                break

        # Identificar circuito
        circuit_folder = None
        for pattern, circuit in patterns_to_circuits.items():
            if pattern in file_name_lower:
                circuit_folder = circuit
                break

        if car_folder:
            circuit_folder = circuit_folder if circuit_folder else "Desconocido"
            destination = os.path.join(car_folder, circuit_folder)
            try:
                os.makedirs(destination, exist_ok=True)

                if file.endswith(".zip"):
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(destination)
                elif file.endswith(".sto"):
                    shutil.copy(file_path, destination)
                print(f"Archivo {file} procesado y movido a {destination}.")
            except zipfile.BadZipFile:
                print(f"ERROR: {file} está corrupto. Saltando.")
            except Exception as e:
                print(f"ERROR: No se pudo procesar {file}. Detalles: {e}")
        else:
            print(f"No se encontró un patrón para {file}. Saltando.")

    print("Proceso completado.")
