#Name: Kalia Hudson
#Date: 10-27-25
#Program Name: Scrappy v2.0
#Program Description: This program allows a user to enter a website url and
#choose an html element to parse for. The results are then displayed on table
#within the gui window.
#File Description: This file holds the scrapper logic.

import requests
from bs4 import BeautifulSoup

#Function - Creating Headers
def createHeader (userAgent=None):
    #TEST
    print("createHeader ran")
    #creating header
    header = {
        "Accept": "application/json, text/html, */*",
        "Accept-Language": "en-US,en;1=0.9",
        "Referer": "https://google.com"
        }
    if userAgent == None :
        #assigning default user agent if no value is passed
        header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    else :
        header["User-Agent"] = userAgent
    return header

#validating url format
def validate_url(url):
    print("validate_url ran")
    if not url.startswith("https://"):
        print("Invalid URL")
        return False
    return True

#Function - FETCH (PROCESS ONE)
def fetch_html(enteredUrl, header):
    print("Fetch_html ran")
    #fetching the raw html
    response = requests.get(enteredUrl, headers = header)
    #saving status code
    code = response.status_code
    if code == 200:
        print("HTML response received")
        return response.text
    else:
        print("Error code : " + str(code) + " code")
        return code

#Function - PARSE (PROCESS TWO)
def parse_html(html):
    #creating parsable object
    soup = BeautifulSoup(html, "lxml")

    #Printing page title
    print("page title: ", soup.title.text.strip())

    return soup

#Function - EXTRACT (PROCESS THREE)
def extract_data(soup,tag):
    
    #extracting selected tags and save them in a list
    tags = soup.find_all(tag)
    
    #creating an empty list to hold the cleaned tags
    cleanedTags = []

    #creating a for loop to iterate through each tag in the tags list
    for tag in tags:
        #appending each cleaned tag to the cleanedTags list
        cleanedTags.append(tag.text.strip())

    return cleanedTags
        


