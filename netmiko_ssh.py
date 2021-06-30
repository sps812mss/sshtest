#Lsb 7 Netmiko lab_ss
import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter SSh username: ")
PASS = getpass("Please enter your SSH password: ")

device = {'ip' : '192.168.220.11', 'username' : USERNAME, 'password' : PASS, 'device_type' : 'cisco_ios'}


c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)
f.close()
