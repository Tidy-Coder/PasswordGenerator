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
        myNumberA += int(float(str(time.time())[-1]))
        if myNumberA >= tidyNumberA and myNumberA <= tidyNumberB:
          yield myNumberA
      else:
        checkA = True
      if myNumberB < tidyNumberB:
        myNumberB += int(float(str(time.time())[-1]))
        if myNumberB >= tidyNumberA and myNumberB <= tidyNumberB:
          yield myNumberB
      elif checkA == True:
        checkA = False
        break
def genereStrongPassword(limitationLenString):
  tidyLocation = 0
  tidyPassWord = ""
  for i in genereRandomNumber(0, 9):
    if tidyLocation == limitationLenString:
      break
    tidyPassWord += str(i)
    tidyLocation += 1
  return tidyPassWord.replace("7", "@").replace("1", "a").replace("9", "%").replace("3", "^").replace("5", "!").replace("8", "b")
