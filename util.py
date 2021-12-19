import os
import cv2

def split_image_types(image_names):
    ir_images, color_images = [], []
    image_range = len(image_names) // 2
    for img in image_names:
        if img[:image_range] == "C0":
            ir_images.append(img)
        else:
            color_images.append(img)
    return ir_images, color_images

def load_image(image_number, images_path, ir = True):
    ir_images, color_images = split_image_types(os.listdir(images_path))
    
    ir_image_path = os.path.join(images_path, ir_images[image_number])
    color_image_path = os.path.join(images_path, color_images[image_number])
    image = cv2.imread(ir_image_path if ir else color_image_path, cv2.IMREAD_GRAYSCALE if ir else cv2.IMREAD_COLOR)
    return image