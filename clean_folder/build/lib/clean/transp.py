import os
from translat import normalize


def transp(original_path, main_path, folder_name, name):
    
    normalized_name = normalize(name)
    old_path = os.path.join(main_path, name)
    new_folder = os.path.join(original_path, folder_name)
    new_path = os.path.join(new_folder, normalized_name)
    
    try:
        os.mkdir(new_folder)
        os.replace(old_path, new_path)
    except FileExistsError:
        os.replace(old_path, new_path)
    return new_path



