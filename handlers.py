from kino import general
from query import film_db


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('Напишите /film для просмотра списка фильмов')


def films(bot, update):
    with open('films.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    update.message.reply_text(f'Список фильмов: \n{content}')
    print('Вывод списка фильмов')


def film(bot, update):
    film = general()
    message = []
    for a in film:
        message.append(f'{a}: {film[a]}')
    update.message.reply_text('\n'.join(message))
    print('Вывод данных фильма')


def film_base(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    del user_text[0]
    user_text = (' '.join(user_text))
    a = film_db(user_text)

    for film in a:
        update.message.reply_text(film)
    if not a:
        update.message.reply_text('В базе фильма нет!')
