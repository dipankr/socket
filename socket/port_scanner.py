import socket
import argparse
from colorama import init, Fore

def is_port_open(host: str, port: int) -> bool:
    sock = socket.socket()

    try:
        sock.connect((host, port))
        sock.settimeout(0.5)
    except socket.error as e:
        return False
    else:
        return True

# test if a port is open
if __name__ == '__main__':

    # Declare arguments
    parser = argparse.ArgumentParser(description='Socket server')
    parser.add_argument('-H', '--host', help='Target host', default='127.0.0.1', type=str)
    parser.add_argument('-s', '--start', help='Starting port', default=500, type=int)
    parser.add_argument('-e', '--end', help='Ending port', default=60000, type=int)

    # Parse arguments
    args = parser.parse_args()
    host, start, end = args.host, args.start, args.end

    for port in range(start, end+1):
        if not is_port_open(host, port):
            #print(f'{Fore.RED}{port} is closed {Fore.RESET}')
            continue

        print(f'{Fore.GREEN}Port {port} is open{Fore.RESET}')
        

# scan.py --host 127.0.0.1 --start 100 --end 1000