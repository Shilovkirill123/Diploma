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
    soup = BeautifulSoup(html, 'html.parser')
    film_list = soup.find(itemprop="name")['content']
    print(f'Название фильма: {film_list}')



def get_film(html):
    attr = ['год','страна','режиссер','сценарий','продюсер','оператор','композитор','художник','монтаж','жанр','бюджет','маркетинг','сборы в США','сборы в мире','премьера (мир)','премьера (РФ)']
    soup = BeautifulSoup(html, 'html.parser')
    film_lists = soup.find('table',{'class':'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td',{'class':'type'}).text
        if a in attr:
            print(f'{a}: {film.find("a").text}')


def get_genre_film(html):
    genres_0=[]
    genres=[]
    soup = BeautifulSoup(html, 'html.parser')
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
    print(f'жанр: {gen}')


def get_tagline_film(html):
    soup = BeautifulSoup(html, 'html.parser')
    film_lists = soup.find('table',{'class':'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td',{'class':'type'}).text
        if a == 'слоган':
            print(f"{a}: {film.find('td',{'style':'color: #555'}).text}")
        
    
def get_long_film(html):
    soup = BeautifulSoup(html, 'html.parser')
    film_list = soup.find('table',{'class':'info'}).find('td' ,{'class':'time'}).text
    print(f'Продолжительность: {film_list}')


def get_actors_film(html):
    actors = []
    soup = BeautifulSoup(html, 'html.parser')
    film_list = soup.find_all('li',{'itemprop':'actors'})
    for actor in film_list:
        actors.append(actor.text)
    for actor in actors:
        actor = ', '.join(actors[:4])
    print(f'актеры: {actor}')

def get_rating_film(html):
    soup = BeautifulSoup(html, 'html.parser')
    film_list = soup.find('span',{'class': 'rating_ball'}).text
    print(f'рейтинг кинопоиска: {film_list}')



if __name__ == "__main__":
    
    
#Для парсинга из файла
    f = open('film.html', 'r', encoding = 'utf-8')
    content = f.read()
    html = content
    
    get_name_film(content)
    get_tagline_film(content)
    get_genre_film(content)
    get_actors_film(content)
    get_rating_film(content)
    get_film(content)
    get_long_film(content)
    
# Для парсинга с сайта    
    '''
    
    html = get_html("https://www.kinopoisk.ru/film/435/")
    if html:
        get_name_film(html)
        get_tagline_film(html)
        get_genre_film(html)
        get_actors_film(html)
        get_rating_film(html)
        get_film(html)
        get_long_film(html)
    '''
    
        

   



