import pandas as pd


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


if __name__ == '__main__':
    pest24_rename_train_test_val()
    print("Done!")
