import os

path = os.path.abspath(".").replace("\\", "/")
iconpath = '"{}/icon.ico"'.format(path)
wordspath = '"{}/Words";"Words/"'.format(path)
localepath = '"{}/locale";"locale/"'.format(path)
imagespath = '"{}/images";"images/"'.format(path)
starterpath = '"{}/Starter.py"'.format(path)

os.system('pyinstaller -y -F -w -i {} '
          '--add-data {} '
          '--add-data {} '
          '--add-data {} '
          '--add-data {};'
          '"." -n Hangman {}'.format(iconpath, wordspath, localepath, imagespath, iconpath, starterpath))