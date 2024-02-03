import time
def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumberA = tidyNumberA
  myNumberB = tidyNumberB
  checkA = False
  while True:
    myNumberA = tidyNumberA
    myNumberB = tidyNumberB
    while True:
      if myNumberA < tidyNumberB:
        myNumberA += int(float(str(time.time())[-1])) * int(float(str(time.time())[-2:]))
        if myNumberA >= tidyNumberA and myNumberA <= tidyNumberB:
          yield myNumberA
      else:
        checkA = True
      if myNumberB < tidyNumberB:
        myNumberB += int(float(str(time.time())[-1])) * int(float(str(time.time())[-2:]))
        if myNumberB >= tidyNumberA and myNumberB <= tidyNumberB:
          yield myNumberB
      elif checkA == True:
        checkA = False
        break
