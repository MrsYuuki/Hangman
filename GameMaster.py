import Hangman_GUI as GUI
import Word_Loader as word


def start_game():
    elo = GUI.launch_welcome_window()
    print(elo)



def chosen_difficulty(window, difficulty):
    window.destroy()
    elo = GUI.launch_main_window()
    print(elo)

start_game()
