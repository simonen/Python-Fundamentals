def score_calc(pract_f, theory_f):
    max_points = 187 * 0.65 + 23 * 0.35
    coeff = float(f"{(max_points / 6):.2f}")
    scored_pts = pract_f * 0.65 + theory_f * 0.35

    return scored_pts / coeff


print("### Computer Networking Fundamentals Score Calculator by don_simone")

while True:
    print(f"Your score is: {(score_calc(int(input('Enter practice test points: ')), int(input('Enter theory test points: ')))):.2f}")
