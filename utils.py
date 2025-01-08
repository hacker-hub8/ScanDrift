import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_banner():
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    print(RED + BOLD + '''
      ______                          ______             _     ___  _    
    .' ____ \                        |_   _ `.          (_)  .' ..]/ |_  
    | (___ \_| .---.  ,--.   _ .--.    | | `. \ _ .--.  __  _| |_ `| |-' 
     _.____`. / /'`\]`'_\ : [ `.-. |   | |  | |[ `/'`\][  |'-| |-' | |   
    | \____) || \__. // | |, | | | |  _| |_.' / | |     | |  | |   | |,  
     \______.''.___.'\--;__/[___||__]|______.' [___]   [___][___]  \__/  
                                                                         
     \t''' + BLUE + '[ Open Port Scanner & Exploiter upon Network by HackerHub8 ]' + ENDC + '''
     \t\t
    ''' + GREEN + '░░░░░░███████ ]▄▄▄▄▄▄▄▄' + ENDC + '''   \t''' + BLUE + 'Version' + ENDC + ''': 1.0.3
    ''' + GREEN + ' ▂▄▅█████████▅▄▃▂      ' + ENDC + '''   \t''' + BLUE + 'Author' + ENDC + ''': HackerHub8
    ''' + GREEN + '[███████████████████]. ' + ENDC + '''
    ''' + GREEN + '◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..   ' + ENDC + '''          
    ''' + ENDC)
