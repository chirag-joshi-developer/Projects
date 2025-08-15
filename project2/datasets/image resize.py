import os
from PIL import Image

# Set input and output paths
input_dir = r"E:\1581-Chirag-Joshi-II\datasets\custom dataset"
output_dir = r"E:\1581-Chirag-Joshi-II\datasets\processed_data_256"

target_size = (256, 256)

def resize_and_pad(img, size):
    img.thumbnail(size, Image.Resampling.BILINEAR)  # keep aspect ratio
    new_img = Image.new("RGB", size, (0, 0, 0))  # black padding
    paste_x = (size[0] - img.width) // 2
    paste_y = (size[1] - img.height) // 2
    new_img.paste(img, (paste_x, paste_y))
    return new_img

# Create output directory structure
os.makedirs(output_dir, exist_ok=True)

for class_name in os.listdir(input_dir):
    class_path = os.path.join(input_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    output_class_path = os.path.join(output_dir, class_name)
    os.makedirs(output_class_path, exist_ok=True)

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        try:
            with Image.open(img_path).convert("RGB") as img:
                resized = resize_and_pad(img, target_size)
                output_path = os.path.join(output_class_path, img_name)
                resized.save(output_path)
        except Exception as e:
            print(f"[Error] Could not process {img_path}: {e}")