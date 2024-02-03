import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = 1
  while True:
    myNumber = int(str(time.time() / (myNumber / (myNumber - 3245) * myNumber)).replace(".", ""))
    yield myNumber
