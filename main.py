import subprocess
import re

target_ip = "10.10.97.105"

def ping_to_target(target_ip):

    try:
        ping = subprocess.run(['ping', '-c', '1', target_ip], stdout=subprocess.PIPE, universal_newlines=True)

        output = ping.stdout

        if "1 packets transmitted, 1 received" in output:
            return True
        else:
            return False

    except Exception as e:
        return False

if ping_to_target(target_ip):
    print(f"{target_ip} is Accessible")
else:
    print(f"{target_ip} is NOT Accessible")

def port_check(target_ip, target_port):
    try:
        command = f"echo | timeout 1 bash -c 'cat > /dev/tcp/{target_ip}/{target_port}' 2>&1"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,universal_newlines=True)

        output = result.stdout;

        if ('Connection refused' not in output):
            return True;
        else:
            return False;

    except Exception as e:
        return False


def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports from {start_port} to {end_port} on {target_ip}")

    for port in range(start_port, end_port + 1):
        if port_check(target_ip, port):
            print(f"Port {port} is open!")


if __name__ == "__main__":
    ip_address = target_ip
    start_port = 1
    end_port = 200
    scan_ports(ip_address, start_port, end_port)


