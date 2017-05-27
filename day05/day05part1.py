import hashlib



with open('testdata.txt', 'rt') as fin:
    data = [r.strip() for r in fin.readlines()]

password = ""

base = 'abbhdwsy'


start = 0
while len(password) < 8:
    test = base + str(start)
    m = hashlib.md5()
    m.update(test.encode('utf-8'))
    hex = m.hexdigest()
    if hex[:5] == '00000':
        print("YES!")
        print(start)
        print(hex[5])
        password += hex[5]
        start += 1
    else:
        start += 1

print("the password is", password)
