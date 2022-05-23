cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']

# 根据cars得到如下结构
# info = {'鲁': 2, '黑': 3, '京': 1, '沪': 1}

di = {}
for i in cars:
    print(i)
    di[i[0]] = di.get(cars[0], 0) + 1

print(di)