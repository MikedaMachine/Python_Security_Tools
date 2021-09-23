import socket
from IPy import IP

def scan(ip_address):
    changed_ip = inspect_ip(ip_address)
    print('\n' + 'Scanning Target ip_address ' + str(ip_address))
    for port in range(75,85):
        scanner(changed_ip, port)

def inspect_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def grab_banner(s):
    return s.recv(1024)

def scanner(ip_address, port):
    try:
        runner = socket.socket()
        runner.settimeout(0.5)
        runner.connect((ip_address, port))
        try:
            banner = grab_banner(runner)
            print('Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('Open Port ' + str(port)) 
    except:
        pass


ip_address = input('Enter targets to scan(seperate targets with a comma(,) ): ')
if ',' in ip_address:
    for ip_add in ip_address.split(','):
        scan(ip_add.strip(' '))
else:
    scan(ip_address)
