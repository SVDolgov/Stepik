d = int(input())
ds = set()
for i in range(d):
    ds.add(input())
l = int(input())
ls = list()
ew = set()
for i in range(l):
    s = input().split()
    ls.append(s)
    for w in s:
        if w not in ds:
            ew.add(s)
for w in ew:
    print(w)