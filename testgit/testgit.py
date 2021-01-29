"""
打印小猫爱吃鱼，小猫要喝水
对象是：小猫
类是：鱼和水
"""
# # 定义一个类
# class Cat():
#     # 定义初始化对象 小猫
#     def __init__(self):
#         self.cat = '小猫'
#     # 定义小猫想要做的事情
#     def like(self, fish, water):
#         self.fish = fish
#         self.water = water
#     # 打印结果
#     def __str__(self):
#         return f'{self.cat}爱吃{self.fish},{self.cat}想要喝{self.water}.'
# # 实例化对象
# cat = Cat()
# cat.like('鱼', '水')
# print(cat)


"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""
# # 定义小明的一个类
# class Name():
#     def like(self):
#         # 打印小明的爱好
#         print(f'{self.name}爱{self.like1},{self.name}爱{self.like2}')
#     def weight(self):
#         # 打印小明体重
#         print(f'{self.name}的体重是{self.weight1}kg')
#     def movement(self, loseweight, gainweight):
#         self.loseweight = loseweight
#         self.gainweight = gainweight
#     def __str__(self):
#         return f'小明每次跑步减少{self.loseweight}kg, 每次饭后会增加{self.gainweight}kg'
# # 创建对象
# xiaoming = Name()
# # 实例化对象
# xiaoming.name = '小明'
# xiaoming.like1 = '跑步'
# xiaoming.like2 = '吃东西'
# xiaoming.like()
# xiaoming.weight1 = 75.0
# xiaoming.weight()
# xiaoming.movement(0.5, 1)
# print(xiaoming)
# # 定义小美的一个类
# class Name1():
#     def weight(self):
#         print(f'{self.name}的体重是{self.weight2}kg')
# # 创建对象
# xiaomei = Name1()
# # 实例化对象
# xiaomei.name = '小美'
# xiaomei.weight2 = 45
# xiaomei.weight()

"""

3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

"""
# # 定义一个家具的类
# class furniture():
#     def __init__(self, furnname, furnares):
#         self.furnname = furnname
#         self.furnares = furnares
# # 定义一个房子的类型
# class home():
#     def __init__(self, model, zares):
#         # 房子的户型
#         self.model = model
#         # 房子的总面积
#         self.zares = zares
#         # 房子的剩余面积
#         self.sares = zares
#         # 家具的类型
#         self.furnit = []
#     # 打印房间信息
#     def __str__(self):
#         return f'该房间的户型是{self.model}, 总面积为{self.zares}平米, 剩余面积是{self.sares}平米, 里边的家具都有{self.furnit}.'
#     # 添加房屋家具
#     def call(self, furniture):
#         # 判断家具占地面积小于等于剩余面积
#         if furniture.furnares <= self.sares:
#             # 将家具名称添加到房间中家具列表里
#             self.furnit.append(furniture.furnname)
#             # 从剩余面积中减去家具的占地面积
#             self.sares -= furniture.furnares
#         # 如果家具占地面积大于剩余面积打印的结果
#         else:
#             print("房间面积不够")
# # 实例化信息
# # 床  4平米
# bed = furniture('床', 4)
# home1 = home('两室一厅', 85)
# print(home1)
# # 调用添加的家具
# home1.call(bed)
# print(home1)
# # 衣柜 2平米
# closet = furniture('衣柜', 2)
# home1.call(closet)
# print(home1)
# # 餐桌 1.5平米
# table = furniture('衣柜', 2)
# home1.call(table)
# print(home1)