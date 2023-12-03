import os
from config.config import Config

def deposit(sock, mode):
  BSI = Config.BYTES_SPLIT_ID

  while True:
    print("[ Deposit Mode ]\n")

    localFiles = os.listdir(Config.LOCAL_DATABASE)

    for i, localFile in enumerate(localFiles):
      print(f"[ {i + 1} ] - {localFile}")
    print("[ 0 ] - Exit\n")

    fileNumber = int(input("Choose the file number to deposit or 0 to exit: "))
    os.system("clear")

    if fileNumber == 0:
      print("Exiting deposit mode...\n")
      break
    elif fileNumber > len(localFiles) or fileNumber < 0:
      print("Invalid option, try again\n")
      continue
    else:
      fileName = localFiles[fileNumber - 1]

    while True:
      print("[ 1 ] Single-AZ")
      print("[ 2 ] Dual-AZ")
      print("[ 3 ] Triple-AZ")
      print("[ 0 ] Return to mode selection\n")

      replicationType = input("Enter the type of replication: ")

      if replicationType not in ["1", "2", "3", "0"]:
        print("\nInvalid option, try again\n")
        continue
      elif replicationType == "0":
        os.system("clear")
        returnToModeSelection = True
        print("Returning to mode selection...\n")
        break
      else:
        returnToModeSelection = False
        os.system("clear")
        break

    if returnToModeSelection:
      continue

    modeBytes = str.encode(mode)
    fileNameBytes = str.encode(fileName)
    replicationTypeBytes = str.encode(replicationType)

    with open(f"{Config.LOCAL_DATABASE}/{fileName}", "rb") as file:
      fileBytes = file.read()

    data = modeBytes + BSI + fileNameBytes + BSI + replicationTypeBytes + BSI + fileBytes
    
    os.system("clear")
    
    sock.sendall(data)
    print("File sent successfully!\n")
    print(f"Mode              : Deposit")
    print(f"File name         : {fileName}")
    print(f"Replication type  : {replicationType}\n")
    break
