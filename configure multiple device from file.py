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

# IP_LIST = open('18_switches')
# for IP in IP_LIST:
#     RTR = {
#         'device_type': 'cisco_ios',
#         'ip':   IP,
#         'username': 'admin',
#         'password': 'admin',
#     }

#     print ('\nConnecting to the Switch ' + IP.strip() + ' \n')
#     try:
#         net_connect = ConnectHandler(**RTR)
#     except NetMikoTimeoutException:
#         print ('Device not reachable' )
#         continue

#     except NetMikoAuthenticationException:
#         print ('Authentication Failure' )
#         continue

#     except SSHException:
#         print ('Make sure SSH is enabled' )
#         continue

#     output = net_connect.send_config_from_file(config_file='18_switch_config')
#     print(output)

#     print('\n Saving the Switch configuration \n')
#     output = net_connect.save_config()
#     print(output)

#     output = net_connect.send_command('show ip route')
#     print(output)

# Ctrl + K then press Ctrl + C if you’re using Windows
# Command + K then press Command + C if you’re on a Mac
# To uncomment a block of code, use your mouse to select it and then use the key combination:

# Ctrl + K then Ctrl + U if you’re on Windows
# Command + K then Command + U if you’re on a Mac