import requests
import re
import datetime
import time

def getWordleDateList():
    r = requests.get('https://www.nytimes.com/games/wordle/main.4d41d2be.js')
    x = re.search("Ma=\\[(\"\\w{5}\",?)+]", r.text)
    words = re.findall("\\w{5}", x[0])

    beginning = datetime.datetime(2021, 6, 19)

    date_word_list = []
    today_index = 0

    for word in words:
        difference = datetime.timedelta(words.index(word))
        date = beginning + difference
        if date == datetime.date.today():
            today_index = words.index(word)
        date_word_list.append(date.strftime("%a, %b %d %Y = " + word))

    return date_word_list, today_index

if __name__ == "__main__":
    words = getWordleDateList()[0]
    for word in words:
        print(word)
        time.sleep(0.001)

