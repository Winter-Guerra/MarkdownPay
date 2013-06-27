#!/usr/bin/python

import os

# This class should only be really used for its information definitions such as name and stuff. Acts as a sort of high level wrapper for the accountant class.
class Programmer():
    
    configURL = "programmer_Info.conf"
    
    # Default constructor. No information was provided! Try to read the programmer's information from file.
    def __init__(self, config_Dir):
        
        # Get programmer's current working directory
        self.pwd = os.getcwd()
        
        # Get configuration file path
        self.config_Path = config_Dir + os.sep + configURL
        
        # Make a config reader to get our configuration
        self.config = configReader(self.config_Path)
        
        # Get our current project.
        self.project = project()
        
        # Make our current directory that of the project's git repo if it exists
        if (project.git_Repo != False):
            self.pwd = project.git_Repo
        
        # Open our current project's worksession log
        self.worksessionReader = worksessionReader(self.pwd)
        
    
    def getConfig(self, URL):
        
        config = {}
        # Open config file
        
        # For each line in file, walk through and find the values.
        self.info = config
    
    def startWorkunit():
        pass

    def endWorkunit():
        pass
        
    
    def requestInvoice(doDetailedInvoice):
        # Make an invoice regardless of anything else
        
        if (doDetailedInvoice == true):
            pass
        pass

# Keeps track of info regarding the programmer's current project. This mainly means it keeps track of the GIT repo location and commits.
class project():
    
    def __init__(self):
        
        # Find the project's git repo location
        self.git_Repo = self.get_Git_Repo()
        print 'Git Repo: '+self.git_Repo
        
        
    def get_Git_Repo(self):
        
        # Check if there is a git repo (.git/) somewhere upstream of our current directory. If we find one, use that as our present working directory instead
        search_Path = os.getcwd()
        search_Key = '.git'+os.sep
        print 'search key '+search_Key
        
        # Walk backwards
        files = os.listdir(search_Path)
        print 'Files: '+files
        while (hasattr(files, search_Key) == False):
            parent_Path = os.path.normpath(os.path.join(search_Path, os.path.pardir))
            # Give up searching if we have hit the system's root directory
            if (parent_Path == search_Path):
                # No git repo here!
                return False
            else:
                # Look inside of the parent path for a git repo
                search_Path = parent_Path
                files = os.listdir(search_Path)
                
        # We found a .git repo! Return that path as the programmer's current directory.
        return search_Path
        
    def get_Git_Commits(self, worksession):
        pass