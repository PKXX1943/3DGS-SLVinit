import os
import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy

def process_images(input_folder, output_folder, mean=0, sigma=25):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)

            if image is not None:
                noisy_image = add_gaussian_noise(image, mean, sigma)
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, noisy_image)
                print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    input_folder = '' 
    output_folder = '' 
    mean = 0 
    sigma = 25  
    process_images(input_folder, output_folder, mean, sigma)
