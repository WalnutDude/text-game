import data.encryptor as encryptor
from os import system
from random import randint
from time import sleep
import data.tax as tax
import data.death as death

def five():
    option = ""

    levelFile = open('data/level.lvl', 'wb')
    levelFile.write(encryptor.encrypt("5"))
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
    print("     ▐   ███   ▌")
    print("     ▐ ▐  █  ▌ ▌")
    print("     ▐         ▌")
    print("     ▐███ ─ ███▌")
    print("      ▀▀▀▀▀▀▀▀▀")
    print("      [General]\n")

    print("    Your majesty, the neighbouring kingdom is showing signs of attack, could\n    you please increase the army budget?\n")

    print(f"    Stats: [ Wealth : {wealth} | Religion : {religion} | Lifestyle : {lifestyle} ]")
    print("\n·····························\n")
    print("    1 · Sure, we ought to protect our people.\n")
    print("    2 · No, I don't think they'll attack after what happened last war.\n\n")

    sleep(3)

    while option != '1' or option != '2' or option.lower() != 'exit':
        option = input("  Select an option (1 or 2):  ")
        if option == '1' or option == '2' or option.lower() == 'exit':
            break

    if option == '1':
        chance = randint(1,2)

        system('cls')

        if chance == 1:
            if difficulty == 'easy':
                wealth -= 7.5
                lifestyle += 2.5
                religion += 2.5
            elif difficulty == 'normal':
                wealth -= 15
                lifestyle += 5
                religion += 5
            elif difficulty == 'hard':
                wealth -= 30
                lifestyle += 10
                religion += 10
            else:
                wealth -= 15
                lifestyle += 5
                religion += 5

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

            print()
            print("     ██████████")
            print("     █░░░░░░░░█")
            print("     █░█░░░░█░█")
            print("     █░░░░░░░░█")
            print("     ██████████\n")
            sleep(1.0)

            print("    The war happened.")
            sleep(1.5)
            print("    You were able to successfully defend against it due to the increased\n    budget.")
            sleep(1.5)

            print()
            print("·····························\n")
            print()

            input("   Press ENTER to continue...")
            tax.tax('six')
            
        if chance == 2:
            if difficulty == 'easy':
                wealth -= 7.5
            elif difficulty == 'normal':
                wealth -= 15
            elif difficulty == 'hard':
                wealth -= 30
            else:
                wealth -= 15

            if religion > 100:
                religion = 100
            if wealth > 100:
                wealth = 100
            if lifestyle > 100:
                lifestyle = 100

            wealthFile = open("data/stats/wealth.sts", 'wb')
            wealthFile.write(encryptor.encrypt(f"{wealth}"))
            wealthFile.close()

            print()
            print("     ██████████")
            print("     █░░░░░░░░█")
            print("     █░█░░░░█░█")
            print("     █░░░░░░░░█")
            print("     ██████████\n")
            sleep(1.5)

            print("    The war did not happen.")
            sleep(1.5)
            print("    The increased army budget was a waste of money.")
            sleep(1.5)

            print()
            print("·····························\n")
            print()

            input("    Press ENTER to continue...")
            tax.tax('six')
            

    if option == '2':
        chance = randint(1, 2)

        system("cls")

        if chance == 1:
            if difficulty == 'easy':
                religion += 2.5
            elif difficulty == 'normal':
                religion += 5
            elif difficulty == 'hard':
                religion += 10
            else:
                religion += 5

            if religion > 100:
                religion = 100
            if wealth > 100:
                wealth = 100
            if lifestyle > 100:
                lifestyle = 100

            religionFile = open("data/stats/religion.sts", 'wb')
            religionFile.write(encryptor.encrypt(f"{religion}"))
            religionFile.close()

            print()
            print("     ██████████")
            print("     █░░░░░░░░█")
            print("     █░█░░░░█░█")
            print("     █░░░░░░░░█")
            print("     ██████████\n")
            sleep(1.5)

            print("    The war did not happen.")
            sleep(1.5)
            print("    The increased army budget would've been a waste of money.")
            sleep(1.5)

            print()
            print("·····························\n")
            print()

            input("    Press ENTER to continue...")
            tax.tax('six')
            

        if chance == 2:
            if difficulty == 'easy':
                lifestyle -= 5
                wealth -= 10
                religion -= 2.5
            elif difficulty == 'normal':
                lifestyle -= 10
                wealth -= 20
                religion -= 5
            elif difficulty == 'hard':
                lifestyle -= 20
                wealth -= 40
                religion -= 5
            else:
                lifestyle -= 10
                wealth -= 20
                religion -= 5

            if religion > 100:
                religion = 100
            if wealth > 100:
                wealth = 100
            if lifestyle > 100:
                lifestyle = 100

            print()
            print("     ██████████")
            print("     █░░░░░░░░█")
            print("     █░█░░░░█░█")
            print("     █░░░░░░░░█")
            print("     ██████████\n")
            sleep(1.0)

            print("    The war happened.")
            sleep(1.5)
            print("    People died and temples were raided, a lot of money was lost.")
            sleep(1.5)

            print()
            print("·····························\n")
            print()

            input("   Press ENTER to continue...")
            tax.tax('six')

        elif option.lower() == 'exit':
            system("cls")
            exit()
            