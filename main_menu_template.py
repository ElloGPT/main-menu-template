import time as t
import os

def menu():    #main menu and my Logo :D. Colors are ASCII art
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \033[38;2;100;0;0m▓█████  ██▓     ██▓     ▒█████    ▄████  ██▓███  ▄▄▄█████▓\033[0m
    \033[38;2;130;0;0m▓█   ▀ ▓██▒    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██░  ██▒▓  ██▒ ▓▒\033[0m
    \033[38;2;160;20;20m▒███   ▒██░    ▒██░    ▒██░  ██▒▒██░▄▄▄░▓██░ ██▓▒▒ ▓██░ ▒░\033[0m
    \033[38;2;190;50;50m▒▓█  ▄ ▒██░    ▒██░    ▒██   ██░░▓█  ██▓▒██▄█▓▒ ▒░ ▓██▓ ░\033[0m 
    \033[38;2;220;80;80m░▒████▒░██████▒░██████▒░ ████▓▒░░▒▓███▀▒▒██▒ ░  ░  ▒██▒ ░ \033[0m
    \033[38;2;240;120;120m░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ▒▓▒░ ░  ░  ▒ ░░\033[0m   
    \033[38;2;250;180;180m░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░   ░   ░ ░▒ ░         ░\033[0m    
    \033[38;2;255;220;220m░     ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░░         ░\033[0m      
    \033[38;2;255;255;255m░  ░    ░  ░    ░  ░    ░ ░        ░\033[0m
    """)
    
    print("\033[38;2;240;120;120m[0]XYZ\033[0m") #change option names 
    print("\033[38;2;240;120;120m[0]XYZ\033[0m")
    print("\033[38;2;240;120;120m[0]XYZ\033[0m")
    print("")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #clears terminal screen

while True:
    menu()
    user_input = int(input("Option: ")) #after here do if_statements e.g. if user_input == 1: ...
