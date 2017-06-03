import re

def get_abas(word):
    abas = []
    for i in range(0, len(word) - 2):
        slc = word[i:i+3]
        if slc[0] == slc[2] and slc[0] != slc[1]:
            abas.append(slc)
    return abas

def support_ssl(addr):
    regex = re.compile('.*\[([a-z]+)\].*')
    hypernets = []
    while True:
        m = regex.match(addr)
        if not m:
            break
        inner = m.groups()[0]
        hypernets.append(inner)
        addr = addr.replace(inner, '')
    abas = get_abas(addr)
    for a in abas:
        bab = ''.join( [ a[1], a[0], a[1] ] )
        for h in hypernets:
            if bab in h:
                return True
    return False

with open('input.txt', 'rt') as fin:
    data = [d.strip() for d in fin.readlines()]

goods = 0

for ip in data:
    if support_ssl(ip):
        goods += 1

print(goods)
