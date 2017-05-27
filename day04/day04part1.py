# Each room consists of an
# encrypted name (lowercase letters separated by dashes)
# followed by a dash, a sector ID, and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters
# in the encrypted name, in order, with ties broken by alphabetization. For example:

# aaaaa-bbb-z-y-x-123[abxyz],True
# a-b-c-d-e-f-g-h-987[abcde],True
# not-a-real-room-404[oarel],True
# totally-real-room-200[decoy],True

from collections import Counter

with open('data.txt', 'rt') as fin:
    text = [r.strip().split("-") for r in fin.readlines()]

sectors_collect = []

for dat in text:
    *name, ids = dat
    encrypted_name = "".join(name)
    id_sum = dat[-1].replace(']', '').split('[')
    sector_id = id_sum[0]
    checksum = id_sum[1]
    counted_letters  = {}
    # print(encrypted_name)
    counts = Counter(encrypted_name)
    # print(counts)

    for letter, count in counts.items():
        if count not in counted_letters:
            counted_letters[count] = [letter]
        else:
            counted_letters[count].append(letter)

    count_keys = list(counted_letters.keys())
    count_keys.sort(reverse=True)
    # print(count_keys)

    letters_collect = []

    for num in count_keys:
        letters = counted_letters[num]
        letters.sort()
        letters_collect += letters

    real_letters = "".join(letters_collect)[:5]

    if real_letters == checksum:
        print("is real room!")
        sectors_collect.append(int(sector_id))
    else:
        print("not a real room")

print(sum(sectors_collect))
