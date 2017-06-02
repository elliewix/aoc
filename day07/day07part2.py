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

all_brackets = re.compile(r'\[[a-z]+?\]')
bracket_kill = re.compile(r"\[[a-z]+\]")

aba = re.compile(r'([a-z])([a-z])\1')

goods = 0

for ip in data:
    brackets = re.findall(all_brackets, ip)
    bracket_text = "".join(brackets)
    not_bracket_text = re.sub(bracket_kill, '|', ip)

    # print(bracket_text)
    in_bracket = re.search(aba, bracket_text)
    if in_bracket == None:
        continue

    # get in bracket matches
    edge_l_bracket = in_bracket.group(1)
    middle_l_bracket = in_bracket.group(2)

    out_bracket_text = middle_l_bracket + edge_l_bracket + middle_l_bracket

    if edge_l_bracket == middle_l_bracket:
        # print("NOPE DUPES")
        continue

    if out_bracket_text in not_bracket_text:
        print("YES!")
        print(ip)
        print(edge_l_bracket, middle_l_bracket)

        goods += 1




print(goods)
