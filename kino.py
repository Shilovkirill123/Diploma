import requests
from fake_useragent import UserAgent

from model import Film
from bs4 import BeautifulSoup
from search_film import parsers


def get_html(url):
    ua = UserAgent()
    headers = {
            'User-Agent': ua.random
        }
    
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        print(result.text)
        return result.text
        
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_name_film(soup):
    film_list = soup.find('span', class_="moviename-title-wrapper").text
    print(film_list)
    return film_list


def get_film(soup):
    attr = ['год', 'страна', 'режиссер', 'сценарий', 'продюсер', 'оператор',
            'композитор', 'художник', 'монтаж', 'бюджет', 'маркетинг',
            'сборы в США', 'сборы в мире', 'премьера (мир)', 'премьера (РФ)']
    film_attr = {}
    film_lists = soup.find('table', {'class': 'info'}).find_all('tr')
    for film in film_lists:
        a = film.find('td', {'class': 'type'}).text
        try:
            if a in attr:
                film_attr[a.capitalize()] = film.find("a").text
        except(AttributeError):
            film_attr[a.capitalize()] = 'нет данных'
    return film_attr


def get_genre_film(soup):
    genres_0 = []
    genres = []
    film_lists = soup.find('table', {'class': 'info'}).find_all('tr')
    for film in film_lists:
        a = film.find('td', {'class': 'type'}).text
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


def get_tagline_film(soup):
    film_lists = soup.find('table', {'class': 'info'}).find_all('tr')
    for film in film_lists:
        a= film.find('td', {'class': 'type'}).text
        if a == 'слоган':
            tagline = film.find('td', {'style': 'color: #555'}).text
    return tagline


def get_duration_film(soup):
    film_list = soup.find('table', {'class': 'info'}).find('td', {'class': 'time'}).text
    return film_list


def get_actors_film(soup):
    actors = []
    film_list = soup.find_all('li', {'itemprop': 'actors'})
    for actor in film_list:
        actors.append(actor.text)
        actor = ', '.join(actors[:4])
    return actor


def get_rating_film(soup):
    film_list = soup.find('span', {'class': 'rating_ball'}).text
    return film_list


def get_number_film(soup):
    film_list = soup.find('li', {'class' : 'el_1'}).find('a').get('href')
    film_list = film_list.replace('https://www.kinopoisk.ru/film/', '').replace('/#', '')
    return film_list


def get_imdb_film(soup):
    film_list = soup.find('div', {'style': 'color:#999;font:100 11px tahoma, verdana'}).text.split()
    film_list = film_list[1]
    return film_list


def general(link):
    html = get_html(link)
    soup = BeautifulSoup(html, 'html.parser')
    film_data = {}
    film_data['Название фильма'] = get_name_film(soup)
    print(film_data)
    film_data['Слоган'] = get_tagline_film(soup)
    print(film_data)
    film_data['Актеры'] = get_actors_film(soup)
    print(film_data)
    film_data['Жанр'] = get_genre_film(soup)
    print(film_data)
    film_data['Рейтинг Кинопоиска'] = get_rating_film(soup)
    print(film_data)
    film_data['Рейтинг IMDB'] = get_imdb_film(soup)
    for a in get_film(soup):
        film_data[a] = get_film(soup)[a]
        print(film_data)
    film_data['Продолжительность'] = get_duration_film(soup)
    print(film_data)
    film_data['Номер на кинопоиске'] = get_number_film(soup)

    film = Film(
        id_kinopoisk=get_number_film(soup), name=get_name_film(soup), tagline=get_tagline_film(soup),
        actors=get_actors_film(soup), director=film_data['Режиссер'], rating=get_rating_film(soup),
        rating_imdb=get_imdb_film(soup), year=film_data['Год']
    )
    return film



'''
#Для парсинга из файла
f = open('film.html', 'r', encoding='utf-8')
content = f.read()
html = content
soup = BeautifulSoup(html, 'html.parser')
general()


# Для парсинга с сайта

print(content)
html = get_html(content) 
soup = BeautifulSoup(html, 'html.parser')
if html:
    general()


link = film_base()

html = get_html(link) 
soup = BeautifulSoup(html, 'html.parser')
if html:
    general()
'''