century = int(input())

years = century * 100
days = float(years) * 365.2422
hours = float(days) * 24
minutes = hours * 60

print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")