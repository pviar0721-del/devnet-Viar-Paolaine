"""
Module 2 — Activity: File Sorting with os and shutil
Student: Viar, Paolaine Esther M.
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built an automated file organizer script in Python. It asks the user for a target folder path, 
scans all files inside that folder, creates subfolders for different file types (images, documents, 
videos, and others), and automatically moves each file into its matching subfolder based on its file 
extension.


============================================
KEY VOCABULARY
============================================
- os module: A built-in Python module used to interact with the operating system, navigate directories, and check file existence
- shutil module: A Python utility module used for high-level file operations, such as copying and moving files between directories
- file path: The specific address or location of a file or folder in the computer's directory structure
- directory: A folder on a computer used to store and organize files and subdirectories
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

users = input("What is your folder path? ")

if os.path.exists(users):
    print("Proceed to Next Step")

    file = os.listdir(users)
    image = 0
    documents = 0 
    videos = 0
    others = 0

    print(file)

    for file in [image, documents, videos, others]:
        if not os.path.exists(file):
            os.mkdir(file)

    for items in file:
        users = os.path.exists(users)

        print (file)
    
else:
    print("Error")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A mistake I made initially was that the files didn't sort well because I didn't include a proper loop 
to iterate through all items in the directory. Without a loop (for file in os.listdir(...)), the script 
only attempted to process a single item or check if the folder existed, leaving all the other files unsorted 
in the main folder.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
