from netmiko import ConnectHandler

IOSv={
	'device_type' : 'cisco_ios',
	'host':'192.168.122.102', # put device ip here
	'username':'hasan',# put username here
	'password':'hasan' # put password here
}

Connect=ConnectHandler(**IOSv)
output=Connect.send_command('show vlan brief')
print(output)

