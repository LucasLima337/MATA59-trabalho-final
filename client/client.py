import socket, os
from client.deposit import deposit
from config.config import Config

def main():
  while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((Config.HOST, Config.PORT))
      print(f"Connected to {Config.HOST}:{Config.PORT}\n")

      print("[ 1 ] Deposit Mode")
      print("[ 2 ] Recover Mode")
      print("[ 0 ] Exit\n")

      mode = input("Enter mode or 0 to exit: ")
      os.system("clear")

      if mode == "1":
        deposit(sock, mode)
      elif mode == "2":
        print("Recover Mode")
      elif mode == "0":
        print("Exiting... bye!")
        break
      else:
        print("Invalid option, try again\n")
