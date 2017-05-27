import hashlib



with open('testdata.txt', 'rt') as fin:
    data = [r.strip() for r in fin.readlines()]

password = list(" " * 8)
finds = 0
base = 'abbhdwsy'


start = 0
while finds < 8:
    test = base + str(start)
    m = hashlib.md5()
    m.update(test.encode('utf-8'))
    hex = m.hexdigest()
    if hex[:5] == '00000':
        print("YES!")
        print(start)
        print(hex)
        position = hex[5]
        if position in list(map(str, range(8))):
            position = int(position)
        else:
            print("bad position", position)
            start += 1
            continue
        value = hex[6]
        if password[position] == " ":
            password[position] = value
            print(password)
            finds += 1
        else:
            print("already found")
    start += 1

print("the password is", "".join(password))
