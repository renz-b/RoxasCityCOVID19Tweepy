import image_to_text
import screenshot_selenium
import rctweepy
import os

root_dir = os.getcwd()

def if_same_data_latest_news():
    pass

def edit_data_before_tweet(data_dict):
    # Changes data before tweeting
    while True:
        edit = input('Edit keys? y/n \n')
        if edit == 'y':
            key_ = input('Key: ')
            if type(data_dict[key_]) == list:
                key_edit = input('Edit whole list (1) or specific list position (2): ')
                if key_edit == "2":
                    print(data_dict[key_])
                    print([x for x in range(len(data_dict[key_]))])
                    key_order = input('Input key position: ')
                    specific_value = input('Corrected key value in position {}, last position: {} :'.format(str(key_order), str(len(data_dict[key_])- 1)))
                    data_dict[key_][int(key_order)] = specific_value
                    print(data_dict[key_])
                else:
                    print(data_dict[key_])
                    list_ = input('List:')
                    data_dict[key_] = list_.split()
                    print(data_dict[key_])
            else:
                value_ = input('Corrected value: ')
                data_dict[key_] = value_
            print(data_dict)
            bool_ = input('Continue edit (y/n): ')
            if bool_ == 'n':
                # appends to txt file in root folder for future purposes
                image_to_text.write_to_file(data_dict)
                rctweepy.tweet(data_dict)
                break
            else:
                continue
        else:
            break



def main():
    image_to_text.files_workdir()
    image_to_text.folder_date()
    screenshot_selenium.automation_script()
    screenshot_selenium.scrnshot()

    # pytess func returns dict type of data
    data_dict = image_to_text.pytess()

    # prints lines to terminal for double checking
    os.chdir(root_dir)
    with open('data.txt') as file:
        for line in file.readlines():
            print(line)
    print(data_dict)

    user_input = input('Continue? y/n\n')
    if user_input == 'y':
        # tweets data if ok with user
        # appends to txt file in root folder for future purposes
        image_to_text.write_to_file(data_dict)
        rctweepy.tweet(data_dict)
    else:
        print('Double check data\n')
        # calls function that can edit dictionary
        edit_data_before_tweet(data_dict)
        

if __name__ == '__main__':
    main()