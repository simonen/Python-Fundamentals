import re

dates = input()
days = 2
years = 4
match = re.finditer(r"(\d{2})(\/|\.|-)([A-Z][a-z]{2})(\2)(\d{4})", dates)

for m in match:
    day = m.group(1)
    month = m.group(3)
    year = m.group(5)
    print(f"Day: {day}, Month: {month}, Year: {year}")
