from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/")
driver.save_screenshot("douban.png")

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > div.SignFlow-account > div.SignFlowInput.SignFlow-accountInputContainer > div.SignFlowInput-errorMask.undefined.SignFlowInput-requiredErrorMask"))).send_keys("15256923312")
driver.find_element_by_name("password").send_keys("3401221998djzh")
driver.find_element_by_class_name("Button SignFlow-submitButton Button--primary Button--blue").click()
#cap = input("请输入验证码")
#driver.find_element_by_name("username").send_keys("15256923312")