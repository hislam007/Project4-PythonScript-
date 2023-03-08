
#Module Imports
import os
import colorama
from colorama import *
import pyfiglet

colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

print("\033[91m" + "Welcome to Spider Offensive Security Tool!".center(80, "-") + "\033[0m")

# Spider ASCII art
print(Fore.GREEN + pyfiglet.figlet_format('Spider.py', font='slant'))
print(Fore.GREEN + """
                   /|      __
             /\  /**|   ,-~ /    
            |  \/  \\\/'-~_-~/
            | |  |  |    /   \\
            \_/-\\_/ \\_  /' ' '|   
           /   o     \\/      |  
          /          (       |  
         /            \\      |  
        /       /      \\     \\
       /      /         \\    \\
      /      /           \\    \\
     /______/             \\____\\
""")

while True:
    print("List of Actions:")
    print("-" * 80)
    print("[1]. Spider NSLookup")
    print("[2]. Spider Port Scan (Port Scanner)")
    print("[3]. Spider Robots.txt Web crawler")
    print("[4]. Spider Web Strike (DDoS Attack)")
    print("[5]. Quit")
    
    selection = input("Choose Action Number:")

    if selection == "1":
        import nslookup
    elif selection == "2":
        import portscanner
    elif selection == "3":
        import robots_txt
    elif selection == "4":
        import ddos
    elif selection == "5":
        print("Exiting")
        break    
    else:
        print("Invalid Selection. Enter 1-5.")