from os import system
import data.encryptor as encryptor
import data.seven as seven
from time import sleep
import data.death as death

def six():

    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("6"))
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
    print("           ▄      ") 
    print("       ▄██████▄▄  ")
    print("      ███▀▀▀████▌ ")
    print("     ▐██     ███▌ ")      
    print("     ▐█▌ ▐ ▐ ▐███ ")     
    print("     ▐█▌      ▐██ ")    
    print("      █▌  ─   ██  ")   
    print("      ▐█▌    ██   ")  
    print("       █     █    \n") 
    print("        [Wife]    \n")

    print("    Thanksgiving is coming soon, I think we should arrage a celebration\n    at the royal quarter.")
    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")

    print("    1 · Sure, I'll start with preparations already.\n")
    print("    2 · No, we need not waste money on unnecessary things.\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == '1':
        if difficulty == 'easy':
            wealth -= 5
            religion += 5
            lifestyle += 2.5
        elif difficulty == 'normal':
            wealth -= 10
            religion += 10
            lifestyle += 5
        elif difficulty == 'hard':
            wealth -= 20
            religion += 20
            lifestyle += 10
        else:
            wealth -= 10
            religion += 10
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
        
        religionFile = open("data/stats/religion.sts", 'wb')
        religionFile.write(encryptor.encrypt(f"{religion}"))
        religionFile.close()

        lifestyleFile = open("data/stats/lifestyle.sts", 'wb')
        lifestyleFile.write(encryptor.encrypt(f"{lifestyle}"))
        lifestyleFile.close()
        seven.seven()

    elif option == '2':
        if difficulty == 'easy':
            religion -= 5
            lifestyle -= 5
        elif difficulty == 'normal':
            religion -= 10
            lifestyle -= 10
        elif difficulty == 'hard':
            religion -= 20
            lifestyle -= 20
        else:
            religion -= 10
            lifestyle -= 10

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
        seven.seven()
