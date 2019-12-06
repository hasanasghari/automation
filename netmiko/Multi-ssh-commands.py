from netmiko import ConnectHandler
Devices = open('My_switches')

for switches in Devices:
    
    Device_info = {
    'username':'hasan',
    'password':'hasan',
    'host':switches,
    'device_type':'cisco_ios'
}
    
    Commands = ['configure terminal',' interface loop 0', 'description "Hello Automation"' , 'end','show ip int brief','show run int loop 0']
    switches = switches.strip()
    print("="*20)    
    print(f'Connecting to " {switches} "')
    print("="*20)    
    Connect = ConnectHandler(**Device_info)
    Command = Connect.send_config_set(Commands)
    print(Command)
