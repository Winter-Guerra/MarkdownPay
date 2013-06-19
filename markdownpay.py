#/bin/python

import sys
import argparse
import os.path

# *******************************************
# CC-BY-SA Winter Guerra (XtremD), June 2013.
# *******************************************

#
# This program will use the commandline to keep track of hours a programmer has worked, while also creating simple user-defined Markdown invoices for freelance work.
# This program should have two states for invoice creation:
#   1. Print out a simple invoice with the rates and total hours spent.
#   2. Print out a detailed outline that adds a separate collection of sheets that also list the individual work sessions, hours, work session topics, and summaries of related git commits. 
     
     
#ARGS:
#    Action - 
#        Clockin
#        Clockout 
#        Invoice - Optionally takes a second arg: "--Simple" or "--Detailed"
#        Config
# *******************************************

# Define global variables
globalConfigURL = "~/.markdownpay/"

    
def main():
    
    print 'Hello World!'
    
    # Get commandline args
    parser = argparse.ArgumentParser(description='MarkdownPay -- Easily Track, Calculate, and Invoice Your Freelance Programming Time Using Markdown PDF Invoices.')
    # Get Version Switch
    parser.add_argument('--v', action='version', version='%(prog)s v0.1 ALPHA')
    
    subparsers = parser.add_subparsers()
    
     # create the parser for the "action" command
    parser_clockin = subparsers.add_parser('clockin')
    parser_clockin.set_defaults(clockin=True)
    parser_clockout = subparsers.add_parser('clockout')
    parser_clockout.set_defaults(clockout=True)
    parser_invoice = subparsers.add_parser('invoice')
    parser_invoice.set_defaults(invoice=True)
    # Add options for invoices here
    parser_config = subparsers.add_parser('config')
    parser_config.set_defaults(config=True)

    args = parser.parse_args()
    
    print args
    
    if (hasattr(args, 'clockin')):
        print "--IN CLOCKIN"
    elif (hasattr(args, 'clockout')):
        print "--IN CLOCKOUT"
    elif (hasattr(args, 'invoice')):
        print "--IN INVOICE"
    elif (hasattr(args, 'config')):
        print "--IN CONFIG"
    
    # First, read the arguments we were passed.
    unpaidProgrammer = Programmer();
    
    masterBookkeeper = Bookkeeper();
    

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
        
# Keeps track of getting and saving boring things such the log files, the total hours worked, the total pay, taxes, other expenses, and detailed statistical breakdowns.
class Bookkeeper():
    
    configURL = globalConfigURL+"bookkeeper_Info.conf"
    
    # Constructor
    def __init__(self, currentFolderURL):
        
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
    
# This class is the actual one that makes the invoices        
class Typesetter():
    
    def getInvoiceTemplate():
        pass
        
    def typesetInformation():
        pass
        
    def typesetSimpleInvoice():
        pass
        
    def typesetDetailedInvoice():
        pass

# If the program is run from the commandline, run the main function 
if __name__ == '__main__':
    main()
    