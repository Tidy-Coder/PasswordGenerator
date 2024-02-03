import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = 1
  while True:
    myNumber = int(str(time.time() / (myNumber / 555 * myNumber)).replace(".", ""))
    yield myNumber
