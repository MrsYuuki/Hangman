import Word_Loader as word

current_word = ""
used_letters = []
used_words = []
score = 0

max_tries = 5


def initialize_game(difficulty, language="Polish"):
    current_word = word.load_word(language, difficulty, used_words)
    used_letters = []


def update_game(letter):
    print(letter)
