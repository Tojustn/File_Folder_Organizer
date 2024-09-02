import schedule
import time
from datetime import datetime
from file_move import FolderByEndSorter,FolderAutomation
import os 
automation_tracker = {}
sepString = os.path.sep

# Change cwd to the user directory

os.chdir(os.path.expanduser("~"))
mp4Path = os.path.join(os.getcwd(),"Videos","mp4")
mp4Sort = FolderByEndSorter(mp4Path)

"""
Purpose: Function for all sorting objects
Parameters: None

Returns: Nothing
"""
def sort():
    mp4Sort.movefiles(".mp4",os.path.join(os.getcwd(),"Videos"))
schedule.every().day.at("12:00").do(sort)

ComSciPath = os.path.join(os.getcwd(),"Desktop","C++School")
ComSciFolderMaker = FolderAutomation(ComSciPath,7,10,"W",False)

"""
Purpose: Function for all folder automation objects
Parameters: None

Returns: Nothing
"""
def folderAutomation():
    ComSciFolderMaker.update_date_created()
    ComSciFolderMaker.createfolderandfile()


schedule.every(7).days.at("12:00").do(folderAutomation)


while True:
    time.sleep(1)