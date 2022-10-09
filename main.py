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
    if len(names[i]) <= len(shortest) and names[i] < shortest:
        shortest = names[i]
    elif len(names[i]) >= len(longest) and names[i] > longest:
        longest = names[i]

print(shortest,longest)