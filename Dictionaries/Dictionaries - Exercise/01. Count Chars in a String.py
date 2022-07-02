# string = "text text text"
# text = text.replace(" ", "")
text_d = {}
text = "".join([x for x in input().split()])

for char in text:
    key = char
    value = text.count(char)
    text_d[key] = value

for k, v in text_d.items():
    print(f"{k} -> {v}")
