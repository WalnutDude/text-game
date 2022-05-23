import data.encryptor as encryptor
from os import system
import data.two as two
from time import sleep
import data.death as death

def one():
    
    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("1"))
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
    print("     ███████████")
    print("     █  ▀▀▀  ▀ █")
    print("     █ ▐     ▌ █")
    print("     █         █")
    print("     █  ─────  █")
    print("      ▀▀▀▀▀▀▀▀▀")
    print("      [Peasant]\n  ")

    print("    Your majesty, as you may know the crops were not able to grow due to\n    the drought, could you please reduce the taxes this harvest?\n")

    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print()
    print("·····························\n")
    print("    1 · Sure\n")
    print("    2 · Sorry\n\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == "1":
        
        if difficulty == 'easy':
            wealth -= 7.5
            lifestyle += 5
        elif difficulty == 'normal':
            wealth -= 15
            lifestyle += 10
        elif difficulty == 'hard':
            wealth -= 30
            lifestyle += 20
        else:
            wealth -= 15
            lifestyle += 10

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

        two.two()

    elif option == "2":
        if difficulty == 'easy':
            lifestyle -= 5
            wealth += 5
        elif difficulty == 'normal':
            lifestyle -= 10
            wealth += 10
        elif difficulty == 'hard':
            lifestyle -= 20
            wealth += 20
        else:
            lifestyle -= 10
            wealth += 10

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

        two.two()

    elif option.lower() == 'exit':
        system("cls")
        exit()
        