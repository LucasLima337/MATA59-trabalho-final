import os

class Config:
  HOST = "localhost"
  PORT = 9000
  LOCAL_DATABASE = os.path.abspath(os.getcwd() + "/client/local")
  CLOUD_DATABASE = os.path.abspath(os.getcwd() + "/server/cloud")
  BYTES_SPLIT_ID = b"GPJ9Z558nTf6mLYSaM"
