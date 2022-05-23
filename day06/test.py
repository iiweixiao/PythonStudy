# 综合题
# 1.车牌区域划分，请根据车牌信息，分析出各省的车牌持有数量.
#cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
# 根据cars得到如下结构
# info = {'鲁': 2, '黑': 3, '京': 1, '沪': 1}

cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
li = []
for car in cars:
    li.append(car[0])
li = list(set(li))
info = []
for l in li:
    d = {l, str(cars).find(l)}
    info.append(d)
print(info)

#
# user_list = [
#     {'username': 'zs', 'password': '1234'},
#     {'username': 'ls', 'password': 'asdf'}
# ]

# board = ['zs', 'ls', 'ww']
# while True:
#     user_name = input("请输入用户名['输入Q或者q时退出程序']：")
#     if user_name.lower() == 'q':
#         print("退出程序")
#         break
#
#     else:
#         if user_name in board:
#             user_name = "*" * len(user_name)
#
#         pwd = input("请输入密码")
#         dic = {}
#         dic["username"] = user_name
#         dic['password'] = pwd
#         user_list.append(dic)
#         print(user_list)

# print('000'.isdigit())
# print('000'.isdecimal())

product_list = [{'name': '苹果', 'price': 10},

                {'name': '榴莲', 'price': 30},

                {'name': '草莓', 'price': 20},

                {'name': '菠萝', 'price': 15}, ]

# 1.创建一个购物车来盛放水果

shopping_cart = {}

# 2.提示用户输入钱

money_str = input('请展示一下你的钱:')

if money_str.isdigit():

    '''是数字'''

    user_money = int(money_str)  # 类型转换

    # 3.展示商品

    for index, dic in enumerate(product_list, start=1):
        print("水果的序号:{},名称:{},价格:{}".format(index, dic['name'], dic['price']))

    while True:

        # 4.输入序号

        num_xh_str = input("请输入序号:")

        if num_xh_str.isdigit():

            '''输入的是一个数字'''

            num_xh = int(num_xh_str)  # 类型转换

            if num_xh > 0 and num_xh <= len(product_list):

                '''输入的序号范围在产品列表范围内'''

                # 5.输入数量

                num_sl_str = input('请输入数量:')

                if num_sl_str.isdigit():

                    '''输入的数量是数字'''

                    num_sl = int(num_sl_str)  # 类型转换

                    # 6.判断买的商品的总价格是否超过了用户的所有钱

                    # 如果没有超出，就可以添加到购物车中，如果超出了

                    # 就退出程序。

                    # (1).求商品的总价格 数量*价钱

                    # 根据序号找到水果的价格

                    num_dj = product_list[num_xh - 1]['price']  # 注意索引的获取

                    product_total_money = num_dj * num_sl  # 购买某一种水果的总价钱

                    # (2).水果总价钱和用户的钱进行比较

                    if product_total_money <= user_money:

                        # 将商品添加到购物车

                        # i. 获取序号对应的商品名称

                        product_name = product_list[num_xh - 1]['name']

                        ret = shopping_cart.get(product_name)  # 去购物车查找对于的商品名称

                        # None

                        if ret:

                            '''购物车中已经存在了此商品，只需添加数量'''

                            # 获取购物车中原有的数量

                            yysl = shopping_cart[product_name]

                            # 总共的数量

                            shopping_cart[product_name] = yysl + num_sl

                            print(shopping_cart)



                        else:

                            '''添加商品和数量'''

                            shopping_cart[product_name] = num_sl

                            print(shopping_cart)

                        # ii.去购物车进行查询如果有就添加数量如果没有就添加商品和数量

                        # 输出用户剩余的钱

                        user_money = user_money - product_total_money

                        print('用户剩余的钱：', user_money)

                    else:

                        '''商品总价格超过了用户的钱'''

                        print('亲，余额不足...')

                        break

                else:

                    '''输入的数量不是数字'''

                    print('数量是数字哦。')



            else:

                '''输入的序号超出了范围'''

                print('看清了在输入亲!!!')



        else:

            '''输入的序号不是一个数字'''

            print('序号是由数字组成,请输入数字')



else:

    '''输入的不是数字'''

    print('你的钱怎么不是数字呢，SB')