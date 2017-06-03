# An ABBA is any four-character sequence which consists of a pair of two different characters
# followed by the reverse of that pair, such as xyyx or abba.
# However, the IP also must not have an ABBA within any hypernet sequences,
# which are contained by square brackets.

# test data should be
# yes
# no
# no
# yes

# this never worked to get the right answer and I don't know why

import re

with open('input.txt', 'rt') as fin:
    data = [d.strip() for d in fin.readlines()]

all_brackets = re.compile(r'.*\[([a-z]+)\].*')
bracket_kill = re.compile(r"\[[a-z]+\]")

aba = re.compile(r'(\w)(\w)\1')

goods = 0

for ip in data:
    brackets = re.findall(all_brackets, ip)
    bracket_text = " ".join([b.replace("[", "").replace("]", "") for b in brackets])
    not_bracket_text = re.sub(bracket_kill, '|', ip)

    new_ip = not_bracket_text + "[" + bracket_text

    abas = ["".join(b) for b in re.findall(r'([a-z])([^\1])(\1)', not_bracket_text) if b[0] != b[1]]

    print(abas)

    babs = [a[1] + a[0] + a[1] for a in abas]

    print(babs)

    for b in babs:
        if b in bracket_text:
            goods += 1
            break
    #
    # # print(bracket_text)
    # inside_bracket_findings = re.findall(aba, bracket_text)
    # # print(inside_bracket_findings)
    # if len(inside_bracket_findings) == 0:
    #     continue
    # else:
    #     print("start")
    #     print(ip)
    #     print(bracket_text)
    #     for pair in inside_bracket_findings:
    #         print(pair)
    #         if pair[0] == pair[1]:
    #             print("dupes")
    #         else:
    #             bab = pair[1] + pair[0] + pair[1]
    #             if bab in not_bracket_text:
    #                 goods += 1
    #                 break



print(goods)





    #
    # # get in bracket matches
    # edge_l_bracket = inside_bracket_findings.group(1)
    # middle_l_bracket = inside_bracket_findings.group(2)
    #
    # out_bracket_text = middle_l_bracket + edge_l_bracket + middle_l_bracket
    #
    # if edge_l_bracket == middle_l_bracket:
    #     # print("NOPE DUPES")
    #     continue
    #
    # if out_bracket_text in not_bracket_text:
    #     print("YES!")
    #     print(ip)
    #     print(edge_l_bracket, middle_l_bracket)
    #
    #     goods += 1




print(goods)
