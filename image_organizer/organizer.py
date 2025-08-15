import os
import shutil
from PIL import Image
import argparse

def get_resolution(filepath):
    with Image.open(filepath) as img:
        return f"{img.width}x{img.height}"

def organize_by_resolution(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if not os.path.isfile(full_path):
            continue
        try:
            res = get_resolution(full_path)
            res_folder = os.path.join(path, res)
            os.makedirs(res_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(res_folder, file))
        except Exception:
            continue

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='Directory to organize')
    parser.add_argument('--mode', choices=['resolution'], default='resolution')
    args = parser.parse_args()

    if args.mode == 'resolution':
        organize_by_resolution(args.path)

if __name__ == "__main__":
    main()
