import data.encryptor as encryptor
from os import system
from random import randint
from time import sleep
import data.menu as menu

def wealthDeath():
    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("-1"))
    levelFile.close()

    wealthFile = open("data/stats/wealth.sts", 'wb')
    wealthFile.write(encryptor.encrypt("80"))
    wealthFile.close()
        
    religionFile = open("data/stats/religion.sts", 'wb')
    religionFile.write(encryptor.encrypt("80"))
    religionFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
    lifestyleFile.write(encryptor.encrypt("80"))
    lifestyleFile.close()

    system("cls")

    print()                                                 
    print("      ▄▄▄▄▄▄ ")  
    print("     █      █")                       
    print("     █ ▌  ▐ █")                       
    print("     ▀▄    ▄▀")                       
    print("      ▐    ▌ ")                        
    print("      ▐││││▌ ")                        
    print("       ▀▀▀▀  \n")
    sleep[1]                        
    print("\n·····························\n")

    print("     You were dethroned.")
    sleep[1]
    print('     Your empire, once rich and prosperous,')
    sleep[1]
    print("     now lies in debris,")
    sleep[1]
    print("     as the emperor fails to feed his population.")

    print("\n·····························\n")

    input("Press ENTER to continue...")
    menu.menu()

def religionDeath():
    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("-1"))
    levelFile.close()

    wealthFile = open("data/stats/wealth.sts", 'wb')
    wealthFile.write(encryptor.encrypt("80"))
    wealthFile.close()
        
    religionFile = open("data/stats/religion.sts", 'wb')
    religionFile.write(encryptor.encrypt("80"))
    religionFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
    lifestyleFile.write(encryptor.encrypt("80"))
    lifestyleFile.close()

    system("cls")

    print()                                                 
    print("      ▄▄▄▄▄▄ ")  
    print("     █      █")                       
    print("     █ ▌  ▐ █")                       
    print("     ▀▄    ▄▀")                       
    print("      ▐    ▌ ")                        
    print("      ▐││││▌ ")                        
    print("       ▀▀▀▀  \n")
    sleep[1]                        
    print("\n·····························\n")

    print("     You were dethroned.")
    sleep[1]
    print('     Your empire, once a pilgrim\'s hotspot,')
    sleep[1]
    print("     was destroyed by a tornado.")
    sleep[1]
    print("     It is said that the gods were in rage, for the emperor was a disloyal scum.")

    print("\n·····························\n")
    
    input("Press ENTER to continue...")
    menu.menu()

def lifestyleDeath():
    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("-1"))
    levelFile.close()

    wealthFile = open("data/stats/wealth.sts", 'wb')
    wealthFile.write(encryptor.encrypt("80"))
    wealthFile.close()
        
    religionFile = open("data/stats/religion.sts", 'wb')
    religionFile.write(encryptor.encrypt("80"))
    religionFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
    lifestyleFile.write(encryptor.encrypt("80"))
    lifestyleFile.close()

    system("cls")

    print()                                                 
    print("      ▄▄▄▄▄▄ ")  
    print("     █      █")                       
    print("     █ ▌  ▐ █")                       
    print("     ▀▄    ▄▀")                       
    print("      ▐    ▌ ")                        
    print("      ▐││││▌ ")                        
    print("       ▀▀▀▀  \n")
    sleep[1]                        
    print("\n·····························\n")

    print("     You were dethroned.")
    sleep[1]
    print('     Your highness, once rescpected by everyone')
    sleep[1]
    print("     now lies in contempt,")
    sleep[1]
    print("     for the king was full of greed.")

    print("\n·····························\n")
    
    input("Press ENTER to continue...")
    menu.menu()

def checkDeath(wealth, religion, lifestyle):
    
    if wealth >= 40:
        pass
    elif wealth == 0:
        wealthDeath()

    elif wealth < 10:
        chance = randint(1, 100)
        if chance <= 75:
            wealthDeath()
    elif wealth < 20:
        chance = randint(1, 2)
        if chance == '1':
            wealthDeath()
    elif wealth < 30:
        chance = randint(1, 5)
        if chance == 3:
            wealthDeath()
    elif wealth < 40:
        chance = randint(1, 10)
        if chance == 7:
            wealthDeath()

    if religion >= 40:
        pass
    elif religion == 0:
        religionDeath()
        
    elif religion < 10:
        chance = randint(1, 100)
        if chance <= 75:
            religionDeath()
    elif religion < 20:
        chance = randint(1, 2)
        if chance == 1:
            religionDeath()
    elif religion < 30:
        chance = randint(1, 5)
        if chance == 3:
            religionDeath()
    elif religion < 40:
        chance = randint(1, 10)
        if chance == 7:
            religionDeath()

    if lifestyle >= 40:
        pass
    elif lifestyle == 0:
        lifestyleDeath()
        
    elif lifestyle < 10:
        chance = randint(1, 100)
        if chance <= 75:
            lifestyleDeath()
    elif lifestyle < 20:
        chance = randint(1, 2)
        if chance == 1:
            lifestyleDeath()
    elif lifestyle < 30:
        chance = randint(1, 5)
        if chance == 3:
            lifestyleDeath()
    elif lifestyle < 40:
        chance = randint(1, 10)
        if chance == 7:
            lifestyleDeath()
