import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = 1
  while True:
    myNumber += int(str(time.time())[-1])
    yield myNumber
