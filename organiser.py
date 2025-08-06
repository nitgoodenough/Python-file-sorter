import os # Seperate
import shutil # Allow file moving

#path variables
pathway = r"C:\Users\NGURUNG2\OneDrive\OneDrive - JLR\Documents\VSCODE\Python\File sorter project\project_test_folder" # Variable holds location
list_pathway = os.listdir(pathway) # Read the contents of the directory into a list for processing
images_dest = r"C:\Users\NGURUNG2\OneDrive\OneDrive - JLR\Documents\VSCODE\Python\File sorter project\images_holder"
zip_dest = r"C:\Users\NGURUNG2\OneDrive\OneDrive - JLR\Documents\VSCODE\Python\File sorter project\zip_holder"
txt_dest = r"C:\Users\NGURUNG2\OneDrive\OneDrive - JLR\Documents\VSCODE\Python\File sorter project\txt_holder"

print(list_pathway) # shows original content

for file in list_pathway: # Initiate loop
    destination_folder = None
    name, type = os.path.splitext(file) # File seperated into the name and extension (EXT used later to seperate)
    source_path = os.path.join(pathway, file) # Original location of files set as source. Joined the file to the pathway.
    
    if type in [".jpg", ".png"]: # Extension check conditionals
         destination_folder = images_dest
    elif type == ".zip":
         destination_folder = zip_dest
    elif type == ".txt":
         destination_folder = txt_dest
    
    if destination_folder is not None:
         os.makedirs(destination_folder, exist_ok=True)
         destination_path = os.path.join(destination_folder, file) # Final dest is the folder with the file inside of it.
         shutil.move(source_path, destination_path)
#Version 4