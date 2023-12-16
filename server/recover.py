import os
from config.config import Config

def recover(sock, fileNameBytes):
  availabilityZones = ["us-east1-a", "us-east1-b", "us-east1-c"]

  print("Recovering file...")

  for zone in availabilityZones:
    if fileNameBytes.decode() in os.listdir(f"{Config.CLOUD_DATABASE}/{zone}"):
      with open(f"{Config.CLOUD_DATABASE}/{zone}/{fileNameBytes.decode()}", "rb") as file:
        fileBytes = file.read()
      break
  
  sock.sendall(fileBytes)
