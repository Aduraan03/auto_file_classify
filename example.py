import os
import shutil

source_folder = 'Downloads/'
destination_folder = 'Reports/'

for filename in os.listdir(source_folder):
    if filename.endswith('.pdf'):
        new_name = 'report_' + filename
        shutil.move(source_folder + filename, destination_folder + new_name)