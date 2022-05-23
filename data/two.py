from time import sleep
import data.encryptor as encryptor
from os import system
import data.three as three
import data.death as death

def two():
    
    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("2"))
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
    print("     ▐          ▌")
    print("     ▐  ▐    ▌  ▌")
    print("     ▐    ──    ▌")
    print("     ▐    ██    ▌")
    print("      ▀▀▀▀▀▀▀▀▀▀")
    print("       [Priest] \n")

    print("    Your majesty, as you already know the drought this year has been a huge\n    problem, I suggest we make a new temple to ask the gods to pour the rain\n    upon us. Do you agree?\n")

    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")
    print("    1 · Only the gods can do something about this. Make the temple.\n")
    print("    2 · God always helps a good willed person, there is no need for a temple.\n\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == "1":
        if difficulty == 'easy':
            wealth -= 7.5
            religion += 7.5
        elif difficulty == 'normal':
            wealth -= 15
            religion += 15
        elif difficulty == 'hard':
            wealth -= 30
            religion += 30
        else:
            wealth -= 15
            religion += 15

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
        three.three()

    elif option == "2":
        if difficulty == 'easy':
            religion -= 5
        elif difficulty == 'normal':
            religion -= 10
        elif difficulty == 'hard':
            religion -= 20
        else:
            religion -= 10

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100
            
        religionFile = open("data/stats/religion.sts", 'wb')
        religionFile.write(encryptor.encrypt(f"{religion}"))
        religionFile.close()
        three.three()

    elif option.lower() == 'exit':
        system("cls")
        exit()