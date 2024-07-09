import subprocess
import re

target_ip = "8.8.8.8"

def ping(target_ip):

    try:
        ping_to_target = subprocess.run(['ping', '-c', '1', target_ip], stdout=subprocess.PIPE, universal_newlines=True)

        output = ping_to_target.stdout

        if "1 packets transmitted, 1 received" in output:
            return True
        else:
            return False

    except Exception as e:
        return False

if ping(target_ip):
    print(f"{target_ip} is Accessible")
else:
    print(f"{target_ip} is NOT Accessible")
