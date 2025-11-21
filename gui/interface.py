#Name: Kalia Hudson
#Date: 10-6-2025
#Program Name: Interface
#Program Description: This program allows the user to interact with the web
#scrapper through a GUI. Functions from the main.py file will be imported and
#bound to tkinter elements.

import tkinter as tk
from tkinter import ttk

class mainWindow:
    def __init__(self):
        
        self.scrapperWindow = tk.Tk()

        #Window background color
        self.scrapperWindow.configure(bg="#2f4f4f")

        #Window size
        self.scrapperWindow.geometry("600x500")

        #Title window
        self.scrapperWindow.title("Scrapper")

        #Label for URL entry field
        self.labelURL = tk.Label(self.scrapperWindow, text="Enter URL: ",bg="#2f4f4f")
        self.labelURL.place(x=15,y=15)

        #URL input field
        self.entryURL = tk.Entry(self.scrapperWindow)
        self.entryURL.place(x=80,y=15)

        #Label for access status
        self.labelStatus = tk.Label(text="Access Granted",font=("Helvetica",15),bg="#2f4f4f")
        self.labelStatus.place(x=15,y=55)

        #Label for HTML element options dropdown box
        self.labelElements = tk.Label(self.scrapperWindow, text="Searchables: ",bg="#2f4f4f")
        self.labelElements.place(x=225,y=15)
        
        #List of dropdown options
        options = ["p","h1","img"]
        
        #Combobox for elements
        self.tagBox = ttk.Combobox(self.scrapperWindow, values=options)
        self.tagBox.current(0)
        self.tagBox.place(x=230,y=40)

        #Button submit
        self.buttonSubmit = tk.Button(self.scrapperWindow, text="Submit",bg="#2f4f4f")
        self.buttonSubmit.place(x=335,y=15)

        #Label results section
        self.labelResults = tk.Label(self.scrapperWindow, text="Results:",bg="#2f4f4f")
        self.labelResults.place(x=15,y=100)

        #Tree results table
        self.tableResults = ttk.Treeview(self.scrapperWindow, columns=("Headers:"))
        self.tableResults.place(x=15,y=130)
                                    
        #Label export data
        self.labelExport = tk.Label(text="Export to CSV",bg="#2f4f4f")
        self.labelExport.place(x=425,y=315)

        #Button export
        self.buttonExport = tk.Button(text="Export",bg="#2f4f4f")
        self.buttonExport.place(x=425,y=340)

        #Function - creating a live window
        def run(self):
            self.scrapperWindow.mainloop()


#Function - getting the entered URL
def getURL(window):
    targetURL = window.entryURL.get()
    #TEST
    print("getURL ran - URL: ", targetURL)
    return targetURL

#FUNCTION - getting the selected tag
def getTag(window):
    targetTag = window.tagBox.get()
    print("getTag ran - Tag: ", targetTag)
    return targetTag
