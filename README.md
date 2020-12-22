# RoxasCityCOVID19Tweepy-
@rxstwitte_rbot

ROXAS CITY COVID 19 BOT
> I am a bot that tweets COVID 19 stats. I use selenium to automate navigation through the website (simple requests HTML does not work) and then takes a screenshot of the desired data.
I then use pytesseract to recognize text and numbers on the screenshot which then returns a string. String is then formatted and tweeted using Tweepy API.
> If data is duplicate from yesterday, automated retweet from latest COVID 19 news from WHO.

Python 3.9

Doing testing on 'test' branch. Adding tinyDB and trying to visualize data


V 2.7.0
- Func: Added tweets.txt function to rctweepy.py using a nested function

V 2.6.0
- Func: Now able to get data type string from data.txt and convert it to a dictionary 
    (data_dict -> write to data.txt as string -> used import ast -> read data.txt as string ->data_dict)
- Func: Added pretty_print function to easily view previous data
- Added workshop folder to show: test.py, TODO.txt


V 2.5.0
- Func: Improved modularity; added function if with screenshots selenium script does not have to run again. Added error handling in retweet. 
- Todo: Further error handling if with invalid user inputs
- Plan: V 3.0.0 source: DOH data drop consisting of CSV files. Parse using pandas.

V 2.4.0
- Func: If data is duplicate from yesterday or unupdated, bot will retweet latest COVID stats from WHO

V 2.3.0
- Func: Show data before calling tweet function to double check data, now able to edit dictionary of data before tweeting
- Added: bat file
- Todo: If data is the same as yesterday, apply covid stream to tweet latest covid news instead, will add if screenshots if exists so that program does not have to run every single time

V 2.2.0
- Style: added date-of-runtime
- Func: improved modularity
- New twitter profile: @rxstwitte_rbot
- Todo: Improve PIL image enhancing for better detection of OCR


V 2.1.0
- Added code so that tweets would be in a thread
- Formatting changes to tweet
- Added checkpoint if data is erroneous or image to text does not work right
- Problems: Selenium sometimes clicks the wrong checkbox even if I used find_element_by_xpath


V 2.0.0
- Changed source website to DOH tableau dashboard
- Link: https://public.tableau.com/profile/doh.covid#!/vizhome/COVID-19CasesandDeathsinthePhilippines_15866705872710/Home
- Selenium to automate the website and take screenshot. Pytesseract API to convert image to a str. Tweepy API to tweet results.
- Task scheduler to run daily.


V 1.0.0
- Simple requests from HTML and parsing to get data. Used a simple website but unreliable.
- Simple Tweepy API 



> Dependencies are in requirements.txt
- pip install requirements.txt
- (note: had to install pytesseract separetly after importing and specifying the PATH)
