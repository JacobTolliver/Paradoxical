import colorama
from colorama import Fore, Back, Style
import keyboard
import time
import requests
import threading
import warnings
import os
import threading
import subprocess
warnings.filterwarnings('ignore')
def run_script(ddosser):
    subprocess.run(["python", ddosser])
def menu_print():
    print(Fore.RED + "  ____                               _                  _                  _ ")
    print(Fore.RED + " |  _ \    __ _   _ __    __ _    __| |   ___   __  __ (_)   ___    __ _  | |")
    print(Fore.RED + " | |_) |  / _` | | '__|  / _` |  / _` |  / _ \  \ \/ / | |  / __|  / _` | | |")
    print(Fore.RED + " |  __/  | (_| | | |    | (_| | | (_| | | (_) |  >  <  | | | (__  | (_| | | |")
    print(Fore.RED + " |_|      \__,_| |_|     \__,_|  \__,_|  \___/  /_/\_\ |_|  \___|  \__,_| |_|" + Style.RESET_ALL + Back.LIGHTBLACK_EX + "   A menu by 𝐆𝐡𝐨𝐬𝐭")
    print(Style.RESET_ALL + " ")
    print(" ")
    print(" ")
    print('"1" Begin ddossing an ip address.')
def loadingui():
    print("■", end="\r")
    time.sleep(.5)
    print("■ ■", end="\r")
    time.sleep(.5)
    print("■ ■ ■", end="\r")
    time.sleep(.5)
    print("■ ■ ■ ■", end="\r")
    time.sleep(.5)
    print("■ ■ ■ ■ ■", end="\r")
    time.sleep(.5)
    print("Script loaded!")
os.system('cls')
loadingui()
print(" ")
menu_print()
# ends the output with a space
if input(">") == "1":
    import ddoss