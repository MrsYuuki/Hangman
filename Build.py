import os

path = os.path.abspath(".").replace("\\", "/")
iconpath = '"{}/icon.ico"'.format(path)
wordspath = '"{}/Words";"Words/"'.format(path)
localepath = '"{}/locale";"locale/"'.format(path)
imagespath = '"{}/images";"images/"'.format(path)

os.system('pyinstaller -y -F -w -i {} '
          '--add-data {} '
          '--add-data {} '
          '--add-data {} '
          '--add-data {};'
          '"." -n Hangman "D:/Repos/Hangman/Starter.py"'.format(iconpath, wordspath, localepath, imagespath, iconpath))