import image_to_text
import screenshot_selenium
import rctweepy
import os
import ast
from datetime import datetime

root_dir = os.getcwd()
now = datetime.now()
current_date = now.strftime('%Y-%m-%d')

def edit_data_before_tweet(data_dict):
    # Changes data before tweeting
    while True:
        edit = input('Edit keys? (y/n): \n')
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
                    list_ = input('List: ')
                    data_dict[key_] = list_.split()
                    print(data_dict[key_])
            else:
                value_ = input('Corrected value: ')
                data_dict[key_] = value_
            print(data_dict)
            bool_ = input('Continue edit (y/n): \n')
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

def data_pretty_print():
    os.chdir(root_dir)
    dict_history = {}
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            dict_ = ast.literal_eval(line)
            date_key = dict_['_id']
            dict_history[date_key] = dict_
            for k, v in dict_history[date_key].items():
                print('{}: {}'.format(k,v))
            print('\n\n')

def main():
    data_pretty_print()
    data_dict = current_covid_19_data_dictionary()  

    # if already with screenshots
    # data_dict = current_covid_19_data_dictionary_ifwithscreenshots()
    
    for k, v in data_dict.items():
        print('{}: {}'.format(k, v))

    user_input = input('Tweet data? (y/n)\n')
    if user_input == 'y':
        # tweets data if ok with user
        # appends to txt file in root folder for future purposes
        rctweepy.tweet(data_dict)
        image_to_text.write_to_file(data_dict)
    else:
        # if data is duplicate or same from yesterday retweet latest covid sats from chosen user
        dupe = input('Is data duplicate? (y/n)\n')
        if dupe == 'y':
            os.chdir(root_dir)
            rctweepy.user_stats_retweet()
        else:
            # calls function that can edit dictionary
            edit_data_before_tweet(data_dict)
        

if __name__ == '__main__':
    main()
