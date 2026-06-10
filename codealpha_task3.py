# task automation

import os
import shutil

source_folder = "source_images"
destination_folder = "moved_images"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move all JPG files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"{file} moved successfully!")

print("All JPG files have been moved.")