import asyncio
from pyppeteer import launch


# width, height = 1600, 800  # 尺寸配置


async def main():
    browser = await launch(
        headless=False,
        args=['--disable-infobars', '--window-size=1600,800'],
    )  # 格式化输出
    page = await browser.newPage()  # 打开新页面

    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    await page.goto("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    await page.screenshot({"path": "baidu.png"})  # 截图并保存
    # await browser.disconnect()
    # print(browser.process)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
