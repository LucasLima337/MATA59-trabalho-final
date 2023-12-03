import os

def deposit():
  while True:
    print("[ Deposit Mode ]\n")

    localFiles = os.listdir(os.path.abspath(os.getcwd() + '/client/local'))

    for i, localFile in enumerate(localFiles):
      print(f"[ {i + 1} ] - {localFile}")
    print("[ 0 ] - Exit\n")

    filename = input("Choose the file number to deposit or 0 to exit: ")
    replicas = input("Enter the number of replicas: ")
    break
