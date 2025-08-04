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
    name, type = os.path.splitext(file) # File seperated into the name and extension (EXT used later to seperate)
    source_path = os.path.join(pathway, file) # Original location of files set as source. Joined the file to the pathway.
    
    if type in [".jpg", ".png"]: # Extension check conditionals
         os.makedirs(images_dest, exist_ok=True) # Makes folder if it doesn't exist. Boolean prevents fileError
         destination_path = os.path.join(images_dest, file) # final destinations
         shutil.move(source_path, destination_path) # Source is moved to new path
    elif type == ".zip":
         os.makedirs(zip_dest, exist_ok=True)
         destination_path = os.path.join(zip_dest, file)
         shutil.move(source_path, destination_path)
    elif type == ".txt":
         os.makedirs(txt_dest, exist_ok=True)
         destination_path = os.path.join(txt_dest, file)
         shutil.move(source_path, destination_path)

#Version 1
#Make a new version which creates folders rather than using pre exisiting