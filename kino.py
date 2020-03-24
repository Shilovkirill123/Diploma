import requests

from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
   

def get_name_film(html):
    film_list = soup.find(itemprop="name")['content']
    return film_list



def get_film(html):
    attr = ['год','страна','режиссер','сценарий','продюсер','оператор','композитор','художник','монтаж','бюджет','маркетинг','сборы в США','сборы в мире','премьера (мир)','премьера (РФ)']
    film_attr= {}
    soup = BeautifulSoup(html, 'html.parser')
    film_lists = soup.find('table',{'class':'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td',{'class':'type'}).text
        if a in attr:
             film_attr[a.capitalize()]=film.find("a").text
    return film_attr


def get_genre_film(html):
    genres_0=[]
    genres=[]
    film_lists = soup.find('table',{'class':'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td',{'class':'type'}).text
        if a == 'жанр':
            for genre in film:
                genres_0.append(genre.find_all('a'))
            genres_0 = genres_0[1]
            for b in genres_0:
                genres.append(b.text)
    del genres[-1]
    for gen in genres:     
        gen = ', '.join(genres)
    return gen


def get_tagline_film(html):
    film_lists = soup.find('table',{'class':'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td',{'class':'type'}).text
        if a == 'слоган':
            tagline = film.find('td',{'style':'color: #555'}).text
    return tagline        
        
    
def get_long_film(html):
    film_list = soup.find('table',{'class':'info'}).find('td' ,{'class':'time'}).text
    return film_list


def get_actors_film(html):
    actors = []
    film_list = soup.find_all('li',{'itemprop':'actors'})
    for actor in film_list:
        actors.append(actor.text)
    for actor in actors:
        actor = ', '.join(actors[:4])
    return actor

def get_rating_film(html):
    soup = BeautifulSoup(html, 'html.parser')
    film_list = soup.find('span',{'class': 'rating_ball'}).text
    return film_list


def general():
    film_data = {}
    film_data['Название фильма'] = get_name_film(html)
    film_data['Слоган'] = get_tagline_film(html)
    film_data['Актеры'] = get_actors_film(html)
    film_data['Рейтинг'] = get_rating_film(html)
    for a in get_film(html):
        film_data[a] = get_film(html)[a]
    film_data['Продолжительность'] = get_long_film(html)

    return film_data    
  


#Для парсинга из файла
f = open('film.html', 'r', encoding = 'utf-8')
content = f.read()
html = content
soup = BeautifulSoup(html, 'html.parser')
general()



'''

    
# Для парсинга с сайта    
    
html = get_html("https://www.kinopoisk.ru/film/326/")
soup = BeautifulSoup(html, 'html.parser')
if html:
    general()
    

'''

   



