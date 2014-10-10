from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.python.org/')

element = browser.find_element_by_css_selector('.introduction > p')
print element.text

browser.close()
