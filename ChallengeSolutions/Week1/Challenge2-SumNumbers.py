# Challenge 2 - Sum Numbers (09/16/2021)
import sys
if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = 10
print()
print(f"Summing the first {n} numbers...")

c = 0
for x in range(1,n+1):
    c = c + x
    #print(c)

print(f"For Loop Answer = {c}")

c = 0
x = 1
while x <= n:
    c = c + x
    #print(c)
    x += 1

print(f"While Loop Answer = {c}")
print()