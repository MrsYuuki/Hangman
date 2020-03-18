# coding=utf-8
class Language:
    folder_name=None
    display_name=None
    alphabet=None

    def __init__(self, folder_name, display_name, alphabet):
        self.folder_name = folder_name
        self.alphabet = alphabet
        self.display_name = display_name

    def __str__(self):
        return self.display_name


def initialize_languages():
    languages = []

    languages.append(Language("English", "English", ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]))
    languages.append(Language("Polish", "Polish (polski)", ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","ń","o","ó","p","r","s","ś","t","u","w","y","z","ź","ż"]))

    return languages
