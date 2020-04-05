
from model import session, Film


def film_db(film_name):
    film_list_db = []
    for row in session.query(Film).filter(Film.name == film_name): 
        film_list_db.append(str(row))
    print(film_list_db)
    return film_list_db



'''
print(a)
# Получем название фильма из бота
if a in film_list_db:
    #Отправляем атрибуты из бд
    print('YES!')
else:
    print('NO')
    #Парсим данные с сайта в бд

'''
    



