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
- os module:
- shutil module:
- file path:
- directory:
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
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
