import os
import cv2
import numpy as np
import random

def add_salt_and_pepper_noise(image, salt_pepper_ratio=0.3, amount=0.004):
    row, col, ch = image.shape
    num_salt = np.ceil(amount * image.size * salt_pepper_ratio)
    num_pepper = np.ceil(amount * image.size * (1.0 - salt_pepper_ratio))

    # Add Salt noise
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    image[coords[0], coords[1], :] = 1

    # Add Pepper noise
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    image[coords[0], coords[1], :] = 0

    return image

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)

                # Add salt and pepper noise
                noisy_image = add_salt_and_pepper_noise(image)

                # Construct output path and create directory if not exist
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, file)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Save the image
                cv2.imwrite(output_path, noisy_image)
                
                

# Specify your input and output directories
input_directory = './train'
output_directory = './train_salt_pepper'

process_directory(input_directory, output_directory)

def add_gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 10
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)

                # Add Gaussian noise
                noisy_image = add_gaussian_noise(image)

                # Construct output path and create directory if not exist
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, file)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Save the image
                cv2.imwrite(output_path, noisy_image)

# Specify your input and output directories
input_directory = './test'
output_directory = './test_gaussian'

process_directory(input_directory, output_directory)
