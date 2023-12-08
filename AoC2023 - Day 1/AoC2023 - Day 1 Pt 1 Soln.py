import re

totalVal = 0
with open("AoCProblem1.txt", "r") as openFile:
  while True:
    calibrationVal = (re.findall(r'(?=([1-9]))',openFile.readline()))

    if not calibrationVal:
      break
  
    match calibrationVal[0]:
      case '1':
        calibrationVal[0] = 1
      case '2':
        calibrationVal[0] = 2
      case '3':
        calibrationVal[0] = 3
      case '4':
        calibrationVal[0] = 4
      case '5':
        calibrationVal[0] = 5
      case '6':
        calibrationVal[0] = 6
      case '7':
        calibrationVal[0] = 7
      case '8':
        calibrationVal[0] = 8
      case '9':
        calibrationVal[0] = 9

    match calibrationVal[len(calibrationVal)-1]:
      case '1':
        calibrationVal[len(calibrationVal)-1] = 1
      case '2':
        calibrationVal[len(calibrationVal)-1] = 2
      case '3':
        calibrationVal[len(calibrationVal)-1] = 3
      case '4':
        calibrationVal[len(calibrationVal)-1] = 4
      case '5':
        calibrationVal[len(calibrationVal)-1] = 5
      case '6':
        calibrationVal[len(calibrationVal)-1] = 6
      case '7':
        calibrationVal[len(calibrationVal)-1] = 7
      case '8':
        calibrationVal[len(calibrationVal)-1] = 8
      case '9':
        calibrationVal[len(calibrationVal)-1] = 9

    totalVal += (calibrationVal[0] * 10) + calibrationVal[len(calibrationVal)-1]

print(totalVal)


