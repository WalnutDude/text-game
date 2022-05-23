from os import system
from time import sleep
import data.encryptor as encryptor
import data.one as one



def introduction():
    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("0"))
    levelFile.close()

    system("cls")

    
    print()
    print("     ██████████")
    print("     █░░░░░░░░█")
    print("     █░█░░░░█░█")
    print("     █░░░░░░░░█")
    print("     ██████████\n")


    print('     Hello.')
    sleep(1.5)
    print("     I'm here to explain the basics of the game.")
    sleep(1.5)
    print("     You are the emperor of a large empire, ")
    sleep(1.5)
    print("     you will have to choose between many decisions.")
    sleep(1.5)
    print("     You have 3 'stats'")
    sleep(1.5)
    print("     Wealth, Religion, Lifestyle")
    sleep(1.5)
    print("     Your decision will affect these stats.")
    sleep(1.5)
    print("     e.g - Building a temple will decrease Wealth, but increase Religion.")
    sleep(2)
    print("     If any of them gets too low, you might get dethroned.")
    sleep(1)

    print()
    print("·····························\n")
    print()

    input(" Press ENTER to continue...")
    one.one()