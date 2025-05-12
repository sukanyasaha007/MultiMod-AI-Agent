import os
from pathlib import Path
from shutil import copyfileobj

def save_upload_file(upload_file, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    destination = Path(destination_folder) / upload_file.filename
    with destination.open("wb") as buffer:
        copyfileobj(upload_file.file, buffer)
    return str(destination)
