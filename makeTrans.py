tr = str.maketrans("aeiou", "AEIOU")

s = "a lazy dog runns over a cunny fox"

print(s.translate(tr))