"""
A Temperature Conversion Program Make By Agung-Krisna
Fork & Edit By:Natsu
Link to Original Repo: https://github.com/Agung-Krisna/Temperature-Conv
"""

# Let's Import Some Stuff
from os import system
from Interaction.Yōkoso import YokosoSensei
from sys import platform
from sys import version_info
import extra.media as player

# Some Simple Checking Function
def checkOsType():
    if platform == "linux" or platform == "cygwin":
        return 2
    elif platform == "win32":
        return 1
    else:
        print("Sorry Currently This Program Can Only Run on Windows and Linux")
        exit()

def isPythonisSupport():
    if version_info.major != 3:
        print("At Least You Need Python Version 3.x.x")
        exit()


# Main Things

isPythonisSupport() # Check For Python Version
if checkOsType() == 2:
    system("clear")
    #player.playBGM() Not Work in Linux for Some Reason
    YokosoSensei.StartInteraction("")
elif checkOsType() == 1:
    system("cls")
    player.playBGM()
    YokosoSensei.StartInteractionInWindows("")


