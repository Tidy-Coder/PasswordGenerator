def genereRandomNumber(tidyNumberA, tidyNumberB, exitNowNow = False):
  myNumber = str(tidyNumberA)
  while True:
    if exitNowNow == True:
      break
    if int(myNumber) % 2 == 1:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 453)
    elif int(myNumber) % 5 == 3:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 259)
    else:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 347)
    itsA = None
    while int(myNumber) > tidyNumberB or int(myNumber) < tidyNumberA:
      if int(myNumber) > tidyNumberB:
        if itsA == True:
          myNumber = int(myNumber) - (tidyNumberB - tidyNumberA)
          continue
        myNumber = myNumber[1:]
        itsA = False
      else:
        myNumber += str((int(myNumber) % 4) + 1)
        itsA = True
      yield int(myNumber)
