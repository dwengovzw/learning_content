import os
from PIL import Image

# Set the path to the directory where you want to add the image
directory_path = '/home/idlab254/learning_content/'

# Set the name of the folder where you want to add the image
folder_name = 'embed'

# Set the path to the image file you want to add
image_path = '/home/idlab254/Pictures/22-10/dwengo.png'

# Open the image file
with Image.open(image_path) as img:

    # Loop through all the subdirectories and files in the specified directory
    for root, dirs, files in os.walk(directory_path):
        
        # Check if the current directory has the specified folder name
        if folder_name in dirs:
            
            # If it does, add the image to the folder
            img_path = os.path.join(root, folder_name, 'dwengo.png')
            img.save(img_path)

            # Print the path to the added image
            print(f'Added image to {img_path}')
