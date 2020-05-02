from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\Selenium_Drivers\Chromedriver-v81\Chromedriver.exe")
#driver = webdriver.Ie(executable_path='C:\\Selenium_Drivers\\IEDriver-32\\IEDriverServer.exe')
# driver = webdriver.Firefox()#"C:\Selenium_Drivers\Firefox-32\geckodriver.exe")
# driver = webdriver.Chrome(executable_path='C:\\Selenium_Drivers\\Chromedriver-v81\\Chromedriver.exe')
driver.get("https://www.hahi.in")

# driver.get("https://www.hahi.in")
# print(driver.title)
# print(driver.current_url)
# driver.close()
driver.implicitly_wait(10)
element1 = driver.find_element_by_xpath("//a[contains(text(),'CHECK FEATURES!')]")
# element1.is_enabled()
# element1.is_displayed()
element1.click()
