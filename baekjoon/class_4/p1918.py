expr = input().strip()
postfix_expr = ""
s = []
ops = {'+': 0, '-': 0, '*': 1, '/': 1}
for char in expr:
    if char == '(':
        s.append('(')
    elif char == ')':
        while s and s[-1] != '(':
            postfix_expr += s.pop()
        if s:
            s.pop()
    elif char in ops:
        while s and s[-1] in ops and ops[char] <= ops[s[-1]]:
            postfix_expr += s.pop()
        s.append(char)
    else:
        postfix_expr += char
while s:
    postfix_expr += s.pop()
print(postfix_expr)