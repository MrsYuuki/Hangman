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
    chosen_category_path = __choose_category(language)
    with open(chosen_category_path) as p:
        words = [w for w in p.readlines() if w not in used_words]
        if len(words) == 0:
            return load_word(language, difficulty, used_words)
        if difficulty == -1:
            return words[rand.randint(0, len(words) - 1)].strip()
        return __word_by_difficulty(words, difficulty)


def __word_by_difficulty(words, difficulty):
    if difficulty not in [0, 1, 2]:
        return "unsupported"

    if difficulty == 2:
        nwords = [w for w in words if len(w) >= hard_diff]
        if len(nwords) == 0:
            difficulty = 1
    if difficulty == 1:
        nwords = [w for w in words if normal_diff <= len(w) < hard_diff]
        if len(nwords) == 0:
            difficulty = 0
    if difficulty == 0:
        nwords = [w for w in words if len(w) < normal_diff]
    return nwords[rand.randint(0, len(nwords) - 1)].strip()


def __choose_category(language):
    path = getcwd() + base_directory + "\\" + language
    category_files = [f for f in listdir(path) if isfile(join(path, f))]
    return join(path, category_files[rand.randint(0, len(category_files) - 1)])
