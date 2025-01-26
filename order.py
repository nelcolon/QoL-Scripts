import os
from collections import defaultdict
import sys

def organize_files_by_extension(directory):
    files_by_extension = defaultdict(list)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"THIS IS A FOLDER: {item_path}")
        else:
            ext = os.path.splitext(item)[1]
            files_by_extension[ext].append(item_path)

    for ext in sorted(files_by_extension):
        print(f"FILES WITH EXTENSION: {ext}")
        for file in sorted(files_by_extension[ext]):
            print(file)
        print()
    
    for ext, files in files_by_extension.items():
        ext_folder = os.path.join(directory, ext.lstrip('.'))
        os.makedirs(ext_folder, exist_ok=True)
        for file in files:
            os.rename(file, os.path.join(ext_folder, os.path.basename(file)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()

    organize_files_by_extension(directory)