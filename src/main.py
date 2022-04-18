import replit

go = 'y'
run = 1
while go == 'y':
    while run == 1:
        #If it looks weird stretch out the console :)

        print("██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗")
        print("██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝")
        print("██║ █╗ ██║████╗   ██║     ██║     ██║   ██║██╔████╔██║█████╗")
        print("██║███╗██║██╔═╝   ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝")
        print(
            "╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗▄█╗"
        )
        print(
            " ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝"
        )
        print("       ")
        print(
            " █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗██████╗ "
        )
        print(
            "██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗"
        )
        print(
            "███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ██████╔╝"
        )
        print(
            "██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══██╗"
        )
        print(
            "██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗██║  ██║"
        )
        print(
            "╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
        )

        print("Press 'Y' to start")
        print("Press 'I' for instructions / rules")
        print("Press 'C' for a cheat sheat")
        print("Press 'E' to exit")

        strtInpt = input("\n")

        if (strtInpt == 'y' or strtInpt == 'Y'):
            print("placeholder :)")

        elif (strtInpt == 'i' or strtInpt == 'I'):
            print(
                "Rules: If you die the game ends. So don't die, that's all. \nMade by Matthew Sorensen & Erick Guarneros"
            )
            run = 2

        elif (strtInpt == 'c' or strtInpt == 'C'):
            print(
                "Make sure to collect lots of money and buy things you think will assist you. \nMonsters you fight may give you items as well as xp and gold, these can be useful for fighting. \nThe objective is to get to the end of the road \n(after 10 road stops!) \nAt the end of the road there is a nasty boss you have been hired to defeat."
            )
            run = 2

        elif (strtInpt == 'e' or strtInpt == 'E'):
            print(" ██████╗ ██╗██╗   ██╗███████╗    ██╗   ██╗██████╗ ██████╗ ")
            print("██╔════╝ ██║██║   ██║██╔════╝    ██║   ██║██╔══██╗╚════██╗")
            print("██║  ███╗██║██║   ██║█████╗      ██║   ██║██████╔╝  ▄███╔╝")
            print("██║   ██║██║╚██╗ ██╔╝██╔══╝      ██║   ██║██╔═══╝   ▀▀══╝ ")
            print("╚██████╔╝██║ ╚████╔╝ ███████╗    ╚██████╔╝██║       ██╗   ")
            print(" ╚═════╝ ╚═╝  ╚═══╝  ╚══════╝     ╚═════╝ ╚═╝       ╚═╝   ")
            giveUp = input("y/n: ")
            if (giveUp == 'y' or giveUp == 'Y'):
                replit.clear()
                go = 'n'
                run = 0
                print("")
            elif (giveUp == 'n' or giveUp == 'N'):
                replit.clear()
                go = 'y'
                run = 1

    else:
        if (run == 2):
            run = input("\nContinue? y/n: ")
            if run == 'y' or run == 'Y':
                go = 'y'
                replit.clear()
                run = 1
            elif run == 'n' or run == 'N':
                replit.clear()
                go = 'n'
