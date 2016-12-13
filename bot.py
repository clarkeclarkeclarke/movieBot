import csv
import requests
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

def filmTitles():
    url = 'http://www.imdb.com/chart/boxoffice'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)


    film = []

    titles = soup.find_all('td', attrs = {'class':'titleColumn'})

    for link in titles:
        print (link.a.string)
        film.append(link.a.string)

    print (film)

def filmGross():
    url = 'http://www.imdb.com/chart/boxoffice'
    response = requests.get(url)
    html = response.content

    money = soup.find_all('td', attrs = {'class':'ratingColumn'})

    for i in money:
        text = i.text.replace('\n','')
        text = text.replace('                            ','')
        text = text.replace('                    ','')
        #print text
        val.append(text)

    val = val[::2]

    dictionary = dict(zip(film,val))

    print (dictionary)
    
def weeksOut():
    url = 'http://www.imdb.com/chart/boxoffice'
    response = requests.get(url)
    html = response.content

    weeks = soup.find_all('td', attrs = {'class':'weeksColumn'})

    wOut = []

    for w in weeks:
        w = w.getText()
        wOut.append(w)

    dictionary = dict(zip(film,wOut))

    print (dictionary)
    
def tweetTop3():
    api.update_status('The highest grossing movie this weekend was '+film[0]+' which made a strong '+val[0])
    api.update_status(film[1]+' came in second place at the box office this weekend with '+val[1])
    api.update_status('In third place at the box office this weekend was '+film[2]+' which earned '+val[2])
