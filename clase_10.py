import socket

# SOCKETS
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))

# Enviar petición HTTP GET
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
mySock.send(cmd.encode())

# Recibir datos en bloques
while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mySock.close()