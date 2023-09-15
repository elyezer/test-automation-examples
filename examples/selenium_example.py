from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('http://castalio.info/')

element = browser.find_element_by_css_selector('a[href="http://castalio.info/archives.html"]')
element.click()

element = browser.find_element_by_css_selector('#archives p:first-child a')
print(element.text)

browser.close()
