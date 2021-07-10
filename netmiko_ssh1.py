#Lsb 7 Netmiko lab_ss

from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetmikoTimeoutException

USERNAME = input("Please enter SSh username: ")
PASS = getpass("Please enter your SSH password: ")

device = {'ip' : '192.168.220.11', 'username' : USERNAME, 'password' : PASS, 'device_type' : 'cisco_ios'}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An authentication error occured while connecting to: " + device['ip'])
except (NetmikoTimeoutException):
    print("The device " + device['ip'] + " timed out when attempting to connect")    
except (SSHException):
    print("An error occured while connecting to device " + device['ip'] + "via SSH.  Is SSH enabled?")
