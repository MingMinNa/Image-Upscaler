# Image Upscaling Tool

English | <a href="./README.zh-TW.md">繁體中文</a>

![Static Badge](https://img.shields.io/badge/Python-3.12-blue) [![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

## Introduction
This project is based on [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) and is designed to enhance image quality.  
Run `main.py` to upscale all images in the input folder and save them to the output folder.

## Usage

### 1. Create and Activate a Virtual Environment
Create a virtual environment using the following commands, then activate it.  
Replace `<venv_name>` with your preferred environment name.

```bash
$ conda create -n <venv_name> python=3.12
$ conda activate <venv_name>
```

### 2. Install Dependencies
Install all required Python packages in the virtual environment

```bash
$ pip install -r requirements.txt
```

### 3. Download Model Weights
Place the downloaded model weights in the `weights/` folder under the project root.

### 4. Add Input Images
Place the images you want to upscale in the `image/` folder, or specify another input folder.

### 5. Run the Main Program
Run `main.py`. You can use the arguments to set the scaling factor, input and output paths, and other options.

```bash
Arguments
    --factor        Optional, scaling factor
    --input         Optional, input folder path
    --output        Optional, output folder path
    --overwrite     Optional, whether to overwrite existing files

Value ranges and defaults
    --factor        [2, 4, 8]                  Default: 2
    --input         Path string                Default: "./image"
    --output        Path string                Default: "./output"
    --overwrite     Flag (no value required)   Default: False
```

## Notes
Since the original source code of [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) is relatively old, this project makes minor changes to ensure compatibility with current environments. The modified source code is included directly in this project. However, the copyright of the original code remains with the original authors of the [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) project.