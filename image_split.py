import os
import shutil
import random
from pathlib import Path

# Path to the main folder containing subfolders and images
main_folder_path = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/order"

# Path to train and test folders
train_folder_path = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/train"
test_folder_path = "/media/cvpr/Expansion/old_hair/data/in_one_folder/ORDER/test"

# Ratio for splitting images (70% for training, 30% for testing)
split_ratio = 0.7

# Function to split images and save them in train and test folders
def split_images(image_paths, folder_name):
    # Calculate the split index
    split_index = int(len(image_paths) * split_ratio)

    # Shuffle the images randomly
    random.shuffle(image_paths)

    # Split the images
    train_images = image_paths[:split_index]
    test_images = image_paths[split_index:]

    # Create train and test subdirectories within train and test folders
    train_subdir = os.path.join(train_folder_path, folder_name)
    test_subdir = os.path.join(test_folder_path, folder_name)
    os.makedirs(train_subdir, exist_ok=True)
    os.makedirs(test_subdir, exist_ok=True)

    # Move images to train and test subdirectories
    for image_path in train_images:
        shutil.copy(image_path, train_subdir)
    
    for image_path in test_images:
        shutil.copy(image_path, test_subdir)

# Function to get a list of image paths in a folder and its subfolders
def get_image_paths(folder_path):
    image_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                image_paths.append(os.path.join(root, file))
    return image_paths

# Get a list of all image paths in the main folder and its subfolders
all_image_paths = get_image_paths(main_folder_path)

# Split images and save them in train and test folders
for root, dirs, _ in os.walk(main_folder_path):
    for dir_name in dirs:
        print(dir_name)
        dir_path = os.path.join(root, dir_name)
        image_paths = get_image_paths(dir_path)
        split_images(image_paths, dir_name)

print("Images have been split and saved into train and test folders while maintaining subfolder structure.")
