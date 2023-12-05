import string

totalVal, count, val1, val2,  val3 = 0, 0, 0, 0, 0
with open("AoCProblem1.txt", "r") as openFile:
  while True:
    char = openFile.read(1)

    if char in '\n':
      val3 = val1 + int(val1/10) if val2 == 0 else val1+ val2
      totalVal+=val3
      val2, count = 0,0

    if not char:
      break

    if char in string.digits:
      if count == 0:
        val1 = int(char) * 10
        count+=1

      else:
        val2 = int(char)

print(totalVal)  

