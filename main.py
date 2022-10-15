n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
for i in range(n):
    c.append(a[i] / b[i])
c = enumerate(c)
c = sorted(c, key=lambda x: x[1], reverse=True)
x = 0
r= 0
suma = a[0]
sumb = sum(b) - b[0]
for i in range(1, n):
    if suma >= sumb:
        x = (sum(b[i - 1:]) - sum(a[:i - 1])) / (a[i - 1] + b[i - 1])
        r = i - 1
    else:
        suma += a[i]
        sumb -= b[i]
rez = 0
for i in range(n):
    if i == r:
        rez += b[i] * x
        break
    else:
        rez += b[i]
print(rez)
