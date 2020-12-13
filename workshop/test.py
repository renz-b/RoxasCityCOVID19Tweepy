# import ast
# dict_history = {}
# with open('data.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         dict_ = ast.literal_eval(line)
#         string = dict_['_id']
#         dict_history[string] = dict_
#         for k, v in dict_history[string].items():
#             print('{}: {}'.format(k,v))
#         print('\n\n')
# # implement this so that I can call the previous day and compare the values from the previous date
# # this code accepts the data.txt file and converts to dictionary
# # Key (yyyy-mm-dd) format the value is the whole file


# forever loop for heroku
# import time
# not_retweeted = True

# while not_retweeted is True:
#     # get_user get_timeline that checks the latest tweets with search paramaters using datetime
#     # this should be a function if no tweets found should return None
#     print('no new tweet')
#     # if statement if func returns string_of_tweet retweet
#     #time.sleep(5minutes)
#     x = input('retweet?')
#     if x == 'y': 
#     # if x == returns (string of tweet)
#     # x == returns none from get_user get_timelines function go to else continue 
#         retweeted = True
#         while retweeted is True:
#             print('already retweeted')
#             time.sleep(1) # calculation for 24 hour variable
#             retweeted = False
#     else:
#         continue

def func1():
    var1 = "hi"
    var2 = "hello"
    var3 = "world"

    def func2():
        long_var = '{} {} {}'.format(var1, var2, var3)
        print(long_var)

    func2()
    




func1()
