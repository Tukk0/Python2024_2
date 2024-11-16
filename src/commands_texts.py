import config
Start = {'en': "Hello",
         'ru': "Здравствуйте",
         'de': "Hallo"}
Language_text = {'en': f'''
Available languages: {config.languages}
Please select one of them.
Example: /language english''',
                 'ru': f'''
Доступные языки: {config.languages}
Выберите один из них.
Пример: /language english''',
                 'de': f'''
Verfügbare Sprachen: {config.languages}
Wähle eine der beiden.
Beispiel: /language english'''}

Language_changed = {'en': "Language changed successfully",
                    'ru': "Язык успешно изменен",
                    'de': "Sprache geändert"}

