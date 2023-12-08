import re

totalVal = 0
with open("AoCProblem1.txt", "r") as openFile:
  while True:

    calibrationVal = (re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))',openFile.readline()))

    if not calibrationVal:
      break

    match calibrationVal[0]:
      case 'one'|'1':
        calibrationVal[0] = 1
      case 'two'|'2':
        calibrationVal[0] = 2
      case 'three'|'3':
        calibrationVal[0] = 3
      case 'four'|'4':
        calibrationVal[0] = 4
      case 'five'|'5':
        calibrationVal[0] = 5
      case 'six'|'6':
        calibrationVal[0] = 6
      case 'seven'|'7':
        calibrationVal[0] = 7
      case 'eight'|'8':
        calibrationVal[0] = 8
      case 'nine'|'9':
        calibrationVal[0] = 9

    match calibrationVal[len(calibrationVal)-1]:
      case 'one'|'1':
        calibrationVal[len(calibrationVal)-1] = 1
      case 'two'|'2':
        calibrationVal[len(calibrationVal)-1] = 2
      case 'three'|'3':
        calibrationVal[len(calibrationVal)-1] = 3
      case 'four'|'4':
        calibrationVal[len(calibrationVal)-1] = 4
      case 'five'|'5':
        calibrationVal[len(calibrationVal)-1] = 5
      case 'six'|'6':
        calibrationVal[len(calibrationVal)-1] = 6
      case 'seven'|'7':
        calibrationVal[len(calibrationVal)-1] = 7
      case 'eight'|'8':
        calibrationVal[len(calibrationVal)-1] = 8
      case 'nine'|'9':
        calibrationVal[len(calibrationVal)-1] = 9

    totalVal += (calibrationVal[0] * 10) + calibrationVal[len(calibrationVal)-1]

print(totalVal)


