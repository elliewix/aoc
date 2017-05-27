from collections import Counter

with open('input.txt', 'rt') as fin:
    data = [d.strip() for d in fin]

code = list(' ' * len(data[0]))
print(code)


for i in range(len(code)):
    letters = []
    for d in data:
        letter = d[i]
        letters.append(letter)
    counted = Counter(letters)
    most_common = counted.most_common()[-1][0]
    code[i] = most_common

print("".join(code))
