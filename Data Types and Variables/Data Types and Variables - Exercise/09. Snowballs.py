n = int(input())

max_value = -10000000
m_weight = 0
m_time = 0
m_quality = 0

for i in range(1, n + 1):
   weight = int(input())
   time = int(input())
   quality = int(input())
   value = (weight / time ) ** quality
   if value > max_value:
       max_value = value
       m_weight = weight
       m_time = time
       m_quality = quality

print(f"{m_weight} : {m_time} = {max_value:.0f} ({m_quality})")