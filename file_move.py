import os, shutil
from datetime import datetime, timedelta
    
    

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
        self.automated_archive = []

    """
    Purpose: Create folders based on iterations
    Parameters: self

    Returns: Nothing
    """
    def createfolderandfile(self):
        files_created = []
        if self.name_iterations:
                file_path = os.path.join(self.path,name)
                # Keeps Track of Iteartion Amount 
                
                if self.current_iteration <= self.num_iterations:
                    
                    # Sets iteration amount to end of string
                    name = str(self.name) + str(int(self.current_iteration) + 1)
                    os.makedirs((file_path),exist_ok=True)
                    files_created.append(file_path)
                    self.current_iteration += 1
                    return files_created

        else:
            os.makedirs(os.path.join(self.path,self.name),exist_ok=True)
            files_created.append(os.path.join(self.path,self.name))


    """
    Purpose: Remove files after specfic intervals
    Parameters: self

    Returns: Nothing
    """
    def removefiles(self):
        files_deleted = []
        # Checks if user wants to delete file after 4 months 
        if self.delete_after == True:
            file_path = ""
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
                    files_deleted.append(file_path)
            return files_deleted
        else: 
            # Redundant just for visual 
            pass

        def folderArchive(self):
            created = self.createfolderandfile()
            for path in created:
                self.automation_tracker[datetime.now()] = "File created at " + path
            
            recent_five = list(self.automation_tracker.values())[-5:]
            for sort in recent_five:
                print(sort)