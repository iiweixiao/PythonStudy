#  pip install pymysql

# 连接mysql数据库
import pymysql

# 打开数据库连接 创建数据库时要记得声明编码类型
# db = pymysql.connect(host="localhost", user="root", password="mysql", port=3306, database="python_test",
db = pymysql.connect(host="localhost", user="root", password="ws3614wx", port=3306)
                     # charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select version()")

# 使用fetchone()获取数据
data = cursor.fetchone()
print("数据库版本为:", data)

# 关闭数据
db.close()
