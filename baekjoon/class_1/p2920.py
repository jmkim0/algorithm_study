tone_list = input().split(" ")
ascending = True
descending = True
for i in range(7):
    if tone_list[i] > tone_list[i + 1]:
        ascending = False
    if tone_list[i] < tone_list[i + 1]:
        descending = False
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
