#!/usr/bin/python

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


import sys
import argparse
import os.path


import bookkeeper
import programmer
import typesetter
import configReader

# Define global variables
globalConfigURL = "~/.markdownpay/"

version = "ALPHA v0.1"

    
def main():
    
    args = getCommandlineArgs()
    
    print 'Arguments given:'
    print args
    
    unpaidProgrammer = programmer.Programmer(args.configFile)
    
    # Init the Bookkeeper with a config url (if any)
    masterBookkeeper = bookkeeper.Bookkeeper()
    
    
    if (args.action_Verb_Arg == 'clockin'):
        print "--IN CLOCKIN"
    elif (args.action_Verb_Arg == 'clockout'):
        print "--IN CLOCKOUT"
    elif (args.action_Verb_Arg == 'invoice'):
        print "--IN INVOICE"
    elif (args.action_Verb_Arg == 'config'):
        print "--IN CONFIG"
    
            
# Sets commandline listeners and returns the passed args.
def getCommandlineArgs():
    
    # Get commandline args
    parser = argparse.ArgumentParser()
    # Define switches that can be called no matter what.
    # version getter
    parser.add_argument('--v', action='version', version='%(prog)s -- ' + version)
    
    
    # Create listeners for the action verbs and their respective configuration flags
    subparsers = parser.add_subparsers(dest='action_Verb_Arg') 
    # Action: "clockin"
    parser_clockin = subparsers.add_parser('clockin', help='Start logging a work session\'s hours.')
    parser_clockin.set_defaults(clockin=True)
    # Action: "clockout"
    parser_clockout = subparsers.add_parser('clockout', help='Finish a work session and annotate it\'s description.')
    parser_clockout.set_defaults(clockout=True)
    # Action: "invoice"
    parser_invoice = subparsers.add_parser('invoice', help='Make a simple or detailed invoice of all unpaid work sessions. (Defaults to making a detailed invoice.)')
    parser_invoice.set_defaults(invoice=True)
    # Action: "config"
    parser_config = subparsers.add_parser('config', help='Probably a useless action flag')
    parser_config.set_defaults(config=True)
    
    
    # Switch for Overriding Config file location
    parser.add_argument('--configFile','--c', default='', help='Override the default configuration folder directory (currently '+globalConfigURL+')')
    
    # Return the args gotten
    args = parser.parse_args()
    return args


# If the program is run from the commandline, run the main function 
if __name__ == '__main__':
    main()
    