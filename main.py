import secrets.choice
# this is Python file
def generateStrongPasswordTidy(numberOfLetters):
  strongPassword = "";
  for(range(0, numberOfLetters+1)):
    strongPassword += choice("abcdefghijklmnopqrstuvwxyz$%ùµ*/!.;?œ“+=1234567890}]{[|''\"\"¡/");
  return strongPassword;

print(generateStrongPasswordTidy);
