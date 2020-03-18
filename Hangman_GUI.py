# coding=utf-8
from tkinter import *
from tkinter import messagebox
import GameMaster as master
import Language as lang

main_window = None
word_label = None
score_label = None
tries_label = None
category_label = None
cur_diff = None
cur_lang = None


def launch_main_window(window, difficulty, language):
    global main_window, word_label, score_label, tries_label, category_label, cur_diff, cur_lang

    cur_diff = difficulty
    cur_lang = language
    word_settings = master.initialize_game(cur_diff, cur_lang.folder_name)                                              #Slowo, lista liter, stan gry
    if window is not None:
        window.destroy()

    main_window = Tk()
    main_window.title("3, 2, 1... Hangman!")
    main_window.geometry('500x500')
    main_window.resizable(0, 0)
    main_window.focus_force()

    windowWidth2 = 500
    windowHeight2 = 500
    positionRight2 = int(main_window.winfo_screenwidth() / 2 - windowWidth2 / 2)          # Gets both half the screen width/height and window width/height
    positionDown2 = int(main_window.winfo_screenheight() / 2 - windowHeight2 / 2)
    main_window.geometry("+{}+{}".format(positionRight2, positionDown2))                  # Positions the window in the center of the page.

    launch_alphabet(main_window, cur_lang.alphabet)

    word_label = Label(main_window, text=split_word_to_view(word_settings[0]), font=("Times new roman", 25))
    word_label.pack()
    word_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    score_label = Label(main_window, text="Score: " + str(word_settings[3]), font=("Times new roman", 15))
    score_label.pack()
    score_label.place(relx=0.8, rely=0.1, anchor=CENTER)

    category_label = Label(main_window, text=word_settings[6], font=("Times new roman", 15))
    category_label.pack()
    category_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    tries_label = Label(main_window, text=str(word_settings[5]) + "/" + str(word_settings[4]), font=("Times new roman", 15))
    tries_label.pack()
    tries_label.place(relx=0.5, rely=0.15, anchor=CENTER)

    main_window.mainloop()


def update_main_window(letter):
    global score_label, word_label, tries_label
    info = master.update_game(letter)
    word_label.configure(text=split_word_to_view(info[0]))
    score_label.configure(text="Score: " + str(info[3]))
    tries_label.configure(text=str(info[5]) + "/" + str(info[4]))

    if info[2] == 1:
        messagebox.showinfo('3, 2, 1... Win!', 'Correct!\nGet ready for the next word...')
        launch_main_window(main_window, cur_diff, cur_lang)
    if info[2] == 2:
        messagebox.showinfo('3, 2, 1... Lose!', 'You lose!\nFinal score: ' + str(info[3]))
        main_window.destroy()
        master.reset_game()
        launch_welcome_window()


def split_word_to_view(word):
    view_word = ""
    for letter in list(word):
        view_word = view_word+letter+" "
    return view_word


def launch_welcome_window():
    welcome_window = Tk()
    welcome_window.title("Hangman")
    welcome_window.geometry('300x250')

    windowWidth = welcome_window.winfo_reqwidth()                                           # Gets the requested values of the height and widht.
    windowHeight = welcome_window.winfo_reqheight()

    positionRight = int(welcome_window.winfo_screenwidth() / 2 - windowWidth / 2)           # Gets both half the screen width/height and window width/height
    positionDown = int(welcome_window.winfo_screenheight() / 2 - windowHeight / 2)

    welcome_window.geometry("+{}+{}".format(positionRight, positionDown))                   # Positions the window in the center of the page.

    welcome_window.resizable(0, 0)

    languages = lang.initialize_languages()

    welcome_label = Label(welcome_window, text="Hangman!\nChoose difficulty\n", font=("Times new roman", 16))
    welcome_label.pack()
    welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

    first_button = Button(welcome_window, text="Easy", font=("Times new roman", 14), command=lambda: launch_main_window(welcome_window, 0, languages[1]), height=1, width=10)
    first_button.pack()
    first_button.place(relx=0.5, rely=0.3, anchor=CENTER)

    second_button = Button(welcome_window, text="Medium", font=("Times new roman", 14), command=lambda: launch_main_window(welcome_window, 1, languages[1]), height=1, width=10)
    second_button.pack()
    second_button.place(relx=0.5, rely=0.55, anchor=CENTER)

    third_button = Button(welcome_window, text="Hard", font=("Times new roman", 14), command=lambda: launch_main_window(welcome_window, 2, languages[1]), height=1, width=10)
    third_button.pack()
    third_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    welcome_window.mainloop()


def launch_alphabet(window, alphabet):
    buttons = []
    x = 0.15
    y = 0.6
    length = 0
    for letter in alphabet:
        if length != 7:
            buttons.append(Button(window, text=letter, font=("Times new roman", 18), command=lambda let=letter: update_main_window(let), height=1, width=3))
            buttons[-1].pack()
            buttons[-1].place(relx=x, rely=y, anchor=CENTER)
            x += 0.1
            length += 1
        else:
            buttons.append(Button(window, text=letter, font=("Times new roman", 18), command=lambda let=letter: update_main_window(let), height=1, width=3))
            buttons[-1].pack()
            buttons[-1].place(relx=x, rely=y, anchor=CENTER)
            x = 0.15
            y += 0.1
            length = 0
