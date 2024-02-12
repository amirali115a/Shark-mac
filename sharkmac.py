
#!/usr/bin/python
 

import subprocess
import re
import random as r
from argparse import ArgumentParser 
from colorama import Fore
 
 
def get_argument():
    parser = ArgumentParser(description="----- A simple and powerful MAC changer tool -----", prog="python3 sharkmac")
    parser.add_argument("-i", dest="interface", help="Specify the name of interface")
    parser.add_argument("-m", dest="new_mac", help="Specify a new mac or type 'r' to set random MAC Address insted of new mac")
    args = parser.parse_args()
 
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
 
    return args
 
  
def get_mac(interface):
    interface_info = str(subprocess.run(["sudo", "ifconfig", interface], capture_output=True))
    interface_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_info)
    return interface_mac.group(0)
 
 


 

arg = get_argument()
interface = arg.interface
new_mac = arg.new_mac
 
if new_mac == "r":
    x = r.randint(0, 9)
    y = r.randint(0, 9)
    z = r.randint(0, 9)
    new_mac = f"00:{x}{y}:{y}{z}:{z}{x}:{y}{x}:{z}{y}"
 
current_mac = get_mac(interface)
 

subprocess.run(["sudo", "ifconfig", interface, "down"])
subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["sudo", "ifconfig", interface, "up"])
 

changed_mac = get_mac(interface)
if current_mac != changed_mac:
    print(Fore.YELLOW,f'Now, Your MAC for {interface} {current_mac}')
    print(Fore.GREEN,f'changed {changed_mac}')
else:
    print("Try Again!!!\n")