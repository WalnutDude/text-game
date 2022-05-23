from os import system
import data.menu as menu
import data.encryptor as encryptor
from os import path

system("mode con cols=83 lines=25")

if path.isfile("data/options.cfg") == False:
    optionsFile = open("data/options.cfg", 'w')
    optionsFile.write('dark')
    optionsFile.close()

if path.isfile("data/level.lvl") == False:
    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("-1"))
    levelFile.close()

if path.isfile("data/stats/wealth.sts") == False:
    levelFile = open('data/stats/wealth.sts', 'wb')
    levelFile.write(encryptor.encrypt("80"))
    levelFile.close()

if path.isfile("data/stats/religion.sts") == False:
    levelFile = open('data/stats/religion.sts', 'wb')
    levelFile.write(encryptor.encrypt("80"))
    levelFile.close()
    
if path.isfile("data/stats/lifestyle.sts") == False:
    levelFile = open('data/stats/lifestyle.sts', 'wb')
    levelFile.write(encryptor.encrypt("80"))
    levelFile.close()

menu.menu()