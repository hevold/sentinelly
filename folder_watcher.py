import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, directory_to_watch, callback):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.event_handler = Handler(callback)  # Oppdaterer dette for å bruke callback
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            self.callback(event.src_path)

def start_watching(directory, callback):
    w = Watcher(directory, callback)
    w.run()
