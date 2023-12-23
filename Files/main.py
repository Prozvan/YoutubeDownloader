from YTsearch import getLink
from Dwn import downloadMusic
from tkinter import filedialog
import tkinter as tk

 
#so the filedialog.askdirectory works
root = tk.Tk()
root.withdraw()


def Type(QUERY):
    if "youtu.be" in QUERY or "www.youtube.com" in QUERY: return "1"
    else: return "2"


print()
print()
print("\t\t\tWelcome to Youtube Downloader!!")
print()
print()

QUERY = input("Enter a Link/Name of the video: ")
OPTION = Type(QUERY)
print()
FORMAT = input("For MP3 => 1, for MP4 (Max: 720p)=> 2: ")
print()



if FORMAT == "1" or FORMAT == "2":
    if OPTION == "1":

        DIR = filedialog.askdirectory(title="Select a directory")
        print("\t\t\tDownloading to: "+DIR)
        print()
        print("Downloading...")
        print()

        downloadMusic(DIR, QUERY, FORMAT)


    elif OPTION == "2":
        LINK = getLink(QUERY)
        
        DIR = filedialog.askdirectory()
        print("\t\t\tDownloading to: "+DIR)
        print()
        print("Downloading...")
        print()
        downloadMusic(DIR, LINK, FORMAT, QUERY)

    else:
        raise ValueError("There is no other option!")
    
    print()
    input("Press Enter to exit... ")
    print()

else:
    raise ValueError("There is no other format!")




