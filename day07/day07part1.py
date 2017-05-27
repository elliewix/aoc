# An ABBA is any four-character sequence which consists of a pair of two different characters
# followed by the reverse of that pair, such as xyyx or abba.
# However, the IP also must not have an ABBA within any hypernet sequences,
# which are contained by square brackets.

# test data should be
# yes
# no
# no
# yes

import re

with open('input.txt', 'rt') as fin:
    data = [d.strip() for d in fin.readlines()]

all_brackets = re.compile(r'\[[a-z]*([a-z])([a-z])\2\1[a-z]*\]')
bracket_kill = re.compile(r"\[[a-z]+\]")
abba_find = re.compile(r"([a-z])([a-z])\2\1")

goods = 0

for ip in data:
    brackets = len(re.findall(all_brackets, ip))
    halfs = re.sub(bracket_kill, '|', ip)
    abba = re.search(abba_find, halfs)
    abba_outside = abba != None

    if brackets > 0:
        continue
    elif abba_outside:
        abba_dupes = abba.group(1) == abba.group(2)
        if abba_dupes:
            continue
        else:
            goods += 1
    else:
        continue
print(goods)
