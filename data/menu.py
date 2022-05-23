from os import system
import data.introduction as introduction
import data.encryptor as encryptor
import data.one as one
import data.two as two
import data.three as three
import data.four as four
import data.five as five
import data.six as six
import data.seven as seven
import data.options as optionspy
import data.difficulty as difficulty

def menu():

    optionsFile = open("data/options.cfg", 'r')
    options = optionsFile.readlines()
    optionsFile.close()
     
    levelFile = open('data/level.lvl', 'rb')
    level = encryptor.decrypt(levelFile.readline())
    levelFile.close()

    wealthFile = open("data/stats/wealth.sts", 'rb')
    wealth = float(encryptor.decrypt(wealthFile.readline()))
    wealthFile.close()

    religionFile = open("data/stats/religion.sts", 'rb')
    religion = float(encryptor.decrypt(religionFile.readline()))
    religionFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'rb')
    lifestyle = float(encryptor.decrypt(lifestyleFile.readline()))
    lifestyleFile.close()
    option = ""

    if religion > 100:
        religion = 100
    if wealth > 100:
        wealth = 100
    if lifestyle > 100:
        lifestyle = 100

    system("cls")
    
    if options[0] == 'light':
        system("color 70")
    elif options[0] == 'dark':
        system("color 07")
    else:
        system("color 07")

    print()
    print("   █  █ █▀▀ █   █   █▀▀█")
    print("   █▀▀█ █▀▀ █   █   █  █")        
    print("   ▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀\n")


    print(f"  Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")

    print()
    print("·····························")
    print()

    print("   1 · START\n")
    print("   2 · OPTIONS\n")
    print("   3 · QUIT\n\n")
    print("   TIP: If you enter 'exit' anywhere in the game, the game will be closed.")
    print()
    print("·····························\n")
    print()


    while option != '1' or option != '2' or option != "3" or option.lower() != 'exit':
        option = input(" Select an option (1, 2 or 3):  ")
        if option == '1' or option == '2' or option == '3' or option.lower() == 'exit':
            break

    if option == '1':
        if level == '-1' or level == "":
            difficulty.selection()
        elif level == '0' or level == "":
            introduction.introduction()
        elif level == '1':
            one.one()
        elif level == '2':
            two.two()
        elif level == '3':
            three.three()
        elif level == '4':
            four.four()
        elif level == '5':
            five.five()
        elif level == '6':
            six.six()
        elif level == '7':
            seven.seven()

    elif option == '2':
        optionspy.options()

    elif option == '3':
        system("cls")
        exit()

    elif option.lower() == 'exit':
        system("cls")
        exit()
    
