alias = input()
# N = int(input())
# rings = [input() for _ in range(N)]
result = 0

# for ring in rings:
#     for i in range(len(ring)):
#         if (ring[i:] + ring[:i]).startswith(alias):
#             result += 1
#             break

for _ in range(int(input())):
    if alias in input() * 2:
            result += 1
print(result)