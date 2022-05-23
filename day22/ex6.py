lsts = []
info = []
with open('data.txt', 'r') as f:
    lsts = f.readlines()

print(lsts)
keys = lsts[0].strip().split(',')
for s in lsts:
    if s == lsts[0]:
        continue
    values = s.strip().split(',')
    info.append(dict(zip(keys, values)))
    print(dict(zip(keys, values)))
print(info)
