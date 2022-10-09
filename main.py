# ******************************
# Make your Code
# ******************************
name = input().split()
names = []

for i in range(len(name)):
    names.append(name[i])

shortest = names[i]
longest = names[i]
for i in range(len(names)):
    if len(names[i]) < len(shortest):
        shortest = names[i]
        continue
    elif len(names[i]) == len(shortest):
        if names[i] < shortest:
            shortest = names[i]
            continue
    if len(names[i]) > len(longest):
        longest = names[i]
        continue
    elif len(names[i]) == len(longest):
        if names[i] < longest:
            longest = names[i]
            continue

print(shortest,longest)