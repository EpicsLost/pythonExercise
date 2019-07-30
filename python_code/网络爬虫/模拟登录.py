from selenium import webdriver

browser = webdriver.Chrome()

url = "https://passport.baidu.com/v2/?login"
browser.get(url)

browser.find_element_by_id("txtUserName").send_keys("070616014")
browser.find_element_by_id("TextBox2").send_keys("3401221998dj")
loginButton = browser.find_element_by_id("TANGRAM__PSP_3__submit")
loginButton.click()