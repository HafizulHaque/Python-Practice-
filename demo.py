cnt = 0
values = []
while True:
   try:
      inp = input()
   except EOFError as error:
      print(error)
      break
   if inp:
      cnt += 1
      values.append(inp)
   else:
      print("null string")
      continue
print("total numbers entered: ", cnt)
print(values)