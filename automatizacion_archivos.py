import os
import shutil
from datetime import datetime
from folders_archivos import Folders as f #Class where are the folders paths

# Create folders if not exists
for folder in [f.pdf_folder, f.text_folder, f.excel_folder, f.image_folder, f.presentation_folder]:
    os.makedirs(folder, exist_ok=True)

# clissify origin files
for filename in os.listdir(f.download_folder):
    source_path = os.path.join(f.download_folder, filename)

    #skip if the archive is a folder
    if os.path.isdir(source_path):
        continue

    #Obtain the last updated date
    timestamp = os.path.getmtime(source_path)
    file_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    #Create new name with the date
    new_name = f"{file_date}_{filename}"


    #Clasify files into folders
    if filename.lower().endswith('.pdf'):
        destination_path = os.path.join(f.pdf_folder, new_name)

    elif filename.lower().endswith('.docx', '.txt'):
        destination_path = os.path.join(f.text_folder, new_name)

    elif filename.lower().endswith(('.xlsx', '.xls')):
        destination_path = os.path.join(f.excel_folder, new_name)

    elif filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        destination_path = os.path.join(f.image_folder, new_name)
    
    elif filename.lower().endswith(('.pptx')):
        destination_path = os.path.join(f.presentation_folder, new_name)

    else:
        continue  # Ignore other types

    # Move archive
    shutil.move(source_path, destination_path)
    print(f"Moved: {filename} -> {destination_path}")

