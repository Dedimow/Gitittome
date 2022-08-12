import tkinter as tk
import tkinter.messagebox as mb
import shutil
import os
import time
from pathlib import Path

#create a dictionary for all source directory paths
sourcedirectorypaths = {'SkyStudio':r'E:\SkyStudio Captures',
                        'PythonScripts':r'E:\Python Scripts',
                        'Tester':r'E:\TestingFolder'}

#create a dictionary for all destination directory paths
destdirectorypaths = {'TimeLapses':r'D:\Captures\Time Lapse Dumps',
                        'PythonBackups':r'D:\My Files\PythonBackups',
                        'TestDest': r'D:\My Files\TestDest' }

#initialize a variable for the source path
sourceloc = Path()

#initialize a variable for the dest path
destloc = Path()

#initialize the interface environment
root = tk.Tk()

#define the size of the interface window
root.geometry('960x540')

#define a name for the window that opens
root.title("Ed's Sick Rocking Utilities")

#create a function that selects a folder path and places it into a variable as the source
def selectsource(btnname):
    global sourceloc
    sourceloc = sourcedirectorypaths[btnname]
    tk.Label (root, text = '{}{}{}'.format("Source to Copy"," = ", sourceloc)).place(x=100,y=500)
    mb.showinfo("Files in source",os.listdir(sourceloc))

#create a function that selects a folder path and places it into a variable as the destination
def selectdest(btnname):
    global destloc
    destloc = destdirectorypaths[btnname]
    tk.Label (root, text = '{}{}{}'.format("Destination to Receive Files"," = ", destloc)).place(x=700,y=500)
    mb.showinfo("Files in destination",os.listdir(destloc))

#create label for source directory section
sourcelabel = tk.Label(root, text = "Source Directories").place(x=100,y=10)

#create button for Testing source folder
TestBtn = tk.Button  (root, 
                    text = "Tester",
                    width = 13,
                    bg = 'blue',
                    command=lambda : selectsource("Tester"))

TestBtn.place(x=40,y=85)

#create button for SkyStudio source folder
SkyBtn = tk.Button  (root, 
                    text = "SkyStudio",
                    width = 13,
                    bg = 'blue',
                    command =lambda: selectsource("SkyStudio"))

SkyBtn.place(x=40,y=55)

#create button for PythonScripts source folder
PythBtn = tk.Button  (root, 
                    text = "PythonScripts",
                    width = 13,
                    bg = 'blue',
                    command =lambda: selectsource("PythonScripts"))

PythBtn.place(x=145,y=55)

#create label for desination directory section
destlabel = tk.Label(root, text = "Destination Directories").place(x=700,y=10)

#create button for TimeLapse destination folder
TestDestBtn = tk.Button  (root, 
                    text = "TestDest",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("TestDest"))

TestDestBtn.place(x=663,y=85)


#create button for TimeLapse destination folder
TLBtn = tk.Button  (root, 
                    text = "TimeLapses",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("TimeLapses"))

TLBtn.place(x=663,y=55)

#create button for PythonBackups destination folder
PythBckBtn = tk.Button  (root, 
                    text = "PythonBackups",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("PythonBackups"))

PythBckBtn.place(x=768,y=55)

def copier():
    #initialize list for all files in source directory
    sourcelist = []

    #initialize list for all file paths in destination
    destlist = []

    #initialize list for all file names in destination
    namelist = []

    #make list of all file paths in destination folder
    for x in os.listdir(destloc):
            
        #create full file path string and puts into temppath variable
        temppath = Path(Path(destloc) / Path(x))
        #print(temppath)
        #add full file path as a path object to the destination list
        destlist.append(Path(temppath))

        #create list of just file names without paths
        namelist.append(temppath.name)

    #loop to evaluate all items in the source location
    for y in os.listdir(sourceloc):

        #create full file path string and puts into temppath variable
        temppath = (Path(sourceloc) / Path(y))

        #print(temppath)

        #if str(temppath).endswith('.*') or str(temppath).endswith('.csv') or str(temppath).endswith('.py') or str(temppath).endswith('.git'):
        if (not '.git' in str(temppath)) and ('.' in str(temppath)):

            print(temppath)      
            #add full file path as a path object to the source list
            sourcelist.append(Path(temppath))

        elif not '.git' in str(temppath): 

            for x in os.listdir(temppath):
                
                newtemppath = (Path(temppath) / Path(x))
                print(newtemppath)
                sourcelist.append(Path(newtemppath))



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
                    if os.path.getsize(Path(unit)) > os.path.getsize(Path(item)):
                        
                        print("Dest" , Path(item).name)
                        print("Source" , Path(unit).name)

                        #copy larger file into
                        shutil.copy(unit , destloc)
                        destlist.append(unit)
                end = time.time()
                looptime = end - start
                #print(counter, " - ", looptime)

        #determines if the file name is not in the destination folder
        if unit.name not in namelist:
                    
            #full file using the file path is copied from source to destination
            shutil.copy(unit , destloc)
            destlist.append(unit)

            #filename is added to namelist
            #((for troubleshooting just in case))
            namelist.append(unit.name)  
    
    if destlist == sourcelist:
        fromto = '{}{}{}{}'.format("From ", sourceloc," to ",destloc)
        mb.showinfo("All files copied!", fromto )
    
    if destlist != sourcelist:
        fromto = '{}{}{}{}'.format("From ", sourceloc," to ",destloc)
        mb.showinfo("No copies made!", fromto )

ExecBtn = tk.Button(root, 
                    text = "Run that shit",
                    width = 13,
                    bg = 'orange',
                    command = copier)

ExecBtn.place(x = 450,y = 400)

#set a loop for the interface to continue showing
root.mainloop()