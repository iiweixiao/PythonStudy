from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("百度一下")
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"su")))#显式等待
    driver.find_element(By.ID, "su").click()
    driver.quit()