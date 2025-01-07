# ScanDrift  

░░░░░░███████ ]▄▄▄▄▄▄▄▄ 

 ▂▄▅█████████▅▄▃▂        
[███████████████████] 

◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤

ScanDrift is a simple and efficient port scanning tool designed to help you identify open ports on a given IP address. Built with flexibility and ease of use in mind, it provides options for scanning specific ports or all commonly used ones.  

---

## Features  

- Lightweight and fast port scanning.  
- Specify the target IP address for scanning.  
- Scan specific ports or a range of ports as needed.  
- Easy-to-use command-line interface.  

---

## Usage  

To use ScanDrift, you must have Python installed. Clone this repository and run the script from the terminal.  

### Command Syntax  

```bash
python ScanDrift.py [-h] [-a ADDRESS] [-p PORTS [PORTS ...]]
```

### Options  

- `-h`, `--help`: Displays the help menu with usage instructions.  
- `-a ADDRESS`: Specify the target IP address.  
  - Example: `-a 127.0.0.1`  
- `-p PORTS [PORTS ...]`: Specify one or more ports for scanning.  
  - Example: `-p 22 80`  


## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/hacker-hub8/ScanDrift.git
   cd ScanDrift
   ```  

2. Make sure Python 3.7 is installed on your machine.  

3. Run the script with the desired arguments as shown in the examples.  

---
## Examples  

1. **Scan all commonly used ports on a target:**  
   ```bash
   python ScanDrift.py -a 192.168.1.1
   ```  

2. **Scan specific ports on a target:**  
   ```bash
   python ScanDrift.py -a 192.168.1.1 -p 22 80 443
   ```  

3. **Display help menu:**  
   ```bash
   python ScanDrift.py -h
   ```  

---


## Notes  

- Ensure that you have appropriate permissions to scan the target IP address. Unauthorized scanning can be illegal and unethical.  
- Use this tool responsibly and only on networks you own or have explicit permission to test.
- Take loads when you scan outer networks
- Best Use for inside network scanning  

---

## License  

ScanDrift is an open-source project licensed under the [MIT License](https://github.com/hacker-hub8/ScanDrift?tab=GPL-3.0-1-ov-file).  

---


## 🌐 Follow us:

For support, email support@hackerhub8.in 
or

Join our Community [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/hacker_hub8) 
