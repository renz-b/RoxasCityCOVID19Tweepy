import image_to_text
import screenshot_selenium
import rctweepy
import os
from datetime import datetime

root_dir = os.getcwd()
now = datetime.now()
current_date = now.strftime('%Y-%m-%d')

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

def current_covid_19_data_dictionary():
    image_to_text.files_workdir()
    image_to_text.folder_date()
    screenshot_selenium.automation_script()
    screenshot_selenium.scrnshot()
    # pytess func returns dict type of data
    return image_to_text.pytess()

def current_covid_19_data_dictionary_ifwithscreenshots(date=current_date):
    if os.getcwd() == root_dir:
        os.chdir('..\\files\\{}'.format(date))
    else:
        os.chdir(root_dir)
        os.chdir('..\\files\\{}'.format(date))
    return image_to_text.pytess()


def main():
    # prints lines to terminal for double checking
    os.chdir(root_dir)
    with open('data.txt', 'r') as file:
        for line in file.readlines():
            print(line)
            print('\n')
    data_dict = current_covid_19_data_dictionary        
    print(data_dict)

    user_input = input('Tweet data? y/n')
    if user_input == 'y':
        # tweets data if ok with user
        # appends to txt file in root folder for future purposes
        image_to_text.write_to_file(data_dict)
        rctweepy.tweet(data_dict)
    else:
        # if data is duplicate or same from yesterday retweet latest covid sats from chosen user
        dupe = input('Is data duplicate? y/n\n')
        if dupe == 'y':
            rctweepy.user_stats_retweet('WHOPhilippines')
        else:
            # calls function that can edit dictionary
            edit_data_before_tweet(data_dict)
        

if __name__ == '__main__':
    main()
