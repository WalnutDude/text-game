import data.encryptor as encryptor
from os import system
import data.four as four
from time import sleep
import data.death as death

def three():
    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("3"))
    levelFile.close()

    difficultyFile = open("data/difficulty.dif", 'rb')
    difficulty = encryptor.decrypt(difficultyFile.readline())
    difficultyFile.close()

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
    print("     ▐════╬════▌") 
    print("     ▐    ▀    ▌")
    print("     ▐ ▐     ▌ ▌")
    print("     ▐         ▌")
    print("     ▐│  ▀▀▀  │▌")
    print("      ▀▀▀▀▀▀▀▀▀")
    print("     [Treasurer]\n")

    print("    Your majesty, wealth is something we'd always need, would you consider\n    increasing the taxes?\n")
    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")
    print("    1 · No, the drought has already brought enough problems for the people.\n")
    print("    2 · Okay, increase it slightly.\n")
    print("    3 · I agree. Increase the tax greatly, we need to keep the empire running.\n")

    sleep(3)

    while option != '1' or option != '2' or option != '3' or option.lower() != 'exit':
        option = input("  Select an option (1, 2 or 3):  ")
        if option == '1' or option == '2' or option == '3' or option.lower() == 'exit':
            break

    if option == '1':

        if difficulty == 'easy':
            wealth -= 2.5
            lifestyle += 2.5
        elif difficulty == 'normal':
            wealth -= 5
            lifestyle += 5
        elif difficulty == 'hard':
            wealth -= 10
            lifestyle += 10
        else:
            wealth -= 5
            lifestyle += 5

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
        four.four()

    elif option == '2':

        if difficulty == 'easy':
            wealth += 5
            lifestyle -= 5
        elif difficulty == 'normal':
            wealth += 10
            lifestyle -= 10
        elif difficulty == 'hard':
            wealth += 20
            lifestyle -= 30
        else:
            wealth += 10
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
        four.four()

    elif option == '3':

        if difficulty == 'easy':
            wealth += 10
            lifestyle -= 10
        elif difficulty == 'normal':
            wealth += 20
            lifestyle -= 20
        elif difficulty == 'hard':
            wealth += 40
            lifestyle -= 40
        else:
            wealth += 20
            lifestyle -= 20

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
        four.four()

    elif option.lower() == 'exit':
        system("cls")
        exit()
