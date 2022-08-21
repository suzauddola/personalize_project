import pandas as pd
import os


# os.chdir()

# rename
def _rename_inside_txt_file_list(file_with_names, new_file_location, server_location_image_name):
    new_file_to_save = open(new_file_location, "w")

    for index, image in file_with_names.iterrows():
        image_name = image['name']
        print(str(index) + "-->" + image_name)
        text = server_location_image_name + image_name + '.jpg' + "\n"
        new_file_to_save.write(text)
        # if index >= 4800:
        #     print(text)
        #     test_file.write(text)


# rename
def pest24_rename_train_test_val():
    location_of_txt_file = r'F:/Datasets/Pest24/ImageSets/val.txt'
    load_file_with_name = pd.read_csv(location_of_txt_file, delim_whitespace=False, header=None, delimiter=',',
                                      names=['name'])

    new_file_location = r'F:/Datasets/Pest24/ImageSets_with_server_locations/val.txt'

    server_location_image_name = r"/home/suza/yolo/yolov7/pest24/images/train/"

    _rename_inside_txt_file_list(load_file_with_name, new_file_location, server_location_image_name)


# can read but can not save into the .txt file
def read_all_file_name_from_a_location_and_save_into_txt_file():
    img_file_path = "D:/ResearchData/phd_research/Project/yolo/ScaledYOLOv4/coco/test2017"

    all_image_name = [imagename for imagename in os.listdir(img_file_path)]

    # print(len(all_image_name))
    counter = 0

    name_file = []

    file = open("new.txt", "w")

    for imagename in all_image_name:
        file.write(imagename + '\n')
        name_file.append(imagename + '\n')

    # print("Total Unmatched : " + Integer.toString(counter))
    print(counter)
    print(len(name_file))
    file.close()


if __name__ == '__main__':
    pest24_rename_train_test_val()
    print("Done!")
