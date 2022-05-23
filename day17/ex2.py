mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)
print('---------')
mygenerator = (x**x for x in range(3))
for i in mygenerator:
    print(i)
print('---------')

for i in mylist:
    print(i)
print('---------')

for i in mygenerator:
    print(i)
    print('haha')
print('---------')

def createGenerator():
    myl = range(3)
    for i in myl:
        yield i+6

mygenerator1 = createGenerator()
print(mygenerator1)
for i in mygenerator1:
    print(i+10)
print('---')
for i in mygenerator1:
    print(i+5)
