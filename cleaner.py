import os
import shutil
directory = "C:\\Users\\shiva\\OneDrive\\Programming" # Change this to your directory
deleteDirectory = "node_modules" # Directory to be deleted #build
for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        if(subdirectory == deleteDirectory):
            print(f'Deleting {os.path.join(root, subdirectory)}')
            shutil.rmtree(os.path.join(root, subdirectory),ignore_errors=True)
           # print("Build directory deleted!")
