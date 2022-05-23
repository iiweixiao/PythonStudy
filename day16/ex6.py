# 京东模拟登录，自动完成滑块验证
# https://blog.csdn.net/weizhen11/article/details/102512866
import asyncio
import cv2  # pip install opencv-python
from pyppeteer import launch
from urllib import request
import random

# pyppeteer常用api https://www.jianshu.com/p/0fcf8bdf74a9
# 滑块的缺口距离识别
async def get_distance():
    img = cv2.imread('image.png', 0)  # 读入一张图像，底图；0代表默认参数，读入一副彩色图片，忽略alpha通道
    template = cv2.imread('template.png', 0)  # 读入一张图像，拼块
    # OpenCV模板匹配（cv2.matchTemplate） https://blog.csdn.net/m0_37579176/article/details/116950903
    res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)  # 模板匹配 标准相关性匹配
    value = cv2.minMaxLoc(res)[2][0]  # 寻找图像全局最大最小值
    distance = value * 278 / 360  # 这里是真实的缺口距离，放到网页中要缩放 278/360，参数要慢慢试
    return distance


# 浏览器设置
async def main():
    browser = await launch(  # 启动浏览器实例
        {'headless': False,
         "userDataDir": r"userDataDir/",  # 设置一个路径
         'args': ['--no=sandbox', '--window-size=1366,768'],
         }
    )

    page = await browser.newPage()  # 打开一个空白页
    await page.setViewport({'width': 1366, 'height': 768})
    await page.goto('https://passport.jd.com/new/login.aspx')  # 在地址栏输入网址并等待加载
    await page.waitFor(1000)  # 等待1秒钟
    await page.click('div.login-tab-r')  # 点击"账号登录"
    await page.waitFor(1000)

    # 模拟真人输入用户名、密码
    await page.type('#loginname', '123456', {'delay': random.randint(60, 121)})  # delay 延时
    await page.type("#nloginpwd", '123456', {'delay': random.randint(100, 151)})

    await page.waitFor(2000)
    await page.click("div.login-btn")  # 点击css选择器内容（登录按钮）
    await page.waitFor(3000)

    # pyppeteer.page.Page()由brower.newPage()或者brower.pages()得到
    # J()：别名querySelector()，看名字就知道通过CSS选择器来选出元素
    # JJ(): 别名querySelectorAll()
    # Jeval(): 功能比page.J()功能多一点，可以选出网页文本或者属性值
    # JJeval(): querySelectorAllEval()
    # Jx(): 别名xpath()
    # addScriptTag(): 将脚本标记添加到此页面， 返回ElementHandle其中一个url，path或content选择是必要的。

    # 模拟真人拖动滑块，失败重试  jeval
    while True:
        if await page.J('#ttbar-login'):  # 登录成功后才有此元素
            print("登录成功")
            await page.waitFor(6000)
            break
        else:
            image_src = await page.Jeval('.JDJRV-bigimg > img', 'el => el.src')  # 底图 img标签下面的src属性
            request.urlretrieve(image_src, 'image.png')  # urlretrieve 直接将远程数据下载到本地
            template_src = await page.Jeval('.JDJRV-smallimg > img', 'el => el.src')  # 拼块
            request.urlretrieve(template_src, "template.png")  # 拼块图片保存
            await page.waitFor(3000)

            el = await page.J('div.JDJRV-slide-btn')  # 选择滑动块元素
            box = await el.boundingBox()  # 返回滑动块元素的边界框，如果元素不可见，则返回 None
            await page.hover('div.JDJRV-slide-btn')  # 鼠标悬停匹配的元素
            distance = await get_distance()  # 计算距离
            await page.mouse.down()  # 按下鼠标左键
            # random.uniform(x, y) 方法将随机生成一个实数，它在 [x,y] 范围内。 'step'：20 --> 每次移动20
            await page.mouse.move(box['x'] + distance + random.uniform(30,33), box['y'], {'steps':20})  # 移动鼠标光标
            await page.waitFor(random.randint(300, 700))
            await page.mouse.move(box['x'] + distance + 29, box['y'], {'steps':20})
            await page.mouse.up()  # 松开鼠标左键
            await page.waitFor(3000)
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())
