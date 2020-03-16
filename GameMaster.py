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
    current_word = additional_upper(wordloader.load_word(language, difficulty, used_words).upper())
    used_words.append(current_word)
    used_letters = []
    cur_tries = 0
    return [word_hider(), used_letters, 0, score]


def update_game(letter):
    global cur_tries, used_letters, score
    letter = additional_upper(letter.upper())
    used_letters.append(letter.decode("utf-8"))
    hided_word = word_hider()
    if letter.decode("utf-8") not in current_word.decode("utf-8"):
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
    for l in current_word.decode("utf-8"):
        if l in used_letters or l.isspace():
            hided_word += l
        else:
            hided_word += "_"
    return hided_word


def additional_upper(word):
    word = word.replace("ą", "Ą")
    word = word.replace("ć", "Ć")
    word = word.replace("ę", "Ę")
    word = word.replace("ł", "Ł")
    word = word.replace("ń", "Ń")
    word = word.replace("ó", "Ó")
    word = word.replace("ś", "Ś")
    word = word.replace("ż", "Ż")
    word = word.replace("ź", "Ź")
    return word
