import image_to_text
import screenshot_selenium
import rctweepy
import os


def main():
    image_to_text.files_workdir()
    image_to_text.folder_date()
    screenshot_selenium.automation_script()
    screenshot_selenium.scrnshot()
    # pytess func returns dict type of data
    data_dict = image_to_text.pytess()
    with open('data.txt') as file:
        for line in file.readlines():
            print(line)
    user_input = input('Continue? yes/no')
    if user_input == 'yes':
        rctweepy.tweet(data_dict)
    else:
        print('Double check data')

if __name__ == '__main__':
    main()