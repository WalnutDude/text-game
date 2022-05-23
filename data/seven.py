import data.encryptor as encryptor
from os import system
from time import sleep
import data.death as death

def seven():

    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("7"))
    levelFile.close()

    difficultyFile = open("data/difficulty.dif", 'rb')
    difficulty = encryptor.decrypt(difficultyFile.readline())
    difficultyFile.close()

    wealthFile = open("data/stats/wealth.sts", 'rb')
    wealth = float(encryptor.decrypt(wealthFile.readline()))
    wealthFile.close()

    religionFile = open("data/stats/religion.sts", 'rb')
    religion = float(encryptor.decrypt(religionFile.readline()))
    religionFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'rb')
    lifestyle = float(encryptor.decrypt(lifestyleFile.readline()))
    lifestyleFile.close()

    death.checkDeath(wealth, religion, lifestyle)

    system("cls")

    print()
    print("      ▄▄▄▄▄▄▄▄▄")
    print("     ▐█████████▌")
    print("     ▐ > ███ < ▌")
    print("     ▐ ▐  █  ▌ ▌")
    print("     ▐         ▌")
    print("     ▐███ ─ ███▌")
    print("      ▀▀▀▀▀▀▀▀▀")
    print("      [General]\n")

    print("    The neighbouring kingdom must be dealt with, I have an assasin ready,\n    waiting for your orders.\n")

    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")
    print("    1 · Send the assasin, they will pay for their actions.\n")
    print("    2 · The financial condition of the kingdom is not yet stable, I don't\n        think its the right time to do it.\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == '1':
        if difficulty == 'easy':
            wealth -= 5
            lifestyle += 7.5
        elif difficulty == 'normal':
            wealth -= 10
            lifestyle += 15
        elif difficulty == 'hard':
            wealth -= 20
            lifestyle += 30
        else:
            wealth -= 10
            lifestyle += 15

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100


        wealthFile = open("data/stats/wealth.sts", 'wb')
        wealthFile.write(encryptor.encrypt(f"{wealth}"))
        wealthFile.close()

        lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
        lifestyleFile.write(encryptor.encrypt(f"{lifestyle}"))
        lifestyleFile.close()

    elif option == '2':
        wealth += 5
        lifestyle -= 10

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100

        wealthFile = open("data/stats/wealth.sts", 'wb')
        wealthFile.write(encryptor.encrypt(f"{wealth}"))
        wealthFile.close()

        lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
        lifestyleFile.write(encryptor.encrypt(f"{lifestyle}"))
        lifestyleFile.close()