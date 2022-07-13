title = input()
article = input()
comment = input()

print("<h1>")
print(f"\t{title}")
print("</h1>")
print("<article>")
print(f"\t{article}")
print("</article>")

while comment != "end of comments":
    print("<div>")
    print(f"\t{comment}")
    print("</div>")

    comment = input()
