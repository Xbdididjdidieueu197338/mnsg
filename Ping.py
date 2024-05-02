import requests
import socket
import time
from colorama import Fore, init

init()

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        print(f"{Fore.RED}[ERROR] Unable to resolve the host name.")
        return None

def check_http_ping(ip):
    while True:
        try:
            start_time = time.time()
            response = requests.get(f"http://{ip}")
            end_time = time.time()
            ping_time = round((end_time - start_time) * 1000)  # تحويل الوقت من الثواني إلى ميلي ثانية وتقريبه للرقم الصحيح
            if response.status_code == 200:
                print(f"{Fore.GREEN}[PING] HTTP Ping: {ping_time} ms")
            else:
                print(f"{Fore.RED}[PING] HTTP Ping: {ping_time} ms - Status Code: {response.status_code}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] An error occurred: {e}")
        time.sleep(5)  # قياس البنق كل 5 ثواني

def main():
    domain = input("Enter the domain to ping (e.g., example.com): ")
    ip = get_ip_address(domain)
    if ip:
        check_http_ping(ip)

if __name__ == "__main__":
    main()