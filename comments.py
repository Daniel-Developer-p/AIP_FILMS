comments = [
    {
        'title': 'Название фильма',
        'img': 'Ссылка на картинку',
        'body': 'Краткое описание (желательно тырить с кинопоиска)',
        'middle_ball': 'Средняя оценка фильма (от 0 да 5)'
    },

    {
        'title': 'Интерстеллар',
        'img': 'https://avatars.mds.yandex.net/get-kinopoisk-image/1600647/430042eb-ee69-4818-aed0-a312400a26bf/300x450',
        'body': 'Космос',
        'middle_ball': '4.5'
    },

    {
        'title': 'Лига Справедливости Знака Снайдара',
        'img': 'https://i.pinimg.com/736x/b5/11/41/b511418db3b345f216352afaee23ab12.jpg',
        'body': 'Круто',
        'middle_ball': '5.0'
    },

    {
        'title': 'Шазам!',
        'img': 'https://i.pinimg.com/originals/c0/ed/e0/c0ede023675dbf2c65078d5cfe6c630e.jpg',
        'body': 'неплохо',
        'middle_ball': '4'
    },

    {
        'title': 'Джон Уик',
        'img': 'https://ratinglist.ru/wp-content/uploads/2019/03/762738.jpg',
        'body': 'Куча перестрелок',
        'middle_ball': '4'
    },

    {
        'title': 'Джон Уик 3',
        'img': 'https://www.film.ru/sites/default/files/movies/posters/32558904-1105257.jpg',
        'body': 'Куча перестрелок, опять..',
        'middle_ball': '4'
    },

    {
        'title': 'Джон Уик',
        'img': 'https://ratinglist.ru/wp-content/uploads/2019/03/762738.jpg',
        'body': 'Куча перестрелок, опять..',
        'middle_ball': '4'
    },

    {
        'title': 'Джон Уик',
        'img': 'https://ratinglist.ru/wp-content/uploads/2019/03/762738.jpg',
        'body': 'Куча перестрелок, опять..',
        'middle_ball': '4'
    }

    # В подобном виде сюда нужно перевести данные из БД
]


def find_by_text(text: str, articles):
    result = []
    text = text.lower()
    for article in articles:
        if text in article.title.lower() or text in article.body.lower():
            result.append(article)
    return result
