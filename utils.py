import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints the tool's banner."""
    print('''
  ______                          ______             _     ___  _    
.' ____ \                        |_   _ `.          (_)  .' ..]/ |_  
| (___ \_| .---.  ,--.   _ .--.    | | `. \ _ .--.  __  _| |_ `| |-' 
 _.____`. / /'`\]`'_\ : [ `.-. |   | |  | |[ `/'`\][  |'-| |-' | |   
| \____) || \__. // | |, | | | |  _| |_.' / | |     | |  | |   | |,  
 \______.''.___.'\--;__/[___||__]|______.' [___]   [___][___]  \__/  
                                                                     
[ ScanDrift - Advanced Port Scanner and Exploitation Framework ]
Version: 2.0.0 | Author: HackerHub8
    ''')
