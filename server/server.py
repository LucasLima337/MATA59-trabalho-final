import socket
from server.deposit import deposit
from server.recover import recover
from server.files import getFiles
from config.config import Config

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((Config.HOST, Config.PORT))
    sock.listen()
    print(f"Server listening on {Config.HOST}:{Config.PORT}")

    while True:
      clientSocket, clientAddress = sock.accept()
      print("Connected by", clientAddress)

      with clientSocket:
        dataBytes = clientSocket.recv(Config.BUFFER_SIZE).split(Config.BYTES_SPLIT_ID)
        mode = dataBytes[0].decode()

        if mode == "1":
          deposit(dataBytes[1], dataBytes[2], dataBytes[3])
        elif mode == "2":
          recover(clientSocket, dataBytes[1])
        elif mode == "0":
          getFiles(clientSocket)
