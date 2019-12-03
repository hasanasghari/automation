import getpass
import sys
import telnetlib

HOST = "192.168.122.100"
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name  Automation-Vlan2 \n")
tn.write("vlan 3\n")
tn.write("name automation-Vlan3 \n")
tn.write("vlan 4\n")
tn.write("name  Automation-Vlan4 \n")
tn.write("vlan 5\n")
tn.write("name automation-Vlan5 \n")
tn.write("int loop 1\n")
tn.write("ip address 10.11.11.1 255.255.255.0 \n")
tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")
print tn.read_all()
a