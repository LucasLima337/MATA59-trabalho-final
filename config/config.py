import os

class Config:
  HOST = "localhost"
  PORT = 9000
  LOCAL_DATABASE = os.path.abspath(os.getcwd() + "/client/local")
  BYTES_SPLIT_ID = b"GPJ9Z558nTf6mLYSaM"
