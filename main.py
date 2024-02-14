import time
# This file is Python code...
def generateRandomNumber(tidyNumberA, tidyNumberB):
  myNumberA = tidyNumberA
  myNumberB = tidyNumberB
  checkA = True
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
      if myNumberB > tidyNumberA:
        myNumberB -= int(float(str(time.time())[-1]))
        if myNumberB >= tidyNumberA and myNumberB <= tidyNumberB:
          yield myNumberB
      elif checkA == True:
        checkA = False
        break
def writeLetters():
  for i in generateRandomNumber(0, 25):
    theAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for ib in generateRandomNumber(1, 4):
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
def replaceUsingFunctions(tidyWord, toreplace, tidyFunction):
  tidyWordReturn = tidyWord
  tidyLocation = 0
  for i in tidyWordReturn:
    if i == toreplace[0]:
      tidyWordReturnB = list(tidyWordReturn)
      tidyWordReturnB[tidyLocation] = tidyFunction()
      tidyWordReturn = str(tidyWordReturnB)
    tidyLocation += 1
  return tidyWordReturn
def generateStrongPassword(limitationLenString):
  tidyLocation = 0
  tidyPassWord = ""
  for i in generateRandomNumber(0, 9):
    if tidyLocation == limitationLenString:
      break
    tidyPassWord += str(i)
    tidyLocation += 1
  tidyLettersArray = writeSevenLetters()
  def writeLetter():
    return writeSevenLetters()[5]
  def writeNumber():
    for i in generateRandomNumber(0, 9):
      return i
  def writeSpecialChar():
    for i in generateRandomNumber(0, 9):
      if i == 0:
        return "%"
      elif i == 1:
        return "@"
      elif i == 2:
        return "*"
      elif i == 3:
        return "~"
      elif i == 4:
        return "&"
      elif i == 5:
        return "¿"
      elif i == 6:
        return "“"
      elif i == 7:
        return "^"
      elif i == 8:
        return "¨"
      elif i == 9:
        return "°"
  return replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(replaceUsingFunctions(tidyPassWord, "1", writeLetter), "2", writeLetter), "3", writeNumber), "3", writeNumber), "4", writeSpecialChar), "5", writeSpecialChar), "6", writeSpecialChar), "7", writeLetter), "8", writeNumber), "9", writeSpecialChar), "0", writeLetter)
while True:
  tidyInput = input("Please enter the length of the password string, or enter \"Exit\" or \"exit\" to exit.")
  if tidyInput == "Exit" or tidyInput == "exit":
    break
  print(generateStrongPassword(int(tidyInput)))
