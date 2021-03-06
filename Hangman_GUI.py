# coding=utf-8
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Translator as translate
import GameMaster as master
import Language as lang
import shelve

main_window = None
root = None
welcome_window = None
welcome_root = None
word_label = None
score_label = None
tries_label = None
category_label = None
used_letters_label = None
cur_diff = None
cur_lang = None
alphabet_buttons = None
used_letters = None
canvas = None
image = None

cur_word = None
cur_score = None

welcome_x = None
welcome_y = None
main_x = None
main_y = None

t, lang_code = translate.basic_language()
t.install()
_ = t.gettext


def launch_main_window(windows, difficulty, language):
    global root, main_window, word_label, score_label, tries_label, category_label, used_letters_label, cur_diff, cur_lang, used_letters, canvas, image, cur_word, cur_score

    used_letters = []
    cur_diff = difficulty
    cur_lang = language
    cur_score = 0
    word_settings = master.initialize_game(cur_diff, cur_lang.folder_name)                                              #Slowo, lista liter, stan gry

    for w in windows:
        w.destroy()

    root = Tk()
    root.title(_("3, 2, 1... Hangman!"))
    root.attributes("-alpha", 0.0)
    root.iconbitmap(master.resource_path("/icon.ico"))

    main_window = Toplevel(root)
    main_window.overrideredirect(1)
    main_window.geometry('1200x700')
    main_window.configure(background="black")
    main_window.resizable(0, 0)
    main_window.focus_force()

    root.bind("<Unmap>", lambda x: main_window.withdraw())
    root.bind("<Map>", lambda x: main_window.deiconify())

    main_window.bind("<Key>", key_pressed_game)
    main_window.bind("<ButtonPress-1>", StartMoveMain)
    main_window.bind("<ButtonRelease-1>", StopMove)
    main_window.bind("<B1-Motion>", OnMotionMain)

    windowWidth2 = 1200
    windowHeight2 = 700
    positionRight2 = int(main_window.winfo_screenwidth() / 2 - windowWidth2 / 2)          # Gets both half the screen width/height and window width/height
    positionDown2 = int(main_window.winfo_screenheight() / 2 - windowHeight2 / 2)
    main_window.geometry("+{}+{}".format(positionRight2, positionDown2))                  # Positions the window in the center of the page.

    launch_alphabet(main_window, cur_lang.alphabet)

    word_label = Label(main_window, text=split_word_to_view(word_settings[0]), font=("Courier new", 20), bg="black", fg="white")
    word_label.pack()
    word_label.place(relx=0.775, rely=0.3, anchor=CENTER)

    surrender_button = Button(main_window, text=_("Surrender"), font=("Courier new", 14), command=lambda: lose_game(), height=1, width=10, bg="grey")
    surrender_button.pack()
    surrender_button.place(relx=0.9, rely=0.05, anchor=CENTER)

    score_label = Label(main_window, text=_("Score:") + ' ' + str(word_settings[3]), font=("Courier new", 15), bg="black", fg="white")
    score_label.pack()
    score_label.place(relx=0.9, rely=0.15, anchor=CENTER)

    category_label = Label(main_window, text=word_settings[6], font=("Courier new", 15), bg="black", fg="white")
    category_label.pack()
    category_label.place(relx=0.775, rely=0.4, anchor=CENTER)

    used_letters_label = Label(main_window, text="", font=("Courier new", 15), bg="black", fg="white")
    used_letters_label.pack()
    used_letters_label.place(relx=0.775, rely=0.5, anchor=CENTER)

    tries_label = Label(main_window, text=str(word_settings[5]) + "/" + str(word_settings[4]), font=("Courier new", 25), bg="black", fg="white")
    tries_label.pack()
    tries_label.place(relx=0.25, rely=0.05, anchor=CENTER)

    canvas = Canvas(main_window, width=642, height=642, highlightthickness=0)
    canvas.pack()
    canvas.place(relx=0.0, rely=0.1)
    image = PhotoImage(file=master.resource_path("/images/%s.png" % str(8 - word_settings[5])))
    canvas.create_image(0, 0, anchor=NW, image=image)

    cur_word = word_settings[7]

    main_window.mainloop()


def newword_main_window():
    global root, main_window, word_label, score_label, tries_label, category_label, used_letters_label, cur_diff, cur_lang, used_letters, canvas, image, alphabet_button, cur_word
    info = master.initialize_game(cur_diff, cur_lang.folder_name)
    word_label.configure(text=split_word_to_view(info[0]))
    tries_label.configure(text=str(info[5]) + "/" + str(info[4]))
    used_letters = info[1]
    used_letters_label.configure(text=sorted(list(used_letters), key=master.additional_sort_key))
    category_label.configure(text=info[6])

    cur_word = info[7]

    canvas.delete(image)
    image = PhotoImage(file=master.resource_path("/images/%s.png" % str(8 - info[5])))
    canvas.create_image(0, 0, anchor=NW, image=image)

    for b in alphabet_buttons:
        b.destroy()
    launch_alphabet(main_window, cur_lang.alphabet)


def update_main_window(letter):
    global score_label, word_label, tries_label, used_letters_label, alphabet_buttons, used_letters, image, cur_score
    info = master.update_game(letter)
    word_label.configure(text=split_word_to_view(info[0]))
    cur_score = info[3]
    score_label.configure(text=_("Score:") + " " + str(info[3]))
    tries_label.configure(text=str(info[5]) + "/" + str(info[4]))
    used_letters = info[1]
    used_letters_label.configure(text=sorted(list(used_letters), key=master.additional_sort_key))

    canvas.delete(image)
    image = PhotoImage(file=master.resource_path("/images/%s.png" % str(8 - info[5])))
    canvas.create_image(0, 0, anchor=NW, image=image)

    [b for b in alphabet_buttons if b['text'] == letter][0]['state'] = DISABLED

    if info[2] == 1:
        messagebox.showinfo(_('3, 2, 1... Win!'), _('Correct!') + '\n' + _('Get ready for the next word...'))
        newword_main_window()
    if info[2] == 2:
        lose_game()


def lose_game():
    global main_window, root
    d = shelve.open('data')
    highscore = d['score']
    if cur_score > highscore:
        d['score'] = cur_score
        messagebox.showinfo(_('3, 2, 1... Lose!'),
                            _('New high score!') + '\n\n' + _('It was... ') + cur_word + '\n' + _('Final score:') + ' ' + str(cur_score))
    else:
        messagebox.showinfo(_('3, 2, 1... Lose!'),
                            _('You lose!') + '\n\n' + _('It was... ') + cur_word + '\n' + _('Final score:') + ' ' + str(cur_score))
    d.close()
    main_window.destroy()
    root.destroy()
    master.reset_game()
    launch_welcome_window()


def key_pressed_game(event):
    global cur_lang, used_letters
    if event.char in cur_lang.alphabet and master.additional_upper(event.char) not in used_letters:
        update_main_window(event.char)


def split_word_to_view(word):
    view_word = ""
    for letter in list(word):
        view_word = view_word+letter+" "
    return view_word


def launch_welcome_window(windows=None):
    global welcome_window, welcome_root, lang_code

    if windows is not None:
        for w in windows:
            w.destroy()

    welcome_root = Tk()
    welcome_root.title(_("Hangman"))
    welcome_root.attributes("-alpha", 0.0)
    welcome_root.iconbitmap(master.resource_path("/icon.ico"))

    welcome_window = Toplevel(welcome_root)
    welcome_window.overrideredirect(1)
    welcome_window.geometry('300x250')
    welcome_window.configure(bg="grey")
    welcome_window.focus_force()

    welcome_root.bind("<Unmap>", lambda x: welcome_window.withdraw())
    welcome_root.bind("<Map>", lambda x: welcome_window.deiconify())

    welcome_window.bind("<ButtonPress-1>", StartMoveWelcome)
    welcome_window.bind("<ButtonRelease-1>", StopMove)
    welcome_window.bind("<B1-Motion>", OnMotionWelcome)

    windowWidth = welcome_window.winfo_reqwidth()                                           # Gets the requested values of the height and widht.
    windowHeight = welcome_window.winfo_reqheight()

    positionRight = int(welcome_window.winfo_screenwidth() / 2 - windowWidth / 2)           # Gets both half the screen width/height and window width/height
    positionDown = int(welcome_window.winfo_screenheight() / 2 - windowHeight / 2)

    welcome_window.geometry("+{}+{}".format(positionRight, positionDown))                   # Positions the window in the center of the page.

    welcome_window.resizable(0, 0)

    languages = lang.initialize_languages()

    languages_list = ttk.Combobox(welcome_window, values=languages)
    languages_list.pack()
    languages_list.current(languages.index([l for l in languages if l.lang_code == lang_code][0]))
    languages_list.bind("<<ComboboxSelected>>", lambda x: language_changed([l for l in languages if l.display_name == languages_list.get()][0]))
    languages_list.place(relx=0.5, rely=0.95, anchor=E)

    welcome_label = Label(welcome_window, text=_("Hangman!") + "\n" + _("Choose difficulty") + "\n", font=("Courier new", 16), bg="grey")
    welcome_label.pack()
    welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

    d = shelve.open('data')
    score_label = Label(welcome_window, text=_("High Score:") + ' ' + str(d['score']), font=("Times new roman", 13), bg="grey")
    score_label.pack()
    score_label.place(relx=0.65, rely=0.95, anchor=W)
    d.close()

    first_button = Button(welcome_window, text=_("Easy"), font=("Courier new", 14), command=lambda: launch_main_window([welcome_window, welcome_root], 0, [l for l in languages if l.display_name == languages_list.get()][0]), height=1, width=10, bg="grey")
    first_button.pack()
    first_button.place(relx=0.5, rely=0.30, anchor=CENTER)

    second_button = Button(welcome_window, text=_("Medium"), font=("Courier new", 14), command=lambda: launch_main_window([welcome_window, welcome_root], 1, [l for l in languages if l.display_name == languages_list.get()][0]), height=1, width=10, bg="grey")
    second_button.pack()
    second_button.place(relx=0.5, rely=0.45, anchor=CENTER)

    third_button = Button(welcome_window, text=_("Hard"), font=("Courier new", 14), command=lambda: launch_main_window([welcome_window, welcome_root], 2, [l for l in languages if l.display_name == languages_list.get()][0]), height=1, width=10, bg="grey")
    third_button.pack()
    third_button.place(relx=0.5, rely=0.60, anchor=CENTER)

    exit_button = Button(welcome_window, text=_("Exit"), font=("Courier new", 14), command=lambda: welcome_root.destroy(), height=1, width=10, bg="grey")
    exit_button.pack()
    exit_button.place(relx=0.5, rely=0.80, anchor=W)

    welcome_window.mainloop()


def StartMoveWelcome(event):
    global welcome_x, welcome_y
    welcome_x = event.x
    welcome_y = event.y


def StartMoveMain(event):
    global main_x, main_y
    main_x = event.x
    main_y = event.y


def StopMove(event):
    global welcome_x, welcome_y, main_x, main_y
    welcome_x = None
    welcome_y = None
    main_x = None
    main_y = None


def OnMotionWelcome(event):
    deltax = event.x - welcome_x
    deltay = event.y - welcome_y
    x = welcome_window.winfo_x() + deltax
    y = welcome_window.winfo_y() + deltay
    welcome_window.geometry("+%s+%s" % (x, y))


def OnMotionMain(event):
    deltax = event.x - main_x
    deltay = event.y - main_y
    x = main_window.winfo_x() + deltax
    y = main_window.winfo_y() + deltay
    main_window.geometry("+%s+%s" % (x, y))


def launch_alphabet(window, alphabet):
    global alphabet_buttons
    alphabet_buttons = []
    x = 0.6
    y = 0.6
    length = 0
    for letter in alphabet:
        alphabet_buttons.append(Button(window, text=letter, font=("Courier new", 18), foreground="white", background="black", command=lambda let=letter: update_main_window(let), height=1, width=3))
        alphabet_buttons[-1].pack()
        alphabet_buttons[-1].place(relx=x, rely=y, anchor=CENTER)
        if length != 7:
            x += 0.05
            length += 1
        else:
            x = 0.6
            y += 0.08
            length = 0


def language_changed(language):
    global t, _, welcome_window, welcome_root, lang_code
    t = translate.language_change(language.lang_code)
    t.install()
    _ = t.gettext
    welcome_window.destroy()
    welcome_root.destroy()
    lang_code = language.lang_code
    launch_welcome_window()
