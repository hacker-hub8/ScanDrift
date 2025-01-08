#! /usr/bin/env python3

import argparse
from scanner import Scanner
from geolocation import GeoLocation
from exploitation import Exploitation

def main():
    banner = '''
  ______                          ______             _     ___  _    
.' ____ \                        |_   _ `.          (_)  .' ..]/ |_  
| (___ \_| .---.  ,--.   _ .--.    | | `. \ _ .--.  __  _| |_ `| |-' 
 _.____`. / /'`\]`'_\ : [ `.-. |   | |  | |[ `/'`\][  |'-| |-' | |   
| \____) || \__. // | |, | | | |  _| |_.' / | |     | |  | |   | |,  
 \______.''.___.'\--;__/[___||__]|______.' [___]   [___][___]  \__/  
                                                                     
[ Open Port Scanner with Advanced Features by HackerHub8 ]
Version: 2.0.0
Author: HackerHub8
'''

    print(banner)

    # Parse arguments
    parser = argparse.ArgumentParser(description="ScanDrift - Advanced Port Scanner and Exploitation Tool")
    parser.add_argument("-a", "--address", required=True, help="Target IP address (e.g., -a 192.168.1.1)")
    parser.add_argument("-p", "--ports", nargs="+", type=int, help="Specific ports to scan (e.g., -p 22 80 443)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads for scanning (default: 10)")
    parser.add_argument("--geo", action="store_true", help="Fetch geolocation of the target IP")
    args = parser.parse_args()

    # Geolocation
    if args.geo:
        print("\n[+] Fetching geolocation data...")
        geo = GeoLocation(args.address)
        geo.fetch_location()

    # Perform port scan
    scanner = Scanner(args.address, args.ports, args.threads)
    scanner.scan()

    # Check if there are open ports
    if scanner.open_ports:
        while True:
            print("\n[+] Scan completed. Open ports detected.")
            print("1. Enter Exploit Mode")
            print("2. Exit")
            try:
                choice = int(input("\nSelect an option: "))
                if choice == 1:
                    exploitation = Exploitation(args.address, scanner.open_ports, scanner.services)
                    exploitation.interactive_mode()
                elif choice == 2:
                    print("[!] Exiting ScanDrift. Goodbye!")
                    break
                else:
                    print("[!] Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("[!] Please enter a valid number.")
    else:
        print("\n[-] No open ports detected. Exiting...")
        print("[!] Goodbye!")

if __name__ == "__main__":
    main()
