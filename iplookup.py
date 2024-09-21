import socket
import re
import requests
import sys

def show_banner():
    ascii_art = r"""
   
  _____ _____    _      ____   ____  _  ___    _ _____  
 |_   _|  __ \  | |    / __ \ / __ \| |/ / |  | |  __ \ 
   | | | |__) | | |   | |  | | |  | | ' /| |  | | |__) |
   | | |  ___/  | |   | |  | | |  | |  < | |  | |  ___/ 
  _| |_| |      | |___| |__| | |__| | . \| |__| | |     
 |_____|_|      |______\____/ \____/|_|\_\\____/|_|     
                                                        
                                                        

    """
    print(ascii_art)

def get_ip_details(ip):
    api_url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if 'bogon' in data: 
            print(f"IP {ip} is a bogon (reserved IP address)")
        else:
            print(f"Details for IP {ip}:")
            print(f"IP: {data.get('ip')}")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}")
            print(f"Country: {data.get('country')}")
            print(f"Org: {data.get('org')}")
            print(f"Location: {data.get('loc')}")
    except requests.RequestException as e:
        print(f"Failed to retrieve data for IP {ip}: {e}")

def get_remote_machine_info():
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Enter the host address or IP: ")
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(ip_pattern, user_input):
        get_ip_details(user_input)
    else:
        try:
            ip = socket.gethostbyname(user_input)
            print(f"IP address of {user_input}: {ip}")
            get_ip_details(ip)
        except socket.gaierror as err_msg:
            print(f"Error resolving hostname {user_input}: {err_msg}")

if __name__ == '__main__':
    show_banner()
    get_remote_machine_info()
