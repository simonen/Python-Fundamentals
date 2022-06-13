progress = int(input())

load = "%" * (progress // 10)
dots = "." * (10 - progress // 10)

if progress < 100:
    print(f"{progress}% [{load}{dots}]")
    print("Still loading...")
else:
    print("100% Complete!\n[%%%%%%%%%%]")


