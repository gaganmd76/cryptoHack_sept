label = "label"

new_string = ""

for ch in label:
    new_string += chr(ord(ch) ^ 13)

print(f"crypto{{{new_string}}}")