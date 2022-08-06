leave = input()
steps = int(input())
step_time = int(input())

seconds_walked = steps * step_time

leave = leave.split(":")
# h, m, s = map(int, leave)
hours = int(leave[0])
minutes = int(leave[1])
seconds = int(leave[2])

arrival_secs = hours * 3600 + minutes * 60 + seconds
total_secs = arrival_secs + seconds_walked

print(f"{((total_secs // 3600) % 24):02d} : {((total_secs // 60) % 60):02d} : {(total_secs % 60):02d}")
