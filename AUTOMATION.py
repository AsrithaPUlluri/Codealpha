#Task 4:Task Automation with Python Scripts
#Python script for file organization
import os
import shutil

def organize_files_by_extension(directory):
    
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lstrip('.').lower()  # Remove the leading dot and convert to lowercase

        # Create a folder for the file extension if it doesn't exist
        ext_folder = os.path.join(directory, ext)
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

        # Move file to the corresponding folder
        shutil.move(filepath, os.path.join(ext_folder, filename))
        print(f"Moved: {filename} to {ext_folder}")

directory_to_organize = 'c:\\Users\\sweety\\OneDrive\\Desktop\\auto'  
organize_files_by_extension(directory_to_organize)
