for _ in range(4):
    sides = sorted(map(int, input().split()))
    if len(sides) == 1 and sides[0] == 0:
        break
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("rightangle")
    else:
        print("triangle")