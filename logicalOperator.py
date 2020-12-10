five = 5
two = 2
naught = 0
zero = 0


res = (five or zero, naught or zero, five and zero, five and two, not zero, not five)

print(res)

print(two or (five or zero))