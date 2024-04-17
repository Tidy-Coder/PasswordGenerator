import random as randomNumberPlease
# this is Python file
def generateStrongPasswordTidy(numberOfLetters):
  strongPassword = "";
  for n in range(0, numberOfLetters+1):
    strongPassword += randomNumberPlease.choice("abcdefghijklmnopqrstuvwxyz$%ùµ*/!.;?œ“+=1234567890}]{[|''\"\"¡/@à°&ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  return strongPassword

while True:
  entranceTidy = input("Please enter length of your strong password or enter exit to exit")
  if(entranceTidy.upper() == "EXIT"):
    break
  else:
    try:
      print(int(print(generateStrongPasswordTidy(int(entranceTidy)))))
    except ValueError:
      print("Please enter int...")
