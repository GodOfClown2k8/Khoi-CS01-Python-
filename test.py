
import os
if os.path.exists("demofile.txt"):
    print("file exist")
else:
  print("The file does not exist")
os.remove("demofile.txt")