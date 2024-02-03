def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = str(tidyNumberA)
  while True:
    if int(myNumber) % 2 == 1:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 453)
    elif int(myNumber) % 5 == 3:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 259)
    else:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) * 5))) + 347)
    itsA = None
    if int(myNumber) > tidyNumberB:
      itsA = False
    else:
      itsA = True
    while int(myNumber) > tidyNumberB or int(myNumber) < tidyNumberA:
      if int(myNumber) > tidyNumberB:
        if itsA == True:
          myNumber = str(int(myNumber) - (tidyNumberB - tidyNumberA))
          continue
        myNumber = myNumber[1:]
        itsA = False
      elif int(myNumber) < tidyNumberA:
        myNumber += str((int(myNumber) % 4) + 1)
        itsA = True
    yield int(myNumber)
