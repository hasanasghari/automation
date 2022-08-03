import getpass

from netmiko import ConnectHandler

USER = input('Enter the Username: ')
PASS = getpass.getpass()

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': USER,
            'password': PASS,
            'secret':'Mysecret'
        }

        net_connect = ConnectHandler(**Router)

        hostname = net_connect.send_command('show run | i host')
        x=hostname.split()
        device = x[1]
        print("Backing up " + device)

        filename = device + '-Backup.txt'

        showrun = net_connect.send_command('show run')
        log_file = open(filename, "w")
        log_file.write(showrun)
        log_file.write("\n")
        net_connect.disconnect()

input('Press ENTER to Continue')