import data.encryptor as encryptor
from os import system
import data.five as five
from time import sleep
import data.death as death

def four():

    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("4"))
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
    print("      ▄▄▄▄▄▄▄▄▄▄")
    print("     ▐   ════   ▌")
    print("     ▐  >    <  ▌")
    print("     ▐  ▐    ▌  ▌")
    print("     ▐    ──    ▌")
    print("     ▐    ██    ▌")
    print("      ▀▀▀▀▀▀▀▀▀▀")
    print("       [Priest] \n")

    print("    Your majesty, the people of the other community are interfering in our\n    prayers! We've had enough and need your support!\n")

    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")
    print("    1 · You have my full support.\n")
    print("    2 · You're not going to do anything, co-existence is the key.\n\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == '1':

        if difficulty == 'easy':
            wealth -= 2.5
            religion += 10
            lifestyle -= 7.5
        elif difficulty == 'normal':
            wealth -= 5
            religion += 20
            lifestyle -= 15
        elif difficulty == 'hard':
            wealth -= 10
            religion += 40
            lifestyle -= 30
        else:
            wealth -= 5
            religion += 20
            lifestyle -= 15

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100

        wealthFile = open("data/stats/wealth.sts", 'wb')
        wealthFile.write(encryptor.encrypt(f"{wealth}"))
        wealthFile.close()
        
        religionFile = open("data/stats/religion.sts", 'wb')
        religionFile.write(encryptor.encrypt(f"{religion}"))
        religionFile.close()

        lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
        lifestyleFile.write(encryptor.encrypt(f"{lifestyle}"))
        lifestyleFile.close()
        five.five()

    elif option == '2':
        if difficulty == 'easy':
            religion -= 10
            lifestyle += 5
        elif difficulty == 'normal':
            religion -= 20
            lifestyle += 10
        elif difficulty == 'hard':
            religion -= 40
            lifestyle += 20
        else:
            religion -= 20
            lifestyle += 10

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100

        religionFile = open("data/stats/religion.sts", 'wb')
        religionFile.write(encryptor.encrypt(f"{religion}"))
        religionFile.close()

        lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
        lifestyleFile.write(encryptor.encrypt(f"{lifestyle}"))
        lifestyleFile.close()
        five.five()

    elif option.lower() == 'exit':
        system("cls")
        exit()