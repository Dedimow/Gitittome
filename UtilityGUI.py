import tkinter as tk
import shutil
import os
import time
from pathlib import Path

#create a dictionary for all source directory paths
sourcedirectorypaths = {'SkyStudio':'E:\SkyStudio Captures',
                        'PythonScripts':'E:\Python Scripts',
                        'Tester':'E:\TestingFolder'}

#create a dictionary for all destination directory paths
destdirectorypaths = {'TimeLapses':'D:\Captures\Time Lapse Dumps',
                        'PythonBackups':'D:\My Files\PythonBackups',
                        'TestDest': 'D:\My Files\TestDest' }

#initialize a variable for the source path
sourceloc = Path()

#initialize a variable for the dest path
destloc = Path()

#create a function that selects a folder path and places it into a variable as the source
def selectsource(btnname):
    sourceloc = sourcedirectorypaths[btnname]
    print(sourceloc)


#create a function that selects a folder path and places it into a variable as the destination
def selectdest(btnname):
    destloc = destdirectorypaths[btnname]
    print(destloc)


#initialize the interface environment
root = tk.Tk()

#define the size of the interface window
root.geometry('960x540')

#define a name for the window that opens
root.title("Ed's Sick Rocking Utilities")

#create label for source directory section
sourcelabel = tk.Label(root, text = "Source Directories").place(x=100,y=10)

#create button for Testing source folder
TestBtn = tk.Button  (root, 
                    text = "Tester",
                    width = 13,
                    bg = 'blue',
                    command = selectsource("Tester"))

TestBtn.place(x=40,y=85)

#create button for SkyStudio source folder
SkyBtn = tk.Button  (root, 
                    text = "SkyStudio",
                    width = 13,
                    bg = 'blue',
                    command = selectsource("SkyStudio"))

SkyBtn.place(x=40,y=55)

#create button for PythonScripts source folder
PythBtn = tk.Button  (root, 
                    text = "PythonScripts",
                    width = 13,
                    bg = 'blue',
                    command = selectsource("PythonScripts"))

PythBtn.place(x=145,y=55)

#create label for desination directory section
destlabel = tk.Label(root, text = "Destination Directories").place(x=700,y=10)

#create button for TimeLapse destination folder
TestDestBtn = tk.Button  (root, 
                    text = "TestDest",
                    width = 13,
                    bg = 'green',
                    command = selectdest("TestDest"))

TestDestBtn.place(x=663,y=85)


#create button for TimeLapse destination folder
TLBtn = tk.Button  (root, 
                    text = "TimeLapses",
                    width = 13,
                    bg = 'green',
                    command = selectdest("TimeLapses"))

TLBtn.place(x=663,y=55)

#create button for PythonBackups destination folder
PythBckBtn = tk.Button  (root, 
                    text = "PythonBackups",
                    width = 13,
                    bg = 'green',
                    command = selectdest("PythonBackups"))

PythBckBtn.place(x=768,y=55)

def copier():
    #initialize list for all files in source directory
    sourcelist = []

    #initialize list for all file paths in destination
    destlist = []

    #initialize list for all file names in destination
    namelist = []

    #walk function separates parts of path into 3 lists #TL = Time Lapse
    #     1. A string of the current folder's name
    #     2. A list of strings in the current folder
    #     3. A list of strings of the files in the current folder
    for TLDump, FolderNames, TLVideos in os.walk('D:\My Files\TestDest'):
        
        #make list of all file paths in destination folder
        for tls in TLVideos:
            
            #create full file path string and puts into temppath variable
            temppath = Path(Path(TLDump) / Path(tls))

            #add full file path as a path object to the destination list
            destlist.append(Path(temppath))

            #create list of just file names without paths
            namelist.append(temppath.name)

    #walk function separates parts of path into 3 lists
    #     1. A string of the current folder's name
    #     2. A list of strings in the current folder
    #     3. A list of strings of the files in the current folder  
    for SkyStudio, DateFolders, VideoFiles in os.walk('E:\TestingFolder'):
        
        #loop to evaluate all items in the VideoFiles list
        for avi in VideoFiles:
            
            #create full file path string and puts into temppath variable
            temppath = (Path(SkyStudio) / Path(avi))
            
            #add full file path as a path object to the source list
            sourcelist.append(Path(temppath))
    start = ()
    end = ()
    counter = 0
    #look at each item in the sourcelist i.e. the source directory
    for unit in sourcelist:
        
        #check all items in destlist
        for item in destlist:
                
                start = time.time()
                counter += 1
                #compare file names
                if Path(item).name is Path(unit).name:
                    
                    #determine size of the item in the sourcelist and compare to item size in destlist
                    if os.path.getsize(unit) > os.path.getsize(item):
                        
                        print("Dest" , Path(item).name)
                        print("Source" , Path(unit).name)

                        #copy larger file into
                        shutil.copy(unit , 'D:\My Files\TestDest')
                end = time.time()
                looptime = end - start
                print(counter, " - ", looptime)

        #determines if the file name is not in the destination folder
        if unit.name not in namelist:
                    
            #full file using the file path is copied from source to destination
            shutil.copy(unit , 'D:\My Files\TestDest')

            #filename is added to destlist
            #((for troubleshooting just in case))
            namelist.append(unit.name)  

ExecBtn = tk.Button(root, 
                    text = "Run that shit",
                    width = 13,
                    bg = 'orange',
                    command = copier)

ExecBtn.place(x = 450,y = 400)  
#set a loop for the interface to continue showing
root.mainloop()