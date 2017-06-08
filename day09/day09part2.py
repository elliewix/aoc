with open('input.txt', 'rt') as fin:
    text = fin.read().strip()

print(text)

real_text = ""

looking_for_parens = True

current_pos = 0

while current_pos < len(text):

    character = text[current_pos]

    if character == "(":
        end = text[current_pos:].find(")")  + current_pos
        print(text[end])
        parens = text[current_pos + 1:end]
        slice, repeat = map(int, parens.split("x"))

        slice_start = end + 1
        slice_end = slice_start + slice

        expand_text = text[slice_start: slice_end] * repeat
        print(expand_text)
        real_text += expand_text

        current_pos = slice_end
    else:
        print("here's a char", character)
        real_text += character
        current_pos += 1

print(real_text)
print(len(real_text))
