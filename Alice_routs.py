class Messages:
    __welcome_message = {
        'text': 'Приветствую!\nЭтот навык - гид по достопримечательностям Екатеринбурга. Вам на выбор предоставляется несколько веток для прохождения экскурсии, после чего мы простроим вам мартрут в Яндекс Картах для самостоятельного прохождения. Начнем?',
        'buttons': [
            {
            'title': 'Да',
            'hide': 'true'
            },
            {
            'title' : 'Нет',
            'hide' : 'true'
            },
            {
            'title' : 'Помощь',
            'hide' : 'true'
            }
            ],
        'end_session': 'false'
    }

    __help_message = {
        'text': 'Данный навык позволяет самостоятельно провести экскурсию по Екатеринбургу.\nВам на выбор даёт синяя, красная, оранжевая, розовая ветки и ближайшая к вам достопримечательность, если ветки вас не заинтересовали. После выбора маршрута вам будет представлена достопримечательность с ее описанием и изображением, после чего вы можете либо продолжить маршрут, либо выбрать другой, либо простроить в Яндекст Картах маршрут для личного прохождения по всей ветке или до ближайшей достопримечательности в случае ее выбора. Начнем?',
        'buttons': [
                {
                'title': 'Да',
                'hide': 'true'
                },
                {
                'title' : 'Нет',
                'hide' : 'true'
                }
                ],
        'end_session': 'false'
        }

    __routes = {
        'text' : 'Пожалуйста, выберите маршрут, нажав на его картинку. На выбор вам дается синяя, красная, оранжевая и розовая линии, которое помогут вам лучше познакомиться с историей города. Если же вас ни одна ветка не заинтерисовала, то я могу найти для вас ближайшую достопримечательность.',
        'card' : {
            "type": "ImageGallery",
            "items": [
                {
                "image_id": "997614/b0e51d8962f0d35f7fa9",
                "title": "Синяя линяя",
                'description' : 'Синяя линия — маршрут, связанный с именем царской семьи, его нанесли на тротуар к 100-летию со дня гибели Романовых. Протяженность маршрута 6.2км.',
                "button" : {
                    "text" : 'Синяя линия',
                    "payload": {
                        'command': 'start_excursion',
                        'line': 'blue_line',
                        'next_sight_number': '0',
                        'visited_sights_number' : '1',
                        'total_sights_number' : '12',
                        'new_excursion' : 'true'
                        }
                    }
                },
                {
                "image_id": "1533899/702e932488ab8d0a82ae",
                "title": "Красная линия",
                'description' : 'Красная линия Екатеринбурга – маршрут по главным достопримечательностям города западной стороны реки Исеть. Длина маршрута составляет 4.5 км.',
                "button": {
                    "text" : 'Красная линия',
                    "payload": {
                        'command': 'start_excursion',
                        'line': 'red_line',
                        'next_sight_number': '0',
                        'visited_sights_number' : '1',
                        'total_sights_number' : '19',
                        'new_excursion' : 'true'
                        }
                    }
                },
                 {
                "image_id": "1030494/80075994a87c0ee030f1",
                "title": "Оранжевая линия",
                'description' : 'Оранжевая линия Екатеринбурга – маршрут по главным достопримечательностям города восточной стороны реки Исеть. Длина маршрута составляет 4.5 км.',
                "button": {
                    "text" : 'Оранжевая линия',
                    "payload": {
                        'command': 'start_excursion',
                        'line': 'orange_line',
                        'next_sight_number': '0',
                        'visited_sights_number' : '1',
                        'total_sights_number' : '19',
                        'new_excursion' : 'true'
                        }
                    }
                },
                {
                "image_id": "965417/f93a672ff1d03a1c4697",
                "title": "Розовая линия",
                'description' : 'Розовая линия - проект Street art line фестиваля STENOGRAFFIA, объединяющий значимые объекты уличного искусства. Протяженность маршрута составила 10 км.',
                "button": {
                    "text" : 'Розовая линия',
                    "payload": {
                        'command': 'start_excursion',
                        'line': 'pink_line',
                        'next_sight_number': '0',
                        'visited_sights_number' : '1',
                        'total_sights_number' : '19',
                        'new_excursion' : 'true'
                        }
                    }
                },
                {
                "image_id": "937455/bc59e8885df7f3830af8",
                "title": "Ближайшая достопримечательность",
                'description': 'Если вас не заитересовали стандартные маршруты, то я могу показать ближайшаю к вам достопримечательность.',
                "button": {
                    "text" : 'Ближайшая достопримечательность',
                    "payload": {
                        'command' : 'find_the_nearest_sight',
                        'line' : 'other_sights'
                        }
                    }
                }
                ]
            },
        'end_session' : 'false'
        }

    __ask_address = {
        'text' : 'Пожалуйста, введите адрес, где вы сейчас находитесь в формате (Улица, дом). Это поможет мне в прокладывании маршрута.',
        'end_session' : 'false'
    }

    __farewell = {
        'text': 'До свидания, надеюсь еще увидимся!',
        'end_session' : 'true'
    }

    __geocode_error = {
        'text': 'Извините, произошла ошибка в получении ваших координат. Введите, пожалуйста, адрес заново.',
        'end_session': 'false'
    }

    __address_error = {
        'text': 'Извините, не поняли ваш адрес. Введите, пожалуйста, адрес заново.',
        'end_session': 'false'
    }

    __regular_error = {
        'text' : 'Извините, произошла ошибка на сервере. Попробуйте позже.',
        'end_session' : 'false'
    }

    __regular_message = {
            'text': f'Извините, я вас не поняла. Попробуйте ответить иначе.',
            'end_session': 'false'
        }

    @staticmethod
    def make_current_sight_message(title: str, image_id: str, description: str, button_text: str, command: str, line: str,
                                   next_sight_number: str, visited_sights_number: str, total_sights_number: str) -> dict:
        message = {
            'text': title,
            "card": {
                "type": "BigImage",
                "image_id": image_id,
                "title": title,
                "description": description
            },
            "buttons": [
                {
                    "title": button_text,
                    "payload": {
                        'command': command,
                        'line': line,
                        'next_sight_number': str(int(next_sight_number) + 1),
                        'visited_sights_number': str(int(visited_sights_number) + 1),
                        'total_sights_number': total_sights_number,
                        'new_excursion' : 'false'
                    },
                    'hide': 'true'
                },
                {
                    'title': 'Давай постоим маршрут',
                    'payload': {
                        'command': 'make_rout',
                        'line': line,
                        'total_sights_number': total_sights_number
                    },
                    'hide': 'true'
                },
                {
                    'title': 'Выбрать другой маршрут',
                    'payload': {
                        'command': 'change_route'
                    },
                    'hide': 'true'
                }
            ],
            'end_session': 'false'
        }

        if visited_sights_number == total_sights_number:
            message['card'][
                "description"] += '\nМаршрут подошел к концу. Не хотите пройтись по нему самостоятельно?'
            message["buttons"] = [
                {
                    'title': 'Давай построим маршрут',
                    'payload': {
                        'command': 'make_rout',
                        'line': line,
                        'total_sights_number': total_sights_number
                    },
                    'hide': 'true'
                },
                {
                    'title': 'Выбрать другой маршрут',
                    'payload': {
                        'command': 'change_route'
                    },
                    'hide': 'true'
                }
            ]
        return message

    @staticmethod
    def make_rout_url_message(rout_url: str) -> dict:
        message = {
            'text': "Надеюсь, что вам понравилось пользоваться навыком.\nНажмите на кнопку ниже, чтобы перейти к маршруту.",
            'buttons': [
                {
                    'title': 'Построить маршрут',
                    'url': rout_url,
                    'hide': 'true'
                },
                {
                    'title': 'Выход',
                    'payload': {
                        'command': 'exit'
                    },
                    'hide': 'true'
                }
            ],
            'end_session': 'false'
        }
        return message

    @staticmethod
    def make_the_nearest_sight_number_message(image_id: str, title: str, description: str,
                        user_latitude: str, user_longitude: str, sight_latitude: str, sight_longitude: str) -> dict:
        rout_url = f'https://yandex.ru/maps?rtext={user_latitude}%2C{user_longitude}~{sight_latitude}%2C{sight_longitude}&rtt=pd'
        message = {
            'text': title,
            "card": {
                "type": "BigImage",
                "image_id": image_id,
                "title": title,
                "description": description
            },
            "buttons": [
                {
                    'title': 'Построить маршрут',
                    'url': rout_url,
                    'hide': 'true'
                },
                {
                    'title': 'Выбрать другой маршрут',
                    'payload': {
                        'command': 'change_route'
                    },
                    'hide': 'true'
                },
                {
                    'title': 'Выход',
                    'payload': {
                        'command': 'exit'
                    },
                    'hide': 'true'
                }
            ],
            'end_session': 'false'
        }
        return message

    @staticmethod
    def get_welcome_message() -> dict:
        return Messages.__welcome_message

    @staticmethod
    def get_help_message() -> dict:
        return Messages.__help_message

    @staticmethod
    def get_routs() -> dict:
        return Messages.__routes

    @staticmethod
    def get_ask_address() -> dict:
        return Messages.__ask_address

    @staticmethod
    def get_farewell() -> dict:
        return Messages.__farewell

    @staticmethod
    def get_address_error() -> dict:
        return Messages.__address_error

    @staticmethod
    def get_geocode_error() -> dict:
        return Messages.__geocode_error

    @staticmethod
    def get_regular_error() -> dict:
        return Messages.__regular_error

    @staticmethod
    def get_regular_message() -> dict:
        return Messages.__regular_message
