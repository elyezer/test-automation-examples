from splinter import Browser

browser = Browser()
browser.driver.maximize_window()
browser.visit('https://www.python.org/')

element = browser.find_by_css('.introduction > p')
print element.text

browser.quit()
