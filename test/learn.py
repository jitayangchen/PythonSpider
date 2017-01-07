import random
import os

# print random.randint(1, 10) / 10.0

path = 'imgs2'
isExists = os.path.exists(path)
print isExists
if not isExists:
    os.mkdir(path)
