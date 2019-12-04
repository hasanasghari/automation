from netmiko import ConnectHandler

IOSv={
	'device_type' : 'cisco_ios',
	'host':'192.168.122.102',
	'username':'hasan',
	'password':'hasan'
}

Connect=ConnectHandler(**IOSv)
output=Connect.send_command('show vlan brief')
print(output)

