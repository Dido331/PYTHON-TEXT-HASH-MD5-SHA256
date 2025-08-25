import os 
import sys
import hashlib
from colorama import Fore, Style


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + """
    __  _____   _____ __  __
   / / / /   | / ___// / / /
  / /_/ / /| | \__ \/ /_/ / 
 / __  / ___ |___/ / __  /  
/_/ /_/_/  |_/____/_/ /_/   
     HASHOWANIE TEKSTU                         
        """ + Style.RESET_ALL)

def menu():
    print(Fore.GREEN + "1. HASHOWANIE TEKSTU (MD5/SHA256)")
    print(Fore.BLUE + "2. Wyjście z terminala")
def hash_text():
    text = input("Podaj tekst: ")
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())




while True:
    banner()
    menu()
    choice = input(Fore.GREEN + "Wybierz opcję: ")
    if choice == "1":
        hash_text()
    elif choice == "2":
        sys.exit()
    else:
        print("Nieprawidłowa opcja!")
    input("\nNaciśnij Enter aby kontynuować...")