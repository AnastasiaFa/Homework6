from translat import normalize
from transp import transp
from extract import extract

import os
import shutil

original_path = 'C:/Users/Fateeva/Downloads'

# key names will be folder names!

extensions = {

    'Video': ['mp4', 'mov', 'avi', 'mkv'],

    'Audio': ['mp3', 'wav', 'ogg', 'amr'],

    'Image': ['jpg', 'png', 'jpeg',  'svg'],

    'Archive': ['zip', 'gz', 'tar', 'rar'],

    'Text': ['pdf', 'txt', 'doc', 'docx', 'pptx', 'xlsx', 'xls'],
}


def traverse(main_path):
    files = os.listdir(main_path)

    print(files)

    for name in files:
        list = name.split('.') # list = ['name', 'extension']
        
        if os.path.isfile(os.path.join(main_path, name)):
            found_ext = False
            for value in extensions.values():
                for v in value:
                    if v == list[-1]:
                        for a,b in extensions.items():
                            if b == value:
                                found_ext = True
                                folder_name = a
                                
                                new_path = transp(original_path, main_path, folder_name, name)
                                if a == 'Archive':
                                    extract(new_path, name)

                            
                

            if not found_ext:        
                folder_name = 'Other'
                transp(original_path, main_path, folder_name, name)
        else:
            if name in extensions.keys() and name != "Other":
                continue
            else:
                new_path = os.path.join(main_path, name)
                traverse(new_path)
                shutil.rmtree(new_path)

traverse(original_path)