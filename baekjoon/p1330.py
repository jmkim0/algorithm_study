a_b = input().split(" ")
a = int(a_b[0])
b = int(a_b[1])
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")