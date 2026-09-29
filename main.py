s = input().strip()
match = {')':'(', ']':'[', '}':'{'}
stack = []
for char in s:
    if char in match.values():
        stack.append(char)
    else:
        if not stack:
            print(False)
            exit()
        top = stack.pop()
        if match[char] != top:
            print(False)
            exit()
print(len(stack) == 0)
