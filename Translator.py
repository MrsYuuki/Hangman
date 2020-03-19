import gettext
from os import getcwd

languages = {
    'en_US': gettext.translation('gui', localedir=getcwd() + '\\locale', languages=['en_US']),
    'pl_PL': gettext.translation('gui', localedir=getcwd()+'\\locale', languages=['pl_PL'])
}


def language_change(lang):
    return languages[lang]
