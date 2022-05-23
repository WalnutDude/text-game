from os import system
import data.encryptor as encryptor
import data.introduction as introduction

def selection():
    
    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("-1"))
    levelFile.close()

    system("cls")

    print()
    print("   █▀▀▄ ▀█▀ █▀▀ █▀▀ ▀█▀ █▀▀ █  █ █   ▀▀█▀▀ █  █") 
    print("   █  █  █  █▀▀ █▀▀  █  █   █  █ █     █   █▄▄█") 
    print("   ▀▀▀  ▀▀▀ ▀   ▀   ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀   ▀   ▄▄▄█\n")

    print()
    print("·····························")
    print()

    print("   1 · EASY\n")
    print("   2 · NORMAL\n")
    print("   3 · HARD\n\n")

    print()
    print("·····························\n")
    print()

    while option != '1' or option != '2' or option != "3" or option.lower() != 'exit':
        option = input(" Select an option (1, 2 or 3):  ")
        if option == '1' or option == '2' or option == '3' or option.lower() == 'exit':
            break

    if option == '1':

        difficultyFile = open('data/difficulty.dif', 'wb')
        difficultyFile.write(encryptor.encrypt("easy"))
        difficultyFile.close()
        introduction.introduction()

    elif option == '2':

        difficultyFile = open('data/difficulty.dif', 'wb')
        difficultyFile.write(encryptor.encrypt("normal"))
        difficultyFile.close()
        introduction.introduction()

    elif option == '3':

        difficultyFile = open('data/difficulty.dif', 'wb')
        difficultyFile.write(encryptor.encrypt("hard"))
        difficultyFile.close()
        introduction.introduction()
