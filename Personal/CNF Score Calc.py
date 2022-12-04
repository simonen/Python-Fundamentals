def score_calc(pract_f, theory_f):
    if 0 <= pract_f <= 187 and 0 <= theory_f <= 23:
        max_points = 187 * 0.65 + 23 * 0.35
        coeff = float(f"{(max_points / 6)}")
        scored_pts = (pract_f * 0.65 + theory_f * 0.35) / coeff
        if scored_pts < 2:
            scored_pts = 2
        print()
        print(f"Your score is: {scored_pts:.2f}!")
        print()
    else:
        print()
        print("Invalid points")
        print()

print("### Computer Networking Fundamentals Score Calculator ### by don_simone")
print()

while True:
    score_calc(int(input('Enter practice test points: ')), int(input('Enter theory test points: ')))
