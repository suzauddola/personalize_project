import os
from os.path import splitext
import shutil




def move_operations(src, dest, type, name_list, ext):
    for name in name_list:
        s_img = src + name.rstrip('\n') + ext
        d_img = dest + type + "/" + name.rstrip('\n') + ext
        shutil.copyfile(s_img, d_img)


def find_and_move_operations(src, dest):
    for root, dirs, files in os.walk((os.path.normpath(src)), topdown=False):
        for name in files:
            if name.endswith('.jpg'):
                # print("Found")
                source_folder = os.path.join(root, name)  # <--- Here is the change
                shutil.copy2(source_folder, dest)  # <--- Here is the change


def read_single_txt(file):
    lines = open(file, 'r').readlines()
    return lines


def find_and_copy(src, dest):
    shutil.copyfile(src, dest)


def read_filepath_and_var():

    img_src = r'F:/Datasets/Pest24/JPEGImages/'
    img_dest = r'F:/Datasets/Pest24/images/'

    lbl_src = r'F:/Datasets/Pest24/Annotations_txt/'
    lbl_dest = r'F:/Datasets/Pest24/labels/'

    types = ['train', 'test', 'val']
    exts = ['.jpg', '.txt']

    return img_src, lbl_src, lbl_dest, img_dest, types, exts


if __name__ == '__main__':

    img_src, lbl_src, lbl_dest, img_dest, types, exts = read_filepath_and_var()

    for type_name in types:

        path_contains_txt_file = 'F:/Datasets/Pest24/ImageSets/'+type_name+'.txt'
        name_list = read_single_txt(path_contains_txt_file)

        for ext in exts:
            if ext == '.jpg':
                src = img_src
                dest = img_dest
            else:
                src = lbl_src
                dest = lbl_dest

            move_operations(src, dest, type_name, name_list, ext)


