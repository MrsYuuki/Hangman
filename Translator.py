import gettext
import locale
import shelve
import GameMaster as master

languages = {
    'en_US': gettext.translation('gui', localedir=master.resource_path('\\locale'), languages=['en_US']),
    'pl_PL': gettext.translation('gui', localedir=master.resource_path('\\locale'), languages=['pl_PL'])
}


def language_change(lang_code):
    if lang_code in languages:
        d = shelve.open('data')
        d['lang'] = lang_code
        return languages[lang_code]
    return languages['en_US']


def basic_language():
    d = shelve.open('data')
    try:
        lang_code = d['lang']
    except KeyError:
        if locale.getdefaultlocale()[0] in languages:
            lang_code = locale.getdefaultlocale()[0]
        else:
            lang_code = 'en_US'
        d['lang'] = lang_code
    d.close()

    return languages[lang_code], lang_code
