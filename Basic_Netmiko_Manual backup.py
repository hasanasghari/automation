#R1

import os
os.chdir('C:/Users/Hasan/Desktop/Automation')
from netmiko import ConnectHandler

print('Connecting to device: R1')
R1 = ConnectHandler(ip='10.111.111.10', username='hasan', password='hasan',secret='hasan', device_type='cisco_ios')
R1.enable()

print('Saving the configuration')
R1.send_command('wr mem')

print('Backing configs to R1.cfs')
R1.send_command('terminal length 0')
R1_config = R1.send_command('show run')
with open ('R1.cfg','w') as config:
    config.write(R1_config)
R1.disconnect()
print('Done')


#R2

import os
os.chdir('C:/Users/Hasan/Desktop/Automation')
from netmiko import ConnectHandler

print('Connecting to device: R2')
R2 = ConnectHandler(ip='10.111.111.20', username='hasan', password='hasan',secret='hasan', device_type='cisco_ios')
R2.enable()

print('Saving the configuration')
R2.send_command('wr mem')

print('Backing configs to R2.cfs')
R2.send_command('terminal length 0')
R2_config = R2.send_command('show run')
with open ('R2.cfg','w') as config:
    config.write(R2_config)
R2.disconnect()
print('Done')

#R3

import os
os.chdir('C:/Users/Hasan/Desktop/Automation')
from netmiko import ConnectHandler

print('Connecting to device: R3')
R3 = ConnectHandler(ip='10.111.111.30', username='hasan', password='hasan',secret='hasan', device_type='cisco_ios')
R3.enable()

print('Saving the configuration')
R3.send_command('wr mem')

print('Backing configs to R3.cfs')
R3.send_command('terminal length 0')
R3_config = R3.send_command('show run')
with open ('R3.cfg','w') as config:
    config.write(R3_config)
R3.disconnect()
print('Done')


import os
os.chdir('C:/Users/Hasan/Desktop/Automation')
from netmiko import ConnectHandler

print('Connecting to device: R4')
R4 = ConnectHandler(ip='10.111.111.40', username='hasan', password='hasan',secret='hasan', device_type='cisco_ios')
R4.enable()

print('Saving the configuration')
R4.send_command('wr mem')

print('Backing configs to R4.cfs')
R4.send_command('terminal length 0')
R4_config = R4.send_command('show run')
with open ('R4.cfg','w') as config:
    config.write(R4_config)
R4.disconnect()
print('Done')

