import requests
import time
import os
import platform
import sys
from options.color import *
from options.header import *

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

def clean_screen():
    os.system("cls" if platform == "nt" else "clear")

def check_ip(target, delay=3):
    print(f"{b_blue}[*]{reset} Memulai scanning...")
    time.sleep(0.5)
    print(f"{b_blue}-{reset}"*40)

    while True:
        try:
            url = f"http://ip-api.com/json/{target}"
            respons = requests.get(url, headers=headers, timeout=3)
            data = respons.json()

            if data['status'] == 'success':
                for k, v in data.items():
                    print(f"{b_green}[✔]{reset} {k:<20}: {v}")
                    time.sleep(0.5)
                print(f"{b_blue}-{reset}"*40)
                print(f"\n{b_green}[✔] Scanning selesai...{reset}")
                tanya = input(f"{b_blue}[?]{reset} Lagi? (y/n) : ")
                if tanya == "y":
                    time.sleep(0.5)
                    continue
                elif tanya == "n":
                    time.sleep(0.5)
                    break
                else:
                    print(f"{b_red}[!] Input anda salah...{reset}")
                    time.sleep(0.5)
                    continue
        except requests.RequestException:
            pass
        except KeyboardInterrupt:
            print(f"\n{b_red}[✘] Tools dibatalkan...{reset}")
            time.sleep(0.5)
            sys.exit()


if __name__ == "__main__":
    while True:
        try:
            clean_screen()
            header_tools()
            target = input(f"{b_blue}[?]{reset} Domain target\t: ")
            delay = int(input(f"{b_blue}[?]{reset} Delay proses\t: "))
            check_ip(target, delay)
        except KeyboardInterrupt:
            print(f"\n{b_red}[✘] Tools dibatalkan...{reset}")
            time.sleep(0.5)
            break