#!/usr/bin/python


# Keeps track of getting and saving boring things such the log files, the total hours worked, the total pay, taxes, other expenses, and detailed statistical breakdowns.
class Bookkeeper():
    
    defaultConfigURL = "bookkeeper_Info.conf"
    
    # Constructor
    def __init__(self, baseConfigURL, currentFolderURL):
        self.ConfigURL = baseConfigURL + defaultConfigURL
        self.bookFileLocation = currentFolderURL
        
    def openBookFile(bookFileURL):
        # Open and read the book file. Return an object that represents the opened file
        pass
    
    def getBookInformation(informationTag):
        pass
        
    def getGitInformation():
        pass
        
    def getSimpleInvoice():
        pass
    
    def getDetailedInvoice():
        pass
