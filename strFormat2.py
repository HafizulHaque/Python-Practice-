d = dict(animal="Elephant", attr="enormous")

string = '{animal} is {attr}.'

print(string.format(**d))