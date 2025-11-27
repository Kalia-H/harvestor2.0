#Name: Kalia Hudson
#Date: 11-26-2025
#Program Name: writeCSV
#Program Description: This program handles the logic for writing 
#extracted data to a CSV file as well as saving the file
#to the user's desired location.

import csv
import tkinter as tk
from tkinter import filedialog

#CLASS: creating the saveAs window
class fileWindow():
    def __init__(self):

        ####TEST
        print("fileWindow instance created")

        fileWindow.file_path = filedialog.asksaveasfilename(
            title="Save your file",
            defaultextension=".csv"
        )

def write_to_csv(data, filePath):
    #creating and opening a new csv file
    with open(filePath, mode='w', newline='') as file:
        writer = csv.writer(file)

        #writing the header row
        writer.writerow(['Extracted Data'])

        ####TEST
        print("writeCSV opened.. passed data: ")
        print(data)
        
        #writing the extracted data rows
        for item in data:
            writer.writerow([item])


