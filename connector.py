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
import writeCSV as write
from writeCSV import fileWindow
from gui.interface import mainWindow
import imageHandler as handler


#FUNCTION: displaying results onto gui
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

#FUNCTION - displaying images onto gui
def display_image_results(window, images):
    
    #####TEST
    print("display_image_results called succesfully")
    
    


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
    results = core.extract_data(site_soup, tag)
    
    #storing results into a windows attribute
    #this allows the extracted_list to be accessed throughout all functions through the activeWindow class in interface.py
    #created at runtime
    window.extracted_list = results
    
    ####TEST
    print(results)

    #checking the selected tag
    if (tag == "img"):
        #unpacking the treeview
        window.tableResults.place_forget()

        #calling the display_image_results function
        display_image_results(window, results)
    else:
        display_results(window, results)

#FUNCTION - handling submit button 
def onSubmit(window):
    ####TEST
    print("onSubmit ran")

    #calling full_operation to start the scraping pipeline
    full_operation(window)

#FUNCTION - handing export button
def onExport(window):
    #####TEST
    print("onExport:")
    print(window.extracted_list)

    #creating an instance of the fileWindow from writeCSV.py
    write.fileWindow()

    #calling write_to_csv from writeCSV.py
    export = write.write_to_csv(window.extracted_list, fileWindow.file_path)

#creating an instance of the mainWindow class from interface.py
activeWindow = mainWindow()

#adding a functionionality from engine.py to the submit button from interface.py
activeWindow.buttonSubmit.config(command=lambda: onSubmit(activeWindow))

#adding functionionality from writeCSV.py to the "export CSV" button from
#interface.py
activeWindow.buttonExport.config(command=lambda: onExport(activeWindow))




        
