# coding=utf-8
import Word_Loader as wordloader
import string
import sys
import os

current_word = None
used_letters = []
used_words = []
score = 0

cur_tries = 0
max_tries = 7

switcher = {
    "Ą": "A",
    "Ć": "C",
    "Ę": "E",
    "Ł": "L",
    "Ń": "N",
    "Ó": "O",
    "Ś": "S",
    "Ż": "Z",
    "Ź": "Z",
    "ą": "a",
    "ć": "c",
    "ę": "e",
    "ł": "l",
    "ń": "n",
    "ó": "o",
    "ś": "s",
    "ż": "z",
    "ź": "z",
}


def initialize_game(difficulty=-1, language="Polish"):
    global cur_tries, current_word, used_letters, used_words, score
    loaded_word = wordloader.load_word(language, difficulty, used_words)
    if loaded_word[0] in used_words:
        used_words = []
    used_words.append(loaded_word[0])
    current_word = additional_upper(loaded_word[0].strip())
    used_letters = []
    cur_tries = 0
    return [word_hider(), used_letters, 0, score, max_tries, max_tries - cur_tries, loaded_word[1].split(".")[0]]


def update_game(letter):
    global cur_tries, used_letters, score
    letter = additional_upper(letter)
    used_letters.append(letter)
    hided_word = word_hider()
    if letter not in current_word:
        cur_tries += 1
    else:
        score += current_word.count(letter)

    if "_" not in hided_word:  # win
        score += 10 * len(used_words)
        return [hided_word, used_letters, 1, score, max_tries, max_tries - cur_tries]
    elif cur_tries == max_tries:  # lose
        return [hided_word, used_letters, 2, score, max_tries, max_tries - cur_tries]
    return [hided_word, used_letters, 0, score, max_tries, max_tries - cur_tries]


def reset_game():
    global used_words, score
    used_words = []
    score = 0


def word_hider():
    global used_letters, current_word
    hidden_word = ""
    for l in list(current_word):
        if l in used_letters or l.isspace():
            hidden_word += l
        else:
            hidden_word += "_"
    return hidden_word


def additional_upper(word):
    return word.upper()\
        .replace("ą", "Ą")\
        .replace("ć", "Ć")\
        .replace("ę", "Ę")\
        .replace("ł", "Ł")\
        .replace("ń", "Ń")\
        .replace("ó", "Ó")\
        .replace("ś", "Ś")\
        .replace("ż", "Ż")\
        .replace("ź", "Ź")


def additional_sort_key(letter):
    if letter in string.ascii_letters:
        return ord(letter)
    if letter in switcher:
        return 0.5 + ord(switcher[letter])
    return -1


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return base_path + relative_path