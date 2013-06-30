#!/usr/bin/python


# Accesses the configuration files, scrapes data from the files, and returns values such.

# *******************************************
# CC-BY-SA Winter Guerra (XtremD), June 2013.
# *******************************************

# An object that will read and manipulate worksession logs. Reuses and extends some attributes of the ConfigReader class.
# TODO: Check the notation for inheritance!
class WorksessionReader():
    worksession_Default_FileURL = 'worksessions.log'
    
    # Constructor
    def __init__(self, presentWorkingDirectory):
        # Find the worksession log URL
        self.worksession_URL = presentWorkingDirectory + worksession_Default_FileURL
        
        # Get the entire worksession file (in a line-by-line array)
        super.openConfig(self.worksession_URL)
        
        pass
        
    def getWorksessions():
        pass
    