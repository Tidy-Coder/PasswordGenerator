import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = 1
  while True:
    myNumber += myNumber
    myNumber = int(str(time.time() / myNumber).replace(".", ""))
    yield myNumber
