import os
from colorama import Fore, init
from scanner.network_discovery import network_discovery
from scanner.port_scanner import port_scanner
from scanner.service_detection import service_detection
from scanner.risk_analyzer import risk_analyzer
init(autoreset=True)

def banner():
    os.system("clear")

    print(Fore.GREEN + """
    =================================
           NETSENTRY v1.0
    Smart Network Security Auditor
    =================================
    """)

def menu():
    print(Fore.CYAN + "[1] Network Discovery")
    print("[2] Port Scanner")
    print("[3] Service Detection")
    print("[4] Security Report")
    print("[5] Exit")

banner()

while True:
    menu()

    choice = input("\nSelect Option: ")

    if choice == "1":
        network_discovery()

    elif choice == "2":
         port_scanner()

    elif choice == "3":
        service_detection()

    elif choice == "4":
        risk_analyzer()

    elif choice == "5":
        print("Exiting NetSentry...")
        break

    else:
        print("Invalid Option!")
 



