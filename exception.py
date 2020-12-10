s = input("input an integer:")
try:
    inp = int(s)
    res = 10/inp
    print(10, "/", inp, "=", res)
except ValueError as error1:
    print(error1)
except ZeroDivisionError as error2:
    print(error2)