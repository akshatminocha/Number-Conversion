print("enter 'x' for exit")
octal=input("enter a number in octal format: ")
if(octal=='x'):
    exit()
else:
    dec=str(int(octal))        #converted into a string to obtain every digit of ocatl
    decm=int(dec)
    print(octal,"in hexadecimal=",hex(decm))
