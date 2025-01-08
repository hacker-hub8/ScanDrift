import os
from scanner import Scanner
from geolocation import GeoLocation
from exploitation import Exploitation
from utils import clear_screen, print_banner

# Global state to store results
scan_results = {
    "open_ports": [],
    "services": {},
    "geo_info": {}
}

def main_menu():
    while True:
        clear_screen()
        print_banner()

        # Main menu options
        print("[1] Perform Port Scan")
        print("[2] Fetch Geolocation Information")
        print("[3] Enter Exploitation Mode")
        print("[4] View Scan Results")
        print("[5] Save Results to File")
        print("[6] Exit")

        try:
            choice = int(input("\nSelect an option: "))
            if choice == 1:
                perform_scan()
            elif choice == 2:
                fetch_geolocation()
            elif choice == 3:
                enter_exploitation_mode()
            elif choice == 4:
                view_results()
            elif choice == 5:
                save_results()
            elif choice == 6:
                print("\n[!] Exiting ScanDrift. Goodbye!")
                break
            else:
                print("[!] Invalid choice. Please select a valid option.")
                input("\nPress Enter to continue...")
        except ValueError:
            print("[!] Please enter a number.")
            input("\nPress Enter to continue...")

def perform_scan():
    clear_screen()
    print_banner()
    target = input("Enter the target IP/Domain: ")
    ports = input("Enter specific ports (comma-separated, e.g., 22,80,443) or press Enter for all ports: ")
    threads = input("Enter the number of threads (default: 10): ")

    ports = list(map(int, ports.split(','))) if ports else None
    threads = int(threads) if threads else 10

    scanner = Scanner(target, ports, threads)
    scanner.scan()

    # Store scan results in global state
    scan_results["open_ports"] = scanner.open_ports
    scan_results["services"] = scanner.services

    print("\n[+] Scan complete. Results have been saved.")
    input("\nPress Enter to return to the main menu...")

def fetch_geolocation():
    clear_screen()
    print_banner()
    target = input("Enter the target IP/Domain: ")

    geo = GeoLocation(target)
    geo_data = geo.fetch_location()

    # Store geolocation results in global state
    scan_results["geo_info"] = geo_data

    input("\nPress Enter to return to the main menu...")

def view_results():
    clear_screen()
    print_banner()
    
    # Display scan results
    print("[+] Scan Results:")
    if scan_results["open_ports"]:
        print("\nOpen Ports:")
        for port, service in scan_results["services"].items():
            print(f"  {port}/tcp - {service}")
    else:
        print("\n[-] No scan results available.")

    # Display geolocation results
    print("\nGeolocation Information:")
    if scan_results["geo_info"]:
        for key, value in scan_results["geo_info"].items():
            print(f"  {key}: {value}")
    else:
        print("\n[-] No geolocation data available.")

    input("\nPress Enter to return to the main menu...")

def enter_exploitation_mode():
    clear_screen()
    print_banner()

    if not scan_results["open_ports"]:
        print("[-] No open ports detected. Perform a scan first.")
        input("\nPress Enter to return to the main menu...")
        return

    target = input("Enter the target IP/Domain (leave blank to use the scanned target): ")
    if not target:
        target = list(scan_results["services"].keys())[0]

    exploitation = Exploitation(target, scan_results["open_ports"], scan_results["services"])
    exploitation.interactive_mode()

def save_results():
    clear_screen()
    print_banner()
    
    # Save results to a file
    filename = input("Enter the filename to save results (e.g., results.txt): ")
    try:
        with open(filename, "w") as f:
            f.write("[+] Scan Results:\n")
            for port, service in scan_results["services"].items():
                f.write(f"  {port}/tcp - {service}\n")

            f.write("\n[+] Geolocation Information:\n")
            for key, value in scan_results["geo_info"].items():
                f.write(f"  {key}: {value}\n")

        print(f"\n[+] Results saved to {filename}.")
    except Exception as e:
        print(f"[-] Failed to save results: {e}")

    input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()
