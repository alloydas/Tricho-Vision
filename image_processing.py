import pywt
import numpy as np
import cv2
import os
import shutil

source_dir = "data"
destination_dir = "processed_dataset"

for root, _, files in os.walk(source_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            relative_path = os.path.relpath(root, source_dir)
            # print(relative_path)
            destination_subfolder = os.path.join(destination_dir, relative_path)
            # print(destination_subfolder)
            os.makedirs(destination_subfolder, exist_ok=True)
            
            # image = Image.open(file_path)
            # Process the image as needed
            # processed_image = image.resize((new_width, new_height))
            # processed_image.save(destination_path)
            ip_image = cv2.imread(file_path, 0)
            backtorgb = cv2.cvtColor(ip_image,cv2.COLOR_GRAY2RGB)

            src_img = cv2.imread(file_path, 0)
     

            src_img_1 = src_img.astype('float')
            img_dct = cv2.dct(src_img_1)
            img_reconst = cv2.idct(img_dct)
            coeffs = pywt.dwt2(img_reconst, 'db3', mode = 'periodization')
            cA, (cH, cV, cD) = coeffs # Extracting coefficients

            imgr = pywt.idwt2(coeffs, 'db3', mode = 'periodization')


            imgr = np.uint8(imgr)
                 

            fft_output = np.fft.fft2(imgr)


            fft_reconst = np.fft.ifft2(fft_output)
                 

            destination_path = os.path.join(destination_subfolder, filename)
            # print(destination_path)
            # assert(0==1)
            cv2.imwrite(destination_path, np.abs(fft_reconst))



     
