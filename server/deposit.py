import os
from glob import glob
from config.config import Config

def deposit(fileNameBytes, replicationTypeBytes, fileBytes):
  availabilityZones = ["us-east1-a", "us-east1-b", "us-east1-c"]
  fileName = fileNameBytes.decode()

  for zone in availabilityZones:
    if fileName in os.listdir(f"{Config.CLOUD_DATABASE}/{zone}"):
      print(f"File already exists in the zone {zone}. Updating...")
      os.rename(f"{Config.CLOUD_DATABASE}/{zone}/{fileName}", f"{Config.CLOUD_DATABASE}/{zone}/{fileName}.old")

  for i in range(int(replicationTypeBytes.decode())):
    with open(f"{Config.CLOUD_DATABASE}/{availabilityZones[i]}/{fileName}", "wb") as file:
      file.write(fileBytes)
    print(f"File deposited successfully in the zone {availabilityZones[i]}")

  try:
    oldFiles = glob(f"{Config.CLOUD_DATABASE}/**/{fileName}.old")

    for oldFile in oldFiles:
      os.remove(oldFile)
  except:
    pass
