import Hangman_GUI as GUI
import Word_Loader as word


def start_game():
    GUI.launch_welcome_window()



def chosen_difficulty(window, difficulty):
    window.destroy()
    GUI.launch_main_window()

start_game()
