# ******************************
# Make your Code
# ******************************
name = input().split()
names = []

for i in range(len(name)):
    names.append(name[i])

shortest = name[0]
longest = name[0]
for i in range(len(names)):
    if names[i] < shortest:
        shortest = names[i]
    elif names[i] > longest:
        longest = names[i]

print(shortest,longest)