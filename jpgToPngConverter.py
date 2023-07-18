import os
from PIL import Image
import shutil

def convert_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            try:
                # Convert JPG to PNG
                image = Image.open(input_path)
                output_path = os.path.splitext(output_path)[0] + ".png"
                image.save(output_path, "PNG")
                print(f"Converted '{file}' to PNG.")
            except IOError:
                print(f"Failed to convert '{file}'.")
        elif file.lower().endswith(".png"):
            try:
                # Copy PNG image directly
                shutil.copyfile(input_path, output_path)
                print(f"Copied '{file}' directly.")
            except IOError:
                print(f"Failed to copy '{file}'.")

# Example usage
input_folder = "Images"
output_folder = "Images"

convert_images(input_folder, output_folder)
