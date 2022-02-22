AB = input()

if len(AB) == 4:
    print(20)
elif len(AB) == 2:
    print(int(AB[0]) + int(AB[1]))
elif AB[2] == '0':
    print(int(AB[0]) + 10)
else:
    print(10 + int(AB[2]))