from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os,shutil
import schedule
import time
from file_move import FolderAutomation
from datetime import datetime
"""
This class will work in tandem with observer manage files
"""
class downloadHandler(FileSystemEventHandler):
    def on_created(self,event):
        file_path = event.src_path
        file_dirname = os.path.dirname(file_path)
        # Gets base name of file
        file_base_name = os.path.basename(file_path)
        if not event.is_directory and file_base_name.endswith(".cpp") and file_dirname == os.path.join(os.path.expanduser("~"),"Downloads"):
            print(f"File is a .cpp file in downloads")
            try:
                shutil.move(file_path,os.path.join(os.path.expanduser("~"),"Desktop","CPP Files"))
                print(f"C++ File Moved")
            except Exception:
                print(f"error")
    def on_deleted(self,event):
        file_path = event.src_path
        print(f" File: {file_path} was deleted")

"""
Purpose: Handle files in my user video file
Parameters: FileSystemEventHandler

Returns: Nothing
"""
class videoHandler(FileSystemEventHandler):
    files_moved = []
    def on_created(self,event):
        file_path = event.src_path
        file_dirname = os.path.dirname(file_path)
        # Gets base name of file
        file_base_name = os.path.basename(file_path)
        file_path = os.path.join(os.path.expanduser("~"),"Videos")
        file_endpath = os.path.join(os.path.expanduser("~"),"Videos","mp4")
        if not event.is_directory and file_base_name.endswith(".mp4"):
            try:
                shutil.move(file_path,file_endpath)
                # Moves files in the video handler class
                videoHandler.files_moved.append((file_path,file_endpath,file_base_name))
                print(f"Mp4 Moved")
            except Exception:
                print("Exception")

if __name__ == "__main__":
    download_monitor = os.path.join(os.path.expanduser("~"),"Downloads")
    video_monitor = os.path.join(os.path.expanduser("~"),"Videos")

    #Created Observer object
    observer = Observer()

    ComSciPath = os.path.join(os.path.expanduser("~"),"Desktop","C++School")
    ComSciFolderMaker = FolderAutomation(ComSciPath,7,10,"W",False)
    ComSciFolderMaker.folderArchive()
    schedule.every(7).days.at("12:00").do(ComSciFolderMaker.folderArchive)

    download_handler = downloadHandler()
    video_handler = videoHandler()

    # Schedule the observer to monitor the specified path
    observer.schedule(download_handler, download_monitor, recursive=False)
    observer.schedule(video_handler, video_monitor, recursive=True)
    
    # Start the observer
    observer.start()

    try:
        while True:
            schedule.run_pending()
            # Keep the script running
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()