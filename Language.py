# coding=utf-8
class Language:
    folder_name=None
    alphabet=None

    def __init__(self, folder_name, alphabet):
        self.folder_name = folder_name
        self.alphabet = alphabet

    def __str__(self):
        return self.folder_name


def initialize_languages():
    languages = []

    languages.append(Language("English", ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]))
    languages.append(Language("Polish", ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","ń","o","ó","p","r","s","ś","t","u","w","y","z","ź","ż"]))

    return languages
