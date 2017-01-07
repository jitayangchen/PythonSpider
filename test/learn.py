import random
import os
import time

# print random.randint(1, 10) / 10.0

# path = 'imgs'
# isExists = os.path.exists(path)
# print isExists
# if not isExists:
#     os.mkdir(path)

# arr = os.listdir(path)
# for name in arr:
#     print name

print "%f" % time.time()
print time.localtime(time.time())
print time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
