import subprocess
import argparse


def ping_to_target(target_ip):
    try:
        ping = subprocess.run(['ping', '-c', '1', target_ip], stdout=subprocess.PIPE, universal_newlines=True)
        output = ping.stdout
        if "1 received" in output:
            return True
        else:
            return False
    except Exception as e:
        return False


def port_check(target_ip, target_port):
    try:
        command = f"echo | timeout 1 bash -c 'cat > /dev/tcp/{target_ip}/{target_port}' 2>&1"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = result.stdout
        if 'Connection refused' not in output:
            return True
        else:
            return False
    except Exception as e:
        return False


def scan_ports(target_ip, ports):
    print(f"Scanning ports {ports} on {target_ip}")

    for port in ports:
        if port_check(target_ip, port):
            print(f"Port {port} is open!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan ports on a target IP address.',  usage='python3 %(prog)s ip_address [-p [PORTS ...]]')
    parser.add_argument('ip_address', help='The target IP address to scan.')
    parser.add_argument('-p', '--ports', nargs='*', type=int, help='Port(s) to scan. Provide as single ports or ranges (e.g., -p 80 443 21 or -p 80-90). Default is all ports 1-65535.')

    args = parser.parse_args()

    ip_address = args.ip_address

    if args.ports:
        ports = []
        for port in args.ports:
            if '-' in str(port):
                start, end = map(int, port.split('-'))
                ports.extend(range(start, end + 1))
            else:
                ports.append(int(port))
    else:
        ports = range(1, 65535)

    if ping_to_target(ip_address):
        print(f"{ip_address} is Accessible")
        scan_ports(ip_address, ports)
    else:
        print(f"{ip_address} is NOT Accessible")
