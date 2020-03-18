# coding=utf-8
from os import listdir, getcwd
from os.path import isfile, join
import random as rand

base_directory = "\\Words"
base_language = "Polish"

normal_diff = 6
hard_diff = 10


# difficulty: -1 random; 0 easy; 1 normal; 2 hard
def load_word(language=base_language, difficulty=-1, used_words=[]):
    all_words = __load_words_lang(language, used_words)
    words = [w for w in all_words if w[0] not in used_words]
    if len(words) == 0:
        words = all_words
    if difficulty == -1:
        return words[rand.randint(0, len(words) - 1)]
    return __word_by_difficulty(words, difficulty)


def __word_by_difficulty(words, difficulty):
    if difficulty not in [0, 1, 2]:
        return "unsupported"

    if difficulty == 2:
        nwords = [w for w in words if len(w[0]) >= hard_diff]
        if len(nwords) == 0:
            difficulty = 1
    if difficulty == 1:
        nwords = [w for w in words if normal_diff <= len(w[0]) < hard_diff]
        if len(nwords) == 0:
            difficulty = 0
    if difficulty == 0:
        nwords = [w for w in words if len(w[0]) < normal_diff]
    return nwords[rand.randint(0, len(nwords) - 1)]


def __load_words_lang(language, used_words):
    path = getcwd() + base_directory + "\\" + language
    category_files = [f for f in listdir(path) if isfile(join(path, f))]
    all_words = []
    for cat in category_files:
        with open(join(path, cat), encoding='utf-8') as p:
            for w in p.readlines():
                all_words.append((w, cat))
    return all_words
