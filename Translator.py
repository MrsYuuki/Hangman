import gettext
import locale
from os import getcwd

languages = {
    'en_US': gettext.translation('gui', localedir=getcwd() + '\\locale', languages=['en_US']),
    'pl_PL': gettext.translation('gui', localedir=getcwd()+'\\locale', languages=['pl_PL'])
}


def language_change(lang_code):
    if lang_code in languages:
        return languages[lang_code]
    return languages['en_US']


def basic_language():
    if locale.getdefaultlocale()[0] in languages:
        return languages[locale.getdefaultlocale()[0]], locale.getdefaultlocale()[0]
    return languages['en_US'], 'en_US'
