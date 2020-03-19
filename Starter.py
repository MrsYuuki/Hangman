import Hangman_GUI as GUI
import shelve


def start():
    d = shelve.open('score')
    try:
        score = d['score']
    except KeyError:
        d['score'] = 0
    d.close()

    GUI.launch_welcome_window()


start()
