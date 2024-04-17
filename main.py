import random as randomNumberPlease
# this is Python file
def generateStrongPasswordTidy(numberOfLetters):
  strongPassword = "";
  for n in range(0, numberOfLetters+1):
    strongPassword += randomNumberPlease.choice("abcdefghijklmnopqrstuvwxyz$%ùµ*/!.;?œ“+=1234567890}]{[|''\"\"¡/")
  return strongPassword

print(generateStrongPasswordTidy)
