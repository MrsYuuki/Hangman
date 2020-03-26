import os

os.system('pyinstaller -y -F -w -i "D:/Repos/Hangman/icon.ico" '
          '--add-data "D:/Repos/Hangman/Words";"Words/" '
          '--add-data "D:/Repos/Hangman/locale";"locale/" '
          '--add-data "D:/Repos/Hangman/images";"images/" '
          '--add-data "D:/Repos/Hangman/icon.ico";'
          '"." -n Hangman  "D:/Repos/Hangman/Starter.py"')
