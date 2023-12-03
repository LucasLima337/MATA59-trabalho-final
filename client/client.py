import socket, os
from deposit import deposit

HOST = "localhost"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.connect((HOST, PORT))
  print(f"Connected to {HOST}:{PORT}\n")

  while True:
    print("[ 1 ] Deposit Mode")
    print("[ 2 ] Recover Mode")
    print("[ 0 ] Exit\n")

    mode = input("Enter mode or 0 to exit: ")
    os.system("clear")

    if mode == "1":
      deposit()
    elif mode == "2":
      print("Recover Mode")
    elif mode == "0":
      print("Exiting... bye!")
      break
    else:
      print("Invalid option, try again\n")
