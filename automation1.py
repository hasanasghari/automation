import getpass
import sys
import telnetlib

HOST = "192.168.122.200"
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("admin\n")
tn.write("conf t\n")
tn.write("hostname hasan \n")
tn.write("int loop 0\n")
tn.write("ip address 10.1.1.1 255.255.255.0\n")
tn.write("end\n")
tn.write("exit\n")
print tn.read_all()