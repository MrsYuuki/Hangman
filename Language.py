# coding=utf-8
class Language:
    def __init__(self, folder_name, display_name, lang_code, alphabet):
        self.folder_name = folder_name
        self.alphabet = alphabet
        self.display_name = display_name
        self.lang_code = lang_code

    def __str__(self):
        return self.display_name


def initialize_languages():
    return [
        Language("English", "English", "en_US", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]),
        Language("Polish", "Polish (polski)", "pl_PL", ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"])
    ]
