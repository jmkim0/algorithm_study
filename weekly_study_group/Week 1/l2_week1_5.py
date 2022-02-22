lap_time = 0;

for _ in range(4):
    lap_time += int(input())
    
print(lap_time // 60)
print(lap_time % 60)
