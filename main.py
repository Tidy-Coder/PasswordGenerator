import time
# This file is Python code...
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
def writeLetters():
  for i in genereRandomNumber(0, 25):
    theAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for ib in genereRandomNumber(1, 4):
      if ib % 2 == 0:
        yield theAlphabet[i].upper()
      else:
        yield theAlphabet[i]
      break
def writeSevenLetters():
  arrayContainsLetters = []
  localisationLetterZ = 0
  for i in writeLetters():
    arrayContainsLetters += [i]
    localisationLetterZ += 1
    if localisationLetterZ == 7:
      break
  return arrayContainsLetters
def genereStrongPassword(limitationLenString):
  tidyLocation = 0
  tidyPassWord = ""
  for i in genereRandomNumber(0, 9):
    if tidyLocation == limitationLenString:
      break
    tidyPassWord += str(i)
    tidyLocation += 1
  tidyLettersArray = writeSevenLetters()
  return tidyPassWord.replace("11", "%1").replace("23", "¨3").replace("87", ";7").replace("93", "/3").replace("1", tidyLettersArray[1]).replace("2", tidyLettersArray[3]).replace("3", tidyLettersArray[5]).replace("4", "à").replace("5", "@").replace("6", "*").replace("7", "/").replace("8", "^").replace("9", "!")
while True:
  tidyInput = input("Please enter the length of the password string, or enter \"Exit\" or \"exit\" to exit.")
  if tidyInput == "Exit" or tidyInput == "exit":
    break
  print(genereStrongPassword(int(tidyInput)))
