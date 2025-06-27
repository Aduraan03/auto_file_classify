import os
import shutil
from datetime import datetime
from folders_archivos import Folders  # Importar la clase, no la instancia

class OrganizadorArchivos:
    def __init__(self, folders):
        self.folders = folders
        self._crear_carpetas()

    def _crear_carpetas(self):
        for folder in [
            self.folders.pdf_folder,
            self.folders.text_folder,
            self.folders.excel_folder,
            self.folders.image_folder,
            self.folders.presentation_folder,
            self.folders.app_folder,
            self.folders.other_folder
        ]:
            os.makedirs(folder, exist_ok=True)

    def organizar(self):
        for filename in os.listdir(self.folders.download_folder):
            source_path = os.path.join(self.folders.download_folder, filename)

            if os.path.isdir(source_path):
                continue

            timestamp = os.path.getmtime(source_path)
            file_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            new_name = f"{file_date}_{filename}"

            destination_path = self._clasificar_archivo(filename, new_name)
            if not destination_path:
                continue

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {destination_path}")

    def _clasificar_archivo(self, filename, new_name):
        nombre = filename.lower()
        if nombre.endswith('.pdf'):
            return os.path.join(self.folders.pdf_folder, new_name)
        elif nombre.endswith(('.docx', '.txt')):
            return os.path.join(self.folders.text_folder, new_name)
        elif nombre.endswith(('.xlsx', '.xls')):
            return os.path.join(self.folders.excel_folder, new_name)
        elif nombre.endswith(('.jpg', '.jpeg', '.png')):
            return os.path.join(self.folders.image_folder, new_name)
        elif nombre.endswith('.pptx'):
            return os.path.join(self.folders.presentation_folder, new_name)
        elif nombre.endswith('.exe'):
            return os.path.join(self.folders.app_folder, new_name)
        elif nombre.endswith('.zip'):
            return os.path.join(self.folders.other_folder, new_name)
        else:
            return None

if __name__ == "__main__":
    folders = Folders()  # Crear instancia de Folders
    organizador = OrganizadorArchivos(folders)
    organizador.organizar()

