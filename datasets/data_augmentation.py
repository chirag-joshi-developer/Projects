import os
import random
import numpy as np
from PIL import Image, ImageFilter, ImageOps
import torchvision.transforms as T
import torchvision.transforms.functional as F
from PIL.Image import Resampling  # For BICUBIC

def random_zoom(image, zoom_range=(0.9, 1.1)):
    w, h = image.size
    scale = random.uniform(*zoom_range)
    new_w, new_h = int(scale * w), int(scale * h)
    image = image.resize((new_w, new_h), Resampling.BICUBIC)

    if scale < 1.0:
        delta_w = 256 - new_w
        delta_h = 256 - new_h
        padding = (
            delta_w // 2,
            delta_h // 2,
            delta_w - delta_w // 2,
            delta_h - delta_h // 2,
        )
        image = ImageOps.expand(image, border=padding, fill=(0, 0, 0))
        image = ImageOps.expand(image, border=padding, fill=(0, 0, 0))
    else:
        image = F.center_crop(image, [256, 256])
    return image

def apply_random_zoom(input_folder, output_folder="aug_zoom"):
    os.makedirs(output_folder, exist_ok=True)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            aug_img = random_zoom(img)
            aug_img.save(os.path.join(output_folder, img_file))

def apply_random_rotation(input_folder, output_folder="aug_rotate"):
    os.makedirs(output_folder, exist_ok=True)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            angle = random.uniform(-15, 15)
            rotated = F.rotate(img, angle, fill=[0, 0, 0])
            rotated = rotated.resize((256, 256), Resampling.BICUBIC)
            rotated.save(os.path.join(output_folder, img_file))

def apply_random_flip(input_folder, output_folder="aug_flip"):
    os.makedirs(output_folder, exist_ok=True)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            if random.random() > 0.5:
                img = F.hflip(img)
            img.save(os.path.join(output_folder, img_file))


def apply_brightness_contrast(input_folder, output_folder="aug_bright_contrast"):
    os.makedirs(output_folder, exist_ok=True)
    transform = T.ColorJitter(brightness=0.2, contrast=0.2)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            aug_img = transform(img)
            aug_img.save(os.path.join(output_folder, img_file))

def apply_random_crop(input_folder, output_folder="aug_crop"):
    os.makedirs(output_folder, exist_ok=True)
    crop_size = int(256 * 0.9)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            cropped = F.center_crop(img, [crop_size, crop_size])
            resized = cropped.resize((256, 256), Resampling.BICUBIC)
            resized.save(os.path.join(output_folder, img_file))

def apply_color_jitter(input_folder, output_folder="aug_colorjitter"):
    os.makedirs(output_folder, exist_ok=True)
    transform = T.ColorJitter(saturation=0.2, hue=0.02)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            aug_img = transform(img)
            aug_img.save(os.path.join(output_folder, img_file))

def apply_gaussian_noise(image, mean=0, std=5):
    np_img = np.array(image).astype(np.float32)
    noise = np.random.normal(mean, std, np_img.shape)
    noisy_img = np.clip(np_img + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_img)

def apply_blur_or_noise(input_folder, output_folder="aug_noise"):
    os.makedirs(output_folder, exist_ok=True)
    for img_file in os.listdir(input_folder):
        if img_file.lower().endswith(('jpg', 'png', 'jpeg')):
            img = Image.open(os.path.join(input_folder, img_file)).convert('RGB')
            if random.random() > 0.5:
                img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
            else:
                img = apply_gaussian_noise(img)
            img.save(os.path.join(output_folder, img_file))

apply_random_zoom(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_random_rotation(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_random_flip(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_brightness_contrast(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_random_crop(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_color_jitter(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")
apply_blur_or_noise(r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256\videocon_d2h_antenna")

