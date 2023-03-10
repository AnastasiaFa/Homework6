import shutil
import os

def extract(new_path, name):
    shutil.unpack_archive(new_path, os.path.splitext(new_path)[0])
    os.remove(new_path)
# extract('chapter7-tornado.zip', 'chapter7-tornado')