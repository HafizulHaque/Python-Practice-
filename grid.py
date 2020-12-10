import random

def getNum(msg, defaultVal, minVal, maxVal):
   while True:
      inp = input(msg)
      if not inp:
         return defaultVal
      else:
         try:
            ret = int(inp)
            if not minVal <= ret <= maxVal:
                print("Number Not in Range. Recheck range & input again")
                continue
         except ValueError:
            print("Invalid number. Enter a valid number")
         return ret

def makeGrid(rows, cols, minNumber, maxNumber):
   space = "     "
   row = 0
   while row < rows:
      col = 0
      rowStr = ""
      while col < cols:
         rowStr += space
         randNum = random.randint(minNumber, maxNumber)
         if randNum < 10:
            rowStr += "   "
         elif 10 <= randNum <= 99:
            rowStr += "  "
         elif 100 <= randNum <= 999:
            rowStr += " "
         rowStr += str(randNum)
         col = col+1
      rowStr += space
      print(rowStr)
      row = row+1




rows = getNum("Rows (press enter for default value '5') [1<=rows<=10]    : ", 5, 1, 10)
cols = getNum("Columns (press enter for default value '6') [1<=cols<=8] : ", 6, 1, 8)
minNumber = getNum("Enter minimum number (press enter for default value '0') [0<=val<=100] : ", 0, 0, 100)
maxNumber = getNum("Enter maximum number ( press enter for default value 500) [200<=val<=9999]: ", 500, 200, 9999)

makeGrid(rows, cols, minNumber, maxNumber)