# start time + time(seconds) = end time in format 00:00:00
def calculate_time(start_time_f, time_taken_f):
    start_f = start_time_f.split(":")
    hours_f, minutes_f, seconds_f = map(int, start_f)
    time_to_secs = hours_f * 3600 + minutes_f * 60 + seconds_f
    total_secs_f = time_to_secs + time_taken_f
    return f"{((total_secs_f // 3600) % 24):02d}:{((total_secs_f // 60) % 60):02d}:{(total_secs_f % 60):02d}"


start_time = input()
command = input()

while command != "stop":
    time_taken = int(command)
    print(f"Time of arrival: {calculate_time(start_time, time_taken)}")
    start_time = calculate_time(start_time, time_taken)
    command = input()
