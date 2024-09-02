import os, shutil
from datetime import datetime, timedelta
class FolderByEndSorter():
    def __init__ (self, endpath,):
        self.endpath = endpath

    
    """
    Purpose: Move files into designated endpath
    Parameters: self, end_of_file and path

    Returns: Nothing
    """
    def movefiles(self, end_of_file, path):
        if os.path.exists(path):
            for file in os.listdir(path):
                if file.endswith(end_of_file):
                    shutil.move(os.path.join(path, file),self.endpath)
        else: 
            print("The path doesn't exist")
    
    
    

class FolderAutomation():
    def __init__(self,path:str ,interval:int,num_iterations:int,name:str,delete_after:bool):
        self.path = path
        self.interval = interval
        self.num_iterations = num_iterations
        self.current_iteration = 0
        self.name = name
        self.date_created = datetime.now()
        self.delete_after = False
        self.name_iterations = True

    """
    Purpose: Create folders based on iterations
    Parameters: self

    Returns: Nothing
    """
    def createfolderandfile(self):
        if self.name_iterations:
                # Keeps Track of Iteartion Amount 
                self.current_iteration += 1
                if self.current_iteration <= self.num_iterations:
                    # Sets iteration amount to end of string
                    name = str(self.name) + str(int(self.current_iteration) + 1)
                    os.makedirs(os.path.join(self.path,name),exist_ok=True)
        else:
            os.makedirs(os.path.join(self.path,self.name),exist_ok=True)


    """
    Purpose: Remove files after specfic intervals
    Parameters: self

    Returns: Nothing
    """
    def removefiles(self):
        # Checks if user wants to delete file after 4 months 
        if self.delete_after == True:
            for file in os.listdir(self.path):
                # Gets file path 
                file_path = os.path.join(self.path,file)
                # Get the creation time of the file
                creation_time = os.path.getctime(file_path)

                # Convert creation time to a datetime object
                creation_datetime = datetime.fromtimestamp(creation_time)
                time_past = datetime.now() - creation_datetime

                # Checks if the datetime object is older then 120 days
                if time_past > timedelta(days=120):
                    # Removes file at path
                    os.unlink(file_path)
        else: 
            # Redundant just for visual 
            pass


        def update_date_created(self):
            self.date_created = datetime.now()  # Update the date_created to the current time
