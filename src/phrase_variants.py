import config

Greeting = {"en": ["Hello", "Hi!", "Welcome back :)"],
            "ru": ["Привет", "Здравствуйте", "Добро пожаловать!"],
            "de": ["Hallo", "Willkommen"]}
Language = {"en": ["To change the language, use the /language command"],
            "ru": ["Чтобы поменять язык, используйте команду /language"],
            "de": ["Um die Sprache zu ändern, benutzen Sie den Befehl /language"]}
Farewell = {"en": ["Goodbye", "Bye", "See you later"],
            "ru": ["До свидания", "До встречи"],
            "de": ["Auf wiedersehen", "Tschüss"]}
Links = {"en": ["Here you go", "There you go", "I`m on it"],
         "ru": ["Пожалуйста!", "Сайт открыт"],
         "de": ["Die Website wurde geöffnet"]}
Feeling = {"en": ["All is well, thank you" + config.emojis["blush"],
                  "I`m feeling a bit under the weather" + config.emojis["sad"],
                  "I`m ok", "I`m great, how about you?"],
           "ru": ["У меня все отлично, спасибо" + config.emojis["blush"],
                  "Я спокоен", "Все прекрасно)"],
           "de": ["Alles gut, danke" + config.emojis["blush"], "Ich bin ok", "Super, wie geht es dir?"]}

