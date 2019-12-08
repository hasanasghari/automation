import socket
import os
os.system('cls' if os.name == 'nt' else 'clear')
def Port_knocking():
    print()
    ip=str(input("Please Input IP Address : "))
    if ip == "q" or ip == "Q":
          raise SystemExit()
    port=int(input("Plese Input UDP Port Number: "))
    Message =input("Please Input Message default = None :")
    call=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    call.sendto(Message.encode('utf-8'), (ip, port))
    print("message sent")
    call.close()
    

def menu():
    print()
    print("To exit press q/Q")
    print()
    print("To send msg press 1")
    print()
    a=input("   > ")
    while a == "1":
        Port_knocking()
        
    
menu()
