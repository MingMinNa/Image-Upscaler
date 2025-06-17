import os
import argparse
import shutil
import torch
from tqdm import tqdm
from PIL import Image
from RealESRGAN import RealESRGAN

PROJECT_FOLDER = os.path.dirname(__file__)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = None
model_path = None
upscaling_bound = (None, None)


def search_folders(folder_path):
    '''
    Given a folder path, search all the sub folder paths(include itself). 
    Return them as a list of string
    '''
    if os.path.exists(folder_path) == False:
        raise FileExistsError(f"{folder_path} doesn't exist.")
    elif os.path.isfile(folder_path):
        raise ValueError(f"{folder_path} is a file, not folder.")
    
    sub_folder_paths = [folder_path]
    for name in os.listdir(path = folder_path):
        path = os.path.join(folder_path, name)
        if os.path.isdir(path):
            sub_folder_paths += search_folders(path)

    return sub_folder_paths

def upscale_image(src_img_path, dest_img_path):
    global upscaling_bound

    src_img = Image.open(src_img_path).convert('RGB')
    if src_img.size[0] > upscaling_bound[0] and src_img.size[1] > upscaling_bound[1]:
        shutil.copy(src_img_path, dest_img_path)
        return False
    else:
        dest_img = model.predict(src_img)
        dest_img.save(dest_img_path)
    return True

def check_file_format(file_path):
    if file_path.endswith('.png') or \
       file_path.endswith('.jpg') or \
       file_path.endswith('.jpeg') or \
       file_path.endswith('.webp'):
        return True
    return False 

def init_parser():

    parser = argparse.ArgumentParser(description = 'This is an image-upscaling tool')
    parser.add_argument('--factor', type = int, choices = [2, 4, 8], default = 2, help = 'set upscaling factor(x2, x4, x8)')
    return parser

def select_model(scaling_factor):
    global model, model_path, upscaling_bound

    if scaling_factor not in (2, 4, 8):
        raise ValueError('scaling_factor is out of bound')

    model = RealESRGAN(device, scale = scaling_factor)
    model_path = os.path.join('weights', f'RealESRGAN_x{scaling_factor:1d}.pth')
    model.load_weights(model_path, download = True)
    upscaling_bound = (3000 / scaling_factor, 3000 / scaling_factor)
    
    return

def main():
    parser = init_parser()
    args = parser.parse_args()
    select_model(scaling_factor = int(args.factor))

    raw_folders_abspath = search_folders(os.path.join(PROJECT_FOLDER, 'image'))
    
    replace_func = lambda path: path.replace(os.path.join(PROJECT_FOLDER, 'image'), os.path.join(PROJECT_FOLDER, 'output'))

    for raw_folder_path in tqdm(raw_folders_abspath):
        tqdm.write(f"Currently Processed Folder: {raw_folder_path}")
        output_folder_path = replace_func(raw_folder_path)

        os.makedirs(output_folder_path, exist_ok = True)
        for name in tqdm(os.listdir(raw_folder_path)):
            raw_file_path = os.path.join(raw_folder_path, name)
            output_file_path = replace_func(raw_file_path)
            if not os.path.isfile(raw_file_path) or \
               os.path.exists(output_file_path): continue

            if check_file_format(raw_file_path):
                upscaling = upscale_image(src_img_path = raw_file_path, dest_img_path = output_file_path)
                if upscaling:   tqdm.write(f"Upscaling Image: {raw_file_path}")
            else:
                tqdm.write(f"file path:\"{raw_file_path}\" doesn't be converted successfully!")

if __name__ == '__main__':
    main()
    
