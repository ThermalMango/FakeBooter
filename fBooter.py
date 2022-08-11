import random as r
from time import sleep as s
from colorama import init
init()
from colorama import Fore


host = ""
attacks = 250


def get_attacks():
    return input(f"\n\nEnter the number of attacks ({attacks}): ")


def get_host():
    return input(f"\n\nEnter host ({host}): ")


def start():
    for attack in range(int(attacks)):
        ip = f"{r.randint(1, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}"
        print(Fore.YELLOW + "Using " + f"{Fore.LIGHTWHITE_EX + ip} " + Fore.YELLOW +
              "to DDoS " + f"{Fore.LIGHTWHITE_EX + host}")
        s(0.025)
    print("\nAttacks completed!\n")


def main():
    global host, attacks
    while True:
        print(Fore.LIGHTWHITE_EX + f"\nIP/Website Booter\n'Quit' - Quits program\n'Host' - {host}\n"
                                   f"'Attacks' - {attacks}\n'Start' - Start the attacks\n")
        option = input("").lower()
        if option == "quit":
            quit()
        if option == "host":
            host = get_host()
        elif option == "attacks":
            attacks = get_attacks()
            if not int(attacks.isnumeric()):
                attacks = 250
        elif option == "start":
            if not host == "":
                start()
            else:
                print("\nAdd a host to start attacking\n")


if __name__ == "__main__":
    main()
