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
    hashtags = []

    titles = soup.find_all('td', attrs = {'class':'titleColumn'})

    for link in titles:
        print (link.a.string)
        film.append(link.a.string)
        
    for z in film:
        z = z.replace(' ','')
        z = z.replace(':','')
        z = z.replace('.','')
        z = z.replace('(2015)','')
        hashtags.append(z)

    return film+hastags

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
    try:
        api.update_status('The highest grossing movie this weekend was '+film[0]+' which made a strong '+val[0]+' #'+hashtags[0]+' #boxoffice')
        time.sleep(120)
        api.update_status(film[1]+' came in second place at the box office this weekend with '+val[1]+' #'+hashtags[1]+' #boxoffice')
        time.sleep(120)
        api.update_status('In third place at the box office this weekend was '+film[2]+' which earned '+val[2]+' #'+hashtags[2]+' #boxoffice')
        time.sleep(120)
    except:
        pass
    
def tweetTop10():
    places = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth']
    
    i = 0
    
    while(i < len(film)):
        try:
            api.update_status(places[i]+' place at the box office this weekend went to '+film[i]+' which earned '+val[i]+' #'+hashtags[i]+' #boxoffice')
            time.sleep(240)
        except:
            api.update_status(places[i]+' place: '+film[i]+' eanred '+val[i])
            time.sleep(240)
        i+=1
    
    
def tweetRating():
    percent = []
    hashtags = []
    film = []
    users = []

    ratings = soup.find_all('strong')
    userRatings = soup.find_all('span', attrs = {'class':'value'})
    titles = soup.find_all('td', attrs = {'class':'overview-top'})

    for name in titles:
        name = name.a.string
        name = name.replace(' (2016)','')
        film.append(name)

    for link in ratings:
        link = link.string
        percent.append(link)

    for v in userRatings:
        v = float(v.string)
        v = v*10
        v = int(v)
        v = str(v)
        users.append(v)

    percent = percent[-11:]
    del percent[-1]

    film = film[-10:]

    for z in film:
        z = z.replace(' ','')
        z = z.replace(':','')
        z = z.replace('.','')
        z = z.replace('(2015)','')
        hashtags.append(z)

    i = 0

    while i != 10:
        try:
            api.update_status(film[i]+' recieved a rating of '+percent[i]+'% from critics while audiences gave it a '+users[i]+'% #'+hashtags[i])
            time.sleep(240)
        except:
            pass
        i += 1


