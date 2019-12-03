

import telnetlib 
import getpass


user = input("Enter your Username: ")

password = getpass.getpass()

f=open("My_switches")

for IP in f:
    IP=IP.strip()
    print("Configuring Switch" + (IP) )
    Host=IP
    Connection=telnetlib.Telnet(Host) # OOP of telnetlib  telnetlib.Telnet(host=None, port=0[, timeout])
    Connection.read_until(b"Username: ") #Telnet.read_until(expected, timeout=None)
    Connection.write(user.encode('ascii') + b"\n")
    if password:
        Connection.read_until(b"Password: ")
        Connection.write(password.encode("ascii") + b"\n")
    Connection.write(b"configure terminal\n")
    for x in range(10,60):
        Connection.write(b"vlan " + str(x).encode("ascii") + b"\n")
        Connection.write(b"Name Automation-VLAN" + str(x).encode("ascii") + b"\n")
    Connection.write(b"end\n")
    Connection.write(b"exit\n")
    print(Connection.read_all().decode('ascii'))


