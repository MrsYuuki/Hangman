from os import listdir, getcwd
from os.path import isfile, join
import random as rand

base_directory = "\\Words"
base_language = "Polish"


def load_word(language=base_language, difficulty=-1):
    chosen_category_path = __choose_category(language)
    with open(chosen_category_path) as p:
        words = p.readlines()
        if difficulty == -1:
            return words[rand.randint(0, len(words) - 1)].strip()
        return "unsupported"


def __choose_category(language):
    path = getcwd() + base_directory + "\\" + language
    category_files = [f for f in listdir(path) if isfile(join(path, f))]
    return join(path, category_files[rand.randint(0, len(category_files) - 1)])


print(load_word())