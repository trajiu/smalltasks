import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host): #Returns True or False
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    try:
        output = subprocess.check_output(command[0] + ' ' + command[1] + ' ' + command[2] + ' ' + command[3], shell=True)
    except Exception:
        return False
    return True

result = []
hostname = ['192.168.43.1', '192.168.43.2', 'google.com']
for item_hostname in hostname:
    if ping(item_hostname) == True:
        result.append(item_hostname + ' is up')
    else:
        result.append(item_hostname + ' is down')
print(result)