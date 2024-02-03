def genereRandomNumber(tidyNumberA, tidyNumberB):
  myNumber = str(tidyNumberA + tidyNumberB)
  theTidyIteration = 1
  while True:
    if int(myNumber) % 2 == 1:
      myNumber = str(int(myNumber + "5" + str(int(int(myNumber) / 2.45 * 3))) + 453)
    elif int(myNumber) % 5 == 3:
      myNumber = str(int(myNumber + "7" + str(int(int(myNumber) / 5.48 * 1.433))) + 259)
    else:
      myNumber = str(int(myNumber + "13" + str(int(int(myNumber) / 9.384 * 1.598))) + 347)
    itsA = None
    if int(myNumber) > tidyNumberB:
      itsA = False
    elif int(myNumber) < tidyNumberA:
      itsA = True
    while int(myNumber) > tidyNumberB or int(myNumber) < tidyNumberA:
      if int(myNumber) > tidyNumberB:
        if itsA == True:
          myNumber = str(int(myNumber) - (tidyNumberB - tidyNumberA))
          continue
        if len(myNumber) == 1:
          myNumber = str(int(myNumber) - (tidyNumberB - tidyNumberA))
        else:
          myNumber = str(int(int(myNumber) / theTidyIteration))
        itsA = False
      elif int(myNumber) < tidyNumberA:
        myNumber += str((int(myNumber) % 4) + 1)
        itsA = True
      print("haha")
    if theTidyIteration > 2555:
      theTidyIteration = 1
    theTidyIteration += 1
    print(myNumber)
    yield int(myNumber)
