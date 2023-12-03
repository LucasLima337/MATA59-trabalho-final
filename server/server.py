import socket

HOST = "localhost"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.bind((HOST, PORT))
  sock.listen()
  print(f"Server listening on {HOST}:{PORT}")

  while True:
    clientSocket, clientAddress = sock.accept()
    print("Connected by", clientAddress)

    with clientSocket:
      dataBytes = clientSocket.recv(1024)
      data = dataBytes.decode()
