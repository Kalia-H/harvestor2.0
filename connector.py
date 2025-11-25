#Name: Kalia Hudson
#Date: 11-2-25
#Program Name: Scrappy v2.0
#Program Description: This program allows a user to enter a website url and
#choose an html element to parse for. The results are then displayed on table
#within the gui window.
#File Description: This file connects engine.py and interface.py, calling
#functions and handling events.

import engine as core
import gui.interface as face
import tkinter as tk
import time
import threading

from gui.interface import mainWindow

def display_results(window, extractedList):
    #Using the Treeview widget from the passed window instance
    tree = window.tableResults

    #Clearing any existing rows
    for row in tree.get_children():
        tree.delete(row)

    for extract in extractedList:
        #Iterating through each extracted item
        if isinstance(extract, (list, tuple)):
            #If the item is a list or tuple, pass it directly 
            values = extract
        else:
            #If the item is a single value, wrap it in a one-element tuple
            values = (extract,)
        #inserting the extracted item into the treeview at the parent level
        tree.insert('', 'end', values=values)

#FUNCTION - Holds the logic flow        
def full_operation(window):
    #running createHeader function from engine.py to create and store the header
    header = core.createHeader()

    #running the getURL function from interface.py to gather the url from the user
    url = face.getURL(window)

    #running the getTag function from interface.py to gather the tag from the user
    tag = face.getTag(window)
    
    #storing url for validation
    is_valid = core.validate_url(url)

    #validating url
    if is_valid == False:
        #modifying url
        url = "https://" + url
        
        #####TEST
        print("New URL: " + url)
        
    #running fetch_html (process 1)
    #url, header
    raw_html = core.fetch_html(url,header)

    #running parse_html (process 2)
    #html
    site_soup = core.parse_html(raw_html)

    #extracting specific data (process 3)
    #soup, tag
    extracted_list = core.extract_data(site_soup, tag)

    ####TEST
    print(extracted_list)

    #running display_results
    display_results(window, extracted_list)

#Function - handling submit button 
def onSubmit(window):
    print("onSubmit ran")
    full_operation(window)

#creating an instance of the mainWindow class from interface.py
activeWindow = mainWindow()

#adding a functionionality from engine.py to the submit button from interface.py
activeWindow.buttonSubmit.config(command=lambda: onSubmit(activeWindow))




        
