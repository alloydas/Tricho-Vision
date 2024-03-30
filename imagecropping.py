import os
from PIL import Image

# Input folder containing subfolders and images
# input_folder = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/  train"
input_folder = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/test"

# Output folder to save cropped images
# output_folder = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/crop512_50/train"
output_folder = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/crop512_50/test"

# Tile size and overlap
tile_size = 512
overlap = int(0.50 * tile_size)  # 25% overlap

# Function to crop an image into tiles
def crop_image(image, output_folder, filename):
    width, height = image.size
    x = 0
    image_number = 1
    while x + tile_size <= width:
        y = 0
        while y + tile_size <= height:
            tile = image.crop((x, y, x + tile_size, y + tile_size))
            tile_filename = f"{filename}_{image_number}.png"
            output_path = os.path.join(output_folder, tile_filename)
            tile.save(output_path)  # Save each tile
            y += tile_size - overlap
            image_number += 1
        x += tile_size - overlap

# Iterate through subfolders and process images
for root, dirs, files in os.walk(input_folder):
    for file in files:
        print(file)
        if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
            # Create subfolder structure in the output folder
            relative_path = os.path.relpath(root, input_folder)
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)

            # Load and crop the image
            input_image_path = os.path.join(root, file)
            image = Image.open(input_image_path)

            # Crop and save images
            filename, ext = os.path.splitext(file)
            crop_image(image, output_subfolder, filename)

print("Images have been cropped and saved into the output folder with the same subfolder structure and renamed with numbers.")
