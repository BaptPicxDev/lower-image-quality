# Import
import os
from  PIL import Image


# Functions
def list_jpeg_files_within_input_folder(extension="jpg"):
    files = os.listdir("input_folder")
    return [
        os.path.join("input_folder", file)
        for file in files
        if file.endswith(extension)
    ]


def resize_image(image_path, max_resolution=2000):
    output_path = image_path.replace("input_folder", "output_folder")
    with Image.open(image_path) as img:
        # Get the current dimensions
        width, height = img.size
        print(f"Current size of {image_path} is ({width},{height}).")

        if (width > max_resolution):
            scale = max_resolution / width
            new_width = int(width * scale)
            new_height = int(height * scale)
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"file {output_path} created.")
            resized_img.save(output_path)
        elif (height > max_resolution):
            scale = max_resolution / height
            new_width = int(width * scale)
            new_height = int(height * scale)
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"file {output_path} created.")
            resized_img.save(output_path)

# Main thread
if __name__ == "__main__":
    print("Main thread.")
    for image_path in list_jpeg_files_within_input_folder():
        resize_image(image_path)
    for image_path in list_jpeg_files_within_input_folder(extension="jpeg"):
        resize_image(image_path)
