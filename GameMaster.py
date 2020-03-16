# coding=utf-8
import Word_Loader as wordloader

current_word = ""
used_letters = []
used_words = []
score = 0

cur_tries = 0
max_tries = 5


def initialize_game(difficulty=-1, language="Polish"):
    global cur_tries, current_word, used_letters, used_words, score
    current_word = additional_upper(wordloader.load_word(language, difficulty, used_words))
    used_words.append(current_word)
    used_letters = []
    cur_tries = 0
    return [word_hider(), used_letters, 0, score]


def update_game(letter):
    global cur_tries, used_letters, score
    letter = additional_upper(letter)
    used_letters.append(letter)
    hided_word = word_hider()
    if letter not in current_word:
        cur_tries += 1
    if "_" not in hided_word:  # win
        score += 1
        return [hided_word, used_letters, 1, score]
    elif cur_tries == max_tries:  # lose
        return [hided_word, used_letters, 2, score]
    return [hided_word, used_letters, 0, score]


def word_hider():
    global used_letters, current_word
    hided_word = ""
    for l in list(current_word):
        if l in used_letters or l.isspace():
            hided_word += l
        else:
            hided_word += "_"
    return hided_word


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
