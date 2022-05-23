from os import system
import data.menu as menu

def options():

    system("cls")
    option = ""

    print()
    print("   █▀▀█  █▀▀█ ▀▀█▀▀ ▀█▀ █▀▀█ █▀▀▄ █▀▀ ") 
    print("   █  █  █▄▄█   █    █  █  █ █  █ ▀▀█ ")
    print("   ▀▀▀▀  ▀      ▀   ▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀")


    print()
    print("·····························")
    print()

    print("   1 · THEME\n")
    print("   2 · BACK")

    print()
    print("·····························\n")
    print()

    while option != '1' or option != '2':
        option = input(" Select an option (1 or 2):  ")
        if option == '1' or option == '2':
            break

    if option == '1':
        system("cls")
        option1 = ""

        print()
        print("   ▀▀█▀▀ █  █ █▀▀ █▀▄▀█ █▀▀ █▀▀")
        print("     █   █▀▀█ █▀▀ █ ▀ █ █▀▀ ▀▀█")
        print("     ▀   ▀  ▀ ▀▀▀ ▀   ▀ ▀▀▀ ▀▀▀")
        print()
        print("·····························")
        print()

        print("    1 · DARK\n")
        print("    2 · LIGHT\n")
        print("    3 · BACK")

        print()
        print("·····························\n")
        print()

        while option1 != '1' or option1 != '2' or option1 != '3':
            option1 = input(" Select an option (1, 2 or 3):  ")
            if option1 == '1' or option1 == '2' or option1 == '3':
                break

        if option1 == '1':
            optionsFile = open("data/options.cfg", 'w')
            optionsFile.write('dark')
            optionsFile.close()
            system("color 07")
            menu.menu()

        elif option1 == '2':
            optionsFile = open("data/options.cfg", 'w')
            optionsFile.write('light')
            optionsFile.close()
            system("color 70")
            menu.menu()
        
        elif option1 == '3':
            menu.menu()

    if option == '2':
        menu.menu()