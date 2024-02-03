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
def writeLetter():
  for i in genereRandomNumber(0, 25):
    theAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("salut", len(theAlphabet))
    for ib in genereRandomNumber(1, 4):
      if ib % 2 == 0:
        return theAlphabet[i].upper()
      else:
        return theAlphabet[i]
      break
    break
def genereStrongPassword(limitationLenString):
  tidyLocation = 0
  tidyPassWord = ""
  for i in genereRandomNumber(0, 9):
    if tidyLocation == limitationLenString:
      break
    tidyPassWord += str(i)
    tidyLocation += 1
  return tidyPassWord.replace("13", "*").replace("89", "ù").replace("35", "s").replace("39", "j").replace("7", "@").replace("1", "a").replace("9", "%").replace("3", "^").replace("5", "!").replace("8", "b")
