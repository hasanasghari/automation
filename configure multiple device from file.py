from netmiko import ConnectHandler
from getpass import getpass 
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException
from paramiko import SSHException

IP_LIST = open('devices.txt')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'hasan',
        'secret':'hasan'
    }

    print ('\n Connecting to the Router ' + IP.strip() + '\n')
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable' )
        continue

    except NetMikoAuthenticationException:
        print ('Authentication Failure' )
        continue

    except SSHException:
        print ('Make sure SSH is enabled' )
        continue
    net_connect.enable()
    output = net_connect.send_config_from_file(config_file='configs.txt')
    print(output)

    print('\n Saving the Router configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show running | in username')
    print(output)
