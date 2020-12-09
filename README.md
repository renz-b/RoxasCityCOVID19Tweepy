# RoxasCityCOVID19Tweepy-


ROXAS CITY COVID 19 BOT
> I am a bot that tweets COVID 19 stats. I use selenium to automate navigation through the website (simple requests HTML does not work) and then takes a screenshot of the desired data.
I then use pytesseract to recognize text and numbers on the screenshot which then returns a string. String is then formatted and tweeted using Tweepy API.


Python 3.9

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
pip install requirements.txt
(note: had to install pytesseract separetly after importing and specifying the PATH)
