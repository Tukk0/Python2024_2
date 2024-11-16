import keywords
import links
import phrase_class as pc
import phrase_variants as pv


Greting = pc.Phrase(pv.Greeting, keywords.Greeting)
Farewell = pc.Phrase(pv.Farewell, keywords.Farewell)
Language = pc.Phrase(pv.Language, keywords.Language)
Feeling = pc.Phrase(pv.Feeling, keywords.Feeling)
Youtube = pc.Phrase(pv.Links, keywords.Youtube, True, links.youtube_link)
Google = pc.Phrase(pv.Links, keywords.Google, True, links.google_link)
Mipt = pc.Phrase(pv.Links, keywords.Mipt, True, links.mipt_link)
Github = pc.Phrase(pv.Links, keywords.Github, True, links.github_link)

phrases = [Greting, Farewell, Language, Feeling, Youtube, Google, Mipt, Github]


def checkall(text):
    phrases_list = []
    for phrase in phrases:
        if phrase.check(text):
            phrases_list.append(phrase)
    if len(phrases_list) == 0:
        return None
    return phrases_list

