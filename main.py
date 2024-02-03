import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = tidyNumberA
  while True:
    while myNumber < tidyNumberB:
      myNumber += int(str(time.time())[-1]) * int(str(time.time())[-2:])
      if myNumber >= tidyNumberA and myNumber <= tidyNumberB:
        yield myNumber
    while myNumber > tidyNumberA:
      myNumber -= int(str(time.time())[-1]) * int(str(time.time())[-2:])
      if myNumber >= tidyNumberA and myNumber <= tidyNumberB:
        yield myNumber
