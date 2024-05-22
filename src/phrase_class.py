import random

import config
import links


class Phrase:
    def __init__(self, variants, keywords, is_a_link=False, link=""):
        self.variants = variants
        self.keywords = keywords
        self.is_a_link = is_a_link
        self.link = link

    def say(self):
        return random.choice(self.variants[config.lang_short])

    def act(self):
        if self.is_a_link:
            links.open_link(self.link)
        return self.say()

    def check(self, text):
        for keyword in self.keywords[config.lang_short]:
            if keyword in text:
                return True
        return False

