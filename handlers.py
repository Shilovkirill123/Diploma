from kino import general
from query import film_db
from search_film import parsers
from model import session


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('Напишите /film для просмотра списка фильмов')


def films(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    del user_text[0]
    user_text = (' '.join(user_text))
    content = parsers(user_text)
    update.message.reply_text(content)
    print('Вывод фильма с кинопоиска')

'''
def film(bot, update):
    film = general()
    message = []
    for a in film:
        message.append(f'{a}: {film[a]}')
    update.message.reply_text('\n'.join(message))
    print('Вывод данных фильма')
'''

def film_base(bot, update, user_data):
    user_text = update.message.text
    user_text = user_text.split()
    del user_text[0]
    user_text = (' '.join(user_text))
    a = film_db(user_text)

    for film in a:
        update.message.reply_text(film)
    if not a:
        content = parsers(user_text)
        attr_film = general(content)
        print(attr_film)
        session.add(attr_film)
        session.commit()
        update.message.reply_text(attr_film)
        print('Вывод фильма с кинопоиска')




    

