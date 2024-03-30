import os
import shutil

def sync_and_clean(src_folder, target_folder):
    # Store all paths from src_folder for comparison
    src_paths = set()
    for root, dirs, files in os.walk(src_folder):
        relative_path = os.path.relpath(root, src_folder)
        for file in files:
            src_paths.add(os.path.join(relative_path, file))

    # Sync files from src_folder to target_folder
    for root, dirs, files in os.walk(src_folder):
        relative_path = os.path.relpath(root, src_folder)
        target_path = os.path.join(target_folder, relative_path)

        # Create the directory in the target folder if it doesn't exist
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        for file in files:
            src_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_path, file)

            # Copying or replacing the file
            shutil.copy2(src_file_path, target_file_path)

    # Delete files in target_folder that are not in src_folder
    for root, dirs, files in os.walk(target_folder):
        relative_path = os.path.relpath(root, target_folder)
        for file in files:
            if os.path.join(relative_path, file) not in src_paths:
                os.remove(os.path.join(root, file))

# Specify your folder paths here
folderA = '/media/cvpr/Expansion/old_hair/data/train'
folderB = '/media/cvpr/Expansion/old_hair/data/in_one_folder/Family/train'

# Sync files from FolderA to FolderB and remove non-matching files
sync_and_clean(folderA, folderB)

print("FolderB is now synchronized with FolderA, and extra files have been removed.")
