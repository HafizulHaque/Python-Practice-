def getNum():
   try:
      inp = input()
      res = int(inp)
   except EOFError as error:
      return -1
   except ValueError as error:
      return -2
   return res


while True:
   num = getNum()
   if  num == -1:
      break
   elif num == -2:
      print("Invalid number")
   else:
      print(num)
      