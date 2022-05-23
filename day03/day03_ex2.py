# 作者:  Bruce
# 时间： 2022/4/19
import schedule
import time

def job():
    print("每隔3秒打印一次！")
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(2)