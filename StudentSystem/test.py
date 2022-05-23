def ad(a='di',b=True):
    print(a)
    print(b)
    return True

print(ad(a='di',b=False))
name = '享学'
_ = '变量'
_9 = "享学"

print(_)
li = [1, 3, 2, "a", 4, "b", 5,"c"]
l = li[-3::-2]
print(l)

# 将列表lis中的”k”变成大写，并打印列表。
# 将列表中的数字3变成字符串”100”
# 将列表中的字符串”tt”变成数字 101
# 在 “qwe”前面插入字符串：'火车头'
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[2] = 'K'
lis[3][2][0]='K1'
print(lis)