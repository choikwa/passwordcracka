import os
import subprocess
from collections import deque
from string import ascii_letters
from string import digits
from string import punctuation
from string import whitespace

bag = [] + list(ascii_letters) + list(digits) + list(punctuation) + list(whitespace)
print("bag: " + str(bag))
CMD="C:\\Program Files\\7-Zip\\7z.exe"

num = 1
count = 0

def check(q):
  if len(q) < 3:
    return
  global num
  global count
  for c in bag:
    print("Checking "+q+c)
    try:
      res = subprocess.check_call([CMD, 'e', 'crypto.7z', '-y', '-p'+q+c], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      print("res=" + str(res) + " word was: " + q+c)
      sys.exit()
    except subprocess.CalledProcessError as e:
      pass
    count += 1
  num += 1

que = deque()
que.append('')
while(que):
  q = que.popleft()
  check(q)
  for c in bag:
    que.append(q+c)