# 作者:  Bruce
# 时间： 2022/4/19

import os

os.system('notepad.exe')  # Windows下 打开记事本
os.startfile('D:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQ.exe')  # Windows下 打开QQ程序
os.system('open /System/Applications/Notes.app')  # MacOS下 打开备忘录
print('---')
print(os.getcwd())  # 获取当前python文件路径
lst = os.listdir('/Users/brucewei/Downloads')  # 列出目录下文件
print(lst)
os.mkdir('wenjianjia')  #创建文件夹
os.makedirs('a/b/c')  #创建多级文件夹
os.rmdir('wenjianjia')
os.removedirs('a/b/c')
print(os.path.exists('a/b/c'))  # 配合if先做判断，再做创建或删除动作避免报错

# import os.path  #如果只用到os.path下到命令可以这么写
print(os.path.abspath('126demo1.py'))  #用于获取文件或目录的绝对路径
print(os.path.exists('126demo1.py'), os.path.exists('abc.py'))  #用于判断文件或目录是否存在，如果存在返回True,否则返回False
print(os.path.join('D:\pythonStu', '126demo1.py'))  #将目录与目录或者文件名拼接起来
print(os.path.split('D:\\pythonStu\\126demo1.py'))  #将目录与目录或者文件名拼接起来
print(os.path.splitext('126demo1.py'))  #分离文件名和扩展名
print(os.path.basename('D:\\pythonstu\\126demo1.py'))  #从一个目录中提取文件名
print(os.path.dirname('D:\\pythonstu\\126demo1.py'))  #从一个路径中提取文件路径，不包括文件名
#列出后缀名为py的文件
path = os.getcwd()
lst = os.listdir(path)
for fileName in lst:
    if fileName.endswith('.py'):
        print(fileName)