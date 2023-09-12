import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#from_dir = "INGRESA LA RUTA DE LA CARPETA DESCARGAS (UTILIZA " / ") en VSC"
#to_dir = "INGRESA LA RUTA DE LA CARPETA DESTINO(UTILIZA " / ") en VSC"

from_dir = "C:/Users/ivann/Downloads"
to_dir = "C:/Users/ivann/Desktop/Fotos"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif', '.webp'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "Audio_Files":['.mp3']
}

# Clase event handler 

class FileMovementHandler(FileSystemEventHandler):

    # Actividad del alumno 1

    

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
        #print(event)
        #print(event.src_path)
                print("descargando archivo " + file_name)
                path1 = from_dir + "/" + file_name 
                path2 =to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name

                time.sleep(3)

                if os.path.exists(path2):
                    print("El directorio existe....")
                    print("moviendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("creando directorio....")
                    os.makedirs(path2)
                    print("moviendo" + file_name + "....")
                    shutil.move(path1,path3)
                    time.sleep(1)

# Inicia la clase event handler
event_handler = FileMovementHandler()


# Inicia Observer
observer = Observer()

# Programa el Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicia el Observer
observer.start()

# Actividad del alumno 2
try:
 while True:
    time.sleep(2)
    print("ejecutando...")
except KeyboardInterrupt:
    print("Detenido")
    observer.stop()



    
