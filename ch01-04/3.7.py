import random
import time

t =int(time.time())
c = chr(ord('A') + t % (ord('Z') - ord('A') + 1))
print(c)