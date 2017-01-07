import random
import os

# print random.randint(1, 10) / 10.0

path = 'imgs'
# isExists = os.path.exists(path)
# print isExists
# if not isExists:
#     os.mkdir(path)

arr = os.listdir(path)
for name in arr:
    print name
