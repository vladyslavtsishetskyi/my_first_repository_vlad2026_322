n = input().strip()
k = int(input().strip())

digits = list(n)
m = ""
pos = 0
while digits:
    pos = (pos + k - 1) % len(digits)
    m += digits.pop(pos)

print(m)
print("YES" if int(m) % 3 == 0 else "NO")
