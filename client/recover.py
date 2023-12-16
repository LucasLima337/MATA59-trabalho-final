import socket, os
from config.config import Config

def recover(sockListFiles, mode):
  BSI = Config.BYTES_SPLIT_ID
  
  sockListFiles.sendall(str.encode("0"))
  fileNamesBytes = sockListFiles.recv(Config.BUFFER_SIZE).split(Config.BYTES_SPLIT_ID)

  if fileNamesBytes[0].decode() == "0":
    print("There are no files to recover\n")
    return

  while True:
    print("[ Recover Mode ]\n")
    
    for i, fileNameBytes in enumerate(fileNamesBytes):
      print(f"[ {i + 1} ] - {fileNameBytes.decode()}")
    print("[ 0 ] - Exit\n")

    fileNumber = int(input("Choose the file number to recover or 0 to exit: "))
    os.system("clear")

    if fileNumber == 0:
      print("Exiting recover mode...\n")
      break
    elif fileNumber > len(fileNamesBytes) or fileNumber < 0:
      print("Invalid option, try again\n")
      continue
    else:
      fileNameBytes = fileNamesBytes[fileNumber - 1]

    modeBytes = str.encode(mode)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((Config.HOST, Config.PORT))
      data = modeBytes + BSI + fileNameBytes
      sock.sendall(data)
      fileBytes = sock.recv(Config.BUFFER_SIZE)

    with open(f"{Config.LOCAL_RECOVERED_DATABASE}/{fileNameBytes.decode()}", "wb") as file:
      file.write(fileBytes)
    print("File recovered successfully!\n")
    break
