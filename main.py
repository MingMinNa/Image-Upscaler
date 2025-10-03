import os
import argparse
import shutil
import torch

from tqdm import tqdm
from PIL import Image
from RealESRGAN import RealESRGAN

PROJECT_FOLDER = os.path.dirname(__file__)
MAX_BOUND = 6000

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
factor = None
model = None
model_path = None


def check_folder(folder_path: str) -> None: 
    
    if os.path.exists(folder_path) == False:
        raise FileExistsError(f"{folder_path} doesn't exist.")
    elif os.path.isfile(folder_path):
        raise ValueError(f"{folder_path} is a file, not folder.")
    return

def upscale_image(src_img_path: str, dest_img_path: str) -> bool:

    src_img = Image.open(src_img_path).convert('RGB')
    if (src_img.size[0] * factor > MAX_BOUND or 
        src_img.size[1] * factor > MAX_BOUND):

        shutil.copy(src_img_path, dest_img_path)
        return False
    
    dest_img = model.predict(src_img)
    dest_img.save(dest_img_path)
    return True

def check_file_format(file_path: str) -> bool:

    valid_formats = ['.png', '.jpg', '.jpeg', '.webp']

    for ext in valid_formats:
        if file_path.lower().endswith(ext):
            return True
    return False 

def init_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description = 'This is an image-upscaling tool')
    parser.add_argument('--factor', type = int, choices = [2, 4, 8], default = 2, help = 'set upscaling factor(x2, x4, x8)')
    parser.add_argument('--input' , type = str, default = os.path.join(PROJECT_FOLDER, 'image') , help = 'set input folder path')
    parser.add_argument('--output', type = str, default = os.path.join(PROJECT_FOLDER, 'output'), help = 'set output folder path')
    parser.add_argument('--overwrite', action = "store_true", help = 'set whether to overwrite the existing files')
    return parser

def select_model(scaling_factor: int) -> None:
    global factor, model, model_path

    if scaling_factor not in (2, 4, 8):
        raise ValueError('scaling_factor is out of bound')

    factor = scaling_factor
    model = RealESRGAN(device, scale = factor)
    model_path = os.path.join(PROJECT_FOLDER, 'weights', f'RealESRGAN_x{factor:1d}.pth')
    model.load_weights(model_path, download = True)
    return

def main() -> None:

    parser = init_parser()
    args = parser.parse_args()
    
    check_folder(os.path.abspath(args.input))
    select_model(scaling_factor = int(args.factor))
    
    replace_func = lambda path: path.replace(os.path.abspath(args.input), os.path.abspath(args.output))

    for root, _, files in tqdm(os.walk(os.path.abspath(args.input))):

        tqdm.write(f"Currently Processed Folder: {root}")
        
        out_folder_path = replace_func(root)
        os.makedirs(out_folder_path, exist_ok = True)

        for name in files:

            in_file_path = os.path.join(root, name)
            out_file_path = replace_func(in_file_path)

            if not args.overwrite and os.path.exists(out_file_path): 
                continue

            if check_file_format(in_file_path):
                upscaling = upscale_image(in_file_path, out_file_path)
                if upscaling:   tqdm.write(f"\033[1;32m[INFO]\033[0m    Upscaled: {in_file_path}")
                else:           tqdm.write(f"\033[1;33m[WARNING]\033[0m Image too large, copied: {in_file_path}") 
            else:               tqdm.write(f"\033[1;31m[ERROR]\033[0m   Unsupported format: {in_file_path}")
    return

if __name__ == '__main__':
    main()
    
