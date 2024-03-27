
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil 

#importing json for...
#importing shutil allows to do operations on file, such as copy, remove and create

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'sahil':
                new_name = filename
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i += 1
                    new_name = filename + str(i)
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)

                
                src = folder_to_track + '/' + filename
                new_name = folder_destination + '/' + new_name
                os.rename(src, new_name)

folder_to_track = '/Users/sahil/Desktop'
folder_destination = '/Users/sahil/Desktop/sahil'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()