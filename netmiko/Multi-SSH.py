from netmiko import ConnectHandler
Devices = open('My_switches')
for switches in Devices:
    Device_info = {
    'username':'hasan',
    'password':'hasan',
    'host':switches,
    'device_type':'cisco_ios'
}
    switches = switches.strip()
    print("="*20)    
    print(f'Connecting to " {switches} "')
    print("="*20)    
    Connect = ConnectHandler(**Device_info)
    Command = Connect.send_command("show ip int brief")
    print(Command)
