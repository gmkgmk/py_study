import os
path = "assets"
isExists=os.path.exists(path)

if not isExists:
  os.makedirs(path)