#!/usr/bin/python

# This class should only be really used for its information definitions such as name and stuff. Acts as a sort of high level wrapper for the accountant class.
class Programmer():
    
    configURL = "programmer_Info.conf"
    
    # Default constructor. No information was provided! Try to read the programmer's information from file.
    def __init__(self):
        
        pwd = ""
        # This will fallback to user prompting if necessary
        config = self.getConfig(pwd)
        
        # Get programmer information from config.
        self.info = config
        
    
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