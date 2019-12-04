import telnetlib 
import getpass


user = input("Enter your Username: ")

password = getpass.getpass()

f=open("My_switches")

for IP in f:
    IP = IP.strip()
    print("Geting Running Config of Switch " + (IP) )
    Host = IP
    Connection=telnetlib.Telnet(Host) # OOP of telnetlib  telnetlib.Telnet(host=None, port=0[, timeout])
    Connection.read_until(b"Username: ") #Telnet.read_until(expected, timeout=None)
    Connection.write(user.encode('ascii') + b"\n")
    if password:
        Connection.read_until(b"Password: ")
        Connection.write(password.encode("ascii") + b"\n")
    Connection.write(b"terminal length 0\n")
    Connection.write(b"show running-config \n")
    Connection.write(b"exit \n")

    read_output = Connection.read_all()
    file_output = open("Switch-"+Host, "w")
    file_output.write(read_output.decode("ascii"))
    file_output.write("\n")
    file_output.close()
    print(Connection.read_all().decode('ascii'))



