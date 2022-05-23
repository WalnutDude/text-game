import imp
from os import system
from time import sleep
import data.encryptor as encryptor
import data.six as six

def tax(nextLevel):

    wealthFile = open("data/stats/wealth.sts", 'rb')
    wealth = int(encryptor.decrypt(wealthFile.readline()))
    wealthFile.close()

    lifestyleFile = open("data/stats/lifestyle.sts", 'rb')
    lifestyle = int(encryptor.decrypt(lifestyleFile.readline()))
    lifestyleFile.close()

    system("cls")

    print()
    print("     ██████████")
    print("     █░░░░░░░░█")
    print("     █░█░░░░█░█")
    print("     █░░░░░░░░█")
    print("     ██████████\n")
    sleep(1.0)

    if lifestyle >= 80:
        wealth += 20

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100

        wealthFile = open("data/stats/wealth.sts", 'wb')
        wealthFile.write(encryptor.encrypt(f"{wealth}"))
        wealthFile.close()

        print("     The people were incredibly happy with your rule,")
        sleep(1.5)
        print("     you have recieved [ 20 ] wealth as tax from the people.")
        sleep(1.5)
        print()
        print("·····························\n")
        print()

        input("   Press ENTER to continue...")
        if nextLevel == 'six':
            six.six()

    elif lifestyle >= 60:
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

        print("     The people were happy with your rule,")
        sleep(1.5)
        print("     you have recived [ 10 ] wealth as tax from the people.")
        sleep(1.5)
        print()
        print("·····························\n")
        print()

        input("   Press ENTER to continue...")
        if nextLevel == 'six':
            six.six()

    elif lifestyle >= 40:
        wealth += 5

        if religion > 100:
            religion = 100
        if wealth > 100:
            wealth = 100
        if lifestyle > 100:
            lifestyle = 100


        wealthFile = open("data/stats/wealth.sts", 'wb')
        wealthFile.write(encryptor.encrypt(f"{wealth}"))
        wealthFile.close()

        print("     The people were satisfied with your rule,")
        sleep(1.5)
        print("     you have recived [ 5 ] wealth as tax from the people.")
        sleep(1.5)
        print()
        print("·····························\n")
        print()

        input("   Press ENTER to continue...")
        if nextLevel == 'six':
            six.six()
    
    elif lifestyle < 40:
        print("     The people were not satisfied with your rule,")
        sleep(1.5)
        print("     you have recived [ 0 ] wealth as tax from the people.")
        sleep(1.5)
        print()
        print("·····························\n")
        print()

        input("   Press ENTER to continue...")
        if nextLevel == 'six':
            six.six()