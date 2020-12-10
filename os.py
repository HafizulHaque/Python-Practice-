import os
import math

fileSizes = {name: os.path.getsize(name) for name in os.listdir('.') if os.path.isdir(name)}

print(fileSizes)