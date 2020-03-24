from kino import *

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
    for a in film:
        update.message.reply_text(f'{a}: {film[a]}')
    print('Вывод данных фильма') 
    

