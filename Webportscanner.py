import socket

print("""
[1] Port Checker
[2] Port Scanner
[3] Exit
""")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Option = int(input("Option>> "))

if(Option == 3):
    print("Exit..")
    exit()

elif(Option == 1):
    Target = input("[+] Target Website/ip>> ")
    Port = int(input("[+] Port>> "))
    try:
        s.connect((Target,Port))
        print("[+] Port OPEN>> "+str(Port))
    except:
        print("[-] Port CLOSE>> "+str(Port))

elif(Option == 2):
    Target = input("[+] Target Website/ip>> ")
    Min = int(input("[+] Minimum Port>> "))
    Max = int(input("[+] Maximum Port>> "))
    for Port in range(Min,Max + 1):
        try:
            s.connect((Target,Port))
            print("[+] Port OPEN>> "+str(Port))
            break
        except:
            print("[-] Port CLOSE>> "+str(Port))

else:
    print("[-] error")
    exit()
