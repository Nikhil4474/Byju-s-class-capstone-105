import os
import shutil

import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Nikhil/Downloads"
move_dir = "C:/Users/Nikhil/Downloads/Move_To"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#  User defined class

class FileMover(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloading....")

                path1 = from_dir + '/'+file_name
                path2 = move_dir + '/' + key
                path3 = move_dir+'/'+key+'/'+file_name

            if os.path.exists(path2):
                print("dict exists")
                print("Moving" + file_name+" ....")
                shutil.move(path1, path3)
                time.sleep(1)

            else:
                print("Making new dir...")
                os.makedirs(path2)
                print("Moving" + file_name+" ....")
                shutil.move(path1, path3)
                time.sleep(1)


eventHandler = FileMover()
myObserver = Observer()
myObserver.schedule(eventHandler, from_dir, recursive=True)
myObserver.start()

try:
    while True:
        time.sleep(1)
        print("Running....")

except KeyboardInterrupt:
    print("Stopping")
    myObserver.stop()
    print("Stopped")
