import os
from config.config import Config

def getFiles(sock):
  BSI = Config.BYTES_SPLIT_ID

  print("Sending files...")
  fileNames = os.listdir(f"{Config.CLOUD_DATABASE}/us-east1-a")
  fileNames.remove(".gitkeep")

  if len(fileNames) == 0:
    data = b"0"
  else:
    data = b""
    for i, fileName in enumerate(fileNames):
      if i == len(fileNames) - 1:
        data += str.encode(fileName)
      else:
        data += str.encode(fileName) + BSI

  sock.sendall(data)
