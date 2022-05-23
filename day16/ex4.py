import asyncio
from pyppeteer import launch


async def main():  # async声明一个异步操作
    browser = await launch()  # await声明一个耗时操作. 创建浏览器对象,可以传入字典形式参数
    page = await browser.newPage()  # 创建一个新页面，页面操作可以在该对象上执行
    await page.goto("https://www.baidu.com")  # 页面跳转
    await page.screenshot({"path": "baidu.png"})  # 截图并保存
    await browser.close()  # 关闭浏览器对象


asyncio.get_event_loop().run_until_complete(main())  # 创建异步池并执行main()函数
