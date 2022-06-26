biscuit_per_worker = int(input())
workers = int(input())
competition = int(input()) # in 30 days

total_biscuits = 0

for day in range(1, 31):
    daily_biscuits = biscuit_per_worker * workers
    if day % 3 == 0:
        daily_biscuits = int(daily_biscuits * 75 / 100)

    total_biscuits += daily_biscuits

percentage = (total_biscuits / competition) * 100

print(f"You have produced {int(total_biscuits)} biscuits for the past month.")

diff = abs(100 - percentage)
if total_biscuits > competition:
    print(f"You produce {diff:.2f} percent more biscuits.")
else:
    print(f"You produce {diff:.2f} percent less biscuits.")