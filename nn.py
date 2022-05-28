file = input("pls type a text")
if len(file) < 1 : file = "clown.txt"
count = 0
for line in file:
    word = line.split(" ")
    count += len(word)
print(count)
