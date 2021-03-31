# Stuff
import time
from os import system
from colorama import Fore
from termcolor import colored
from colorama import init
# Custom Class
# Don't Ask why I name this Class Like This :P
from Kion_tte_nani.SAHA_OI_SAHA import TemperatureCounter


class YokosoSensei:

    def StartInteraction(self):
        print(colored("Welcome to Magic Converter for Temperature", "cyan"))
        time.sleep(5)  # Add a Little Bit Delay
        print(colored(
            "Hemmm...?,How to Use it?,its SIMPLE!\nJust Type The Temperature Type and the Heat Number and let me do the Rest!",
            "cyan"))
        time.sleep(10)  # This To!

        # Ok Without Further do Lets Start Counting!
        print(colored("OK...,First Please Tell me What Type Temperature do you Have", "green"))
        print(colored("1.Celsius", "green"))
        print(colored("2.fahrenheit", "green"))
        print(colored("3.Reamur", "green"))
        print(colored("4.Kelvin", "green"))
        # When Process Above is Still Running than Get the Choice
        while True:
            try:
                choice = int(input())
                system("clear")
                break
            except ValueError:  # Get Trigger When the User is Not input a Number
                print(colored("Please Input a Selection With a Number\n", "red"))
                continue

        # Ok Because Python is Not Have Switch Statement than I Need to use Else if Statement
        if choice == 1:
            while True:
                try:
                    mainChoice = int(input(colored("Please Enter the Heat Number\n", "green")))
                    system("clear")
                    break
                except ValueError:
                    system("clear")
                    print(colored("Please Input Selection With a Number\n", "red"))
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (fahren, kelvin, reamur) = tempNumber.celcius()
            converterChoice = int(input(colored(
                "OK... Now Please Type What do you Want to Convert into?\n 1.Fahrenheit\n 2.kelvin\n 3.Reamur\n Remember I Need a Number :)\n",
                "green")))
            if converterChoice == 1:
                system("clear")
                print(colored("The Result:" + str(fahren) + "°F", "cyan"))
            elif converterChoice == 2:
                system("clear")
                print(colored("The Result:" + str(kelvin) + "K", "cyan"))
            elif converterChoice == 3:
                system("clear")
                print(colored("The Result:" + str(reamur) + "°R", "cyan"))
            else:
                system("clear")
                print(colored("Ahh...,Where the Option?\n", "red"))
        # Just Copy Paste The Rest
        if choice == 2:
            while True:
                try:
                    mainChoice = int(input(colored("Please Enter the Heat Number\n", "green")))
                    system("clear")
                    break
                except ValueError:
                    system("clear")
                    print(colored("Please Input Selection With a Number\n", "red"))
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, kelvin, reamur) = tempNumber.fahrenheit()
            converterChoice = int(input(colored(
                "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.kelvin\n 3.Reamur\n Remember I Need a Number :)\n",
                "green")))
            if converterChoice == 1:
                system("clear")
                print(colored("The Result:" + str(cel) + "°C", "cyan"))
            elif converterChoice == 2:
                system("clear")
                print(colored("The Result:" + str(kelvin) + "K", "cyan"))
            elif converterChoice == 3:
                system("clear")
                print(colored("The Result:" + str(reamur) + "°R", "cyan"))
            else:
                system("clear")
                print(colored("Ahh..., The Option Please~\n", "red"))

        if choice == 3:
            while True:
                try:
                    mainChoice = int(input(colored("Please Enter the Heat Number\n", "green")))
                    system("clear")
                    break
                except ValueError:
                    system("clear")
                    print(colored("Please Input Selection With a Number\n", "red"))
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, kelvin, fahren) = tempNumber.reamur()
            converterChoice = int(input(colored(
                "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.kelvin\n 3.Fahrenheit\n Remember I Need a Number :)\n",
                "green")))
            if converterChoice == 1:
                system("clear")
                print(colored("The Result:" + str(cel) + "°C", "cyan"))
            elif converterChoice == 2:
                system("clear")
                print(colored("The Result:" + str(kelvin) + "K", "cyan"))
            elif converterChoice == 3:
                system("clear")
                print(colored("The Result:" + str(fahren) + "°F", "cyan"))
            else:
                system("clear")
                print(colored("How Many Time i Need to Tell you to Choice the Option?\n", "red"))

        if choice == 4:
            while True:
                try:
                    mainChoice = int(input(colored("Please Enter the Heat Number\n", "green")))
                    system("clear")
                    break
                except ValueError:
                    system("clear")
                    print(colored("Please Input Selection With a Number\n", "red"))
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, reamur, fahren) = tempNumber.kelvin()
            converterChoice = int(input(colored(
                "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.Reamur\n 3.Fahrenheit\n Remember I Need a Number :)\n",
                "green")))
            if converterChoice == 1:
                system("clear")
                print(colored("The Result:" + str(cel) + "°C", "cyan"))
            elif converterChoice == 2:
                system("clear")
                print(colored("The Result:" + str(reamur) + "°R", "cyan"))
            elif converterChoice == 3:
                system("clear")
                print(colored("The Result:" + str(fahren) + "°F", "cyan"))
            else:
                system("clear")
                print(colored("ZerroKarraHajjimaruyo!!\n", "red"))

        if choice > 4:
            system("clear")
            print(colored("Please Type Between 1 - 4~\n", "yellow"))

    def StartInteractionInWindows(self):
        init()
        print(Fore.CYAN + "Welcome to Magic Converter for Temperature\n")
        time.sleep(5)  # Add a Little Bit Delay
        print(Fore.CYAN +
              "Hemmm...?,How to Use it?,its SIMPLE!\nJust Type The Temperature Type and the Heat Number and let me do the Rest!")
        time.sleep(10)  # This To!

        # Ok Without Further do Lets Start Counting!
        print(Fore.GREEN + "OK...,First Please Tell me What Type Temperature do you Have")
        print(Fore.GREEN + "1.Celsius")
        print(Fore.GREEN + "2.fahrenheit")
        print(Fore.GREEN + "3.Reamur")
        print(Fore.GREEN + "4.Kelvin")
        # When Process Above is Still Running than Get the Choice
        while True:
            try:
                choice = int(input())
                system("cls")
                break
            except ValueError:  # Get Trigger When the User is Not input a Number
                system("cls")
                print(Fore.RED + "Please Input a Selection With a Number\n")
                continue

        # Ok Because Python is Not Have Switch Statement than I Need to use Else if Statement
        if choice == 1:
            while True:
                try:
                    mainChoice = int(input(Fore.GREEN + "Please Enter the Heat Number\n"))
                    system("cls")
                    break
                except ValueError:
                    system("cls")
                    print(Fore.RED + "Please Input Selection With a Number\n")
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (fahren, kelvin, reamur) = tempNumber.celcius()
            converterChoice = int(input(Fore.GREEN +
                                        "OK... Now Please Type What do you Want to Convert into?\n 1.Fahrenheit\n 2.kelvin\n 3.Reamur\n Remember I Need a Number :)\n"))
            if converterChoice == 1:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(fahren) + "°F")
            elif converterChoice == 2:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(kelvin) + "K")
            elif converterChoice == 3:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(reamur) + "°R")
            else:
                system("cls")
                print(Fore.RED + "Ahh...,Where the Option?\n")
        # Just Copy Paste The Rest
        if choice == 2:
            while True:
                try:
                    mainChoice = int(input(Fore.GREEN + "Please Enter the Heat Number\n"))
                    system("cls")
                    break
                except ValueError:
                    system("cls")
                    print(Fore.RED + "Please Input Selection With a Number\n")
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, kelvin, reamur) = tempNumber.fahrenheit()
            converterChoice = int(input(Fore.GREEN +
                                        "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.kelvin\n 3.Reamur\n Remember I Need a Number :)\n"))
            if converterChoice == 1:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(cel) + "°C")
            elif converterChoice == 2:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(kelvin) + "K")
            elif converterChoice == 3:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(reamur) + "°R")
            else:
                system("cls")
                print(Fore.RED + "Ahh..., The Option Please~\n")

        if choice == 3:

            while True:
                try:
                    mainChoice = int(input(Fore.GREEN + "Please Enter the Heat Number\n"))
                    system("cls")
                    break
                except ValueError:
                    system("cls")
                    print(Fore.RED + "Please Input Selection With a Number\n")
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, kelvin, fahren) = tempNumber.reamur()
            converterChoice = int(input(Fore.GREEN +
                                        "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.kelvin\n 3.Fahrenheit\n Remember I Need a Number :)\n"))
            if converterChoice == 1:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(cel) + "°C")
            elif converterChoice == 2:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(kelvin) + "K")
            elif converterChoice == 3:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(fahren) + "°F")
            else:
                system("cls")
                print(Fore.RED + "How Many Time i Need to Tell you to Choice the Option?\n")

        if choice == 4:

            while True:
                try:
                    mainChoice = int(input(Fore.GREEN + "Please Enter the Heat Number\n"))
                    system("cls")
                    break
                except ValueError:
                    system("cls")
                    print(Fore.RED + "Please Input Selection With a Number\n")
                    continue
            tempNumber = TemperatureCounter(mainChoice)
            (cel, reamur, fahren) = tempNumber.kelvin()
            converterChoice = int(input(Fore.GREEN +
                                        "OK... Now Please Type What do you Want to Convert into?\n 1.Celcius\n 2.Reamur\n 3.Fahrenheit\n Remember I Need a Number :)\n"))
            if converterChoice == 1:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(cel) + "°C")
            elif converterChoice == 2:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(reamur) + "°R")
            elif converterChoice == 3:
                system("cls")
                print(Fore.CYAN + "The Result:" + str(fahren) + "°F")
            else:
                system("cls")
                print(Fore.RED + "ZerroKarraHajjimaruyo!!\n")

        if choice > 4:
            system("cls")
            print(Fore.YELLOW + "Please Type Between 1 - 4~\n")

# It Took Me 4 Hours to Make This
