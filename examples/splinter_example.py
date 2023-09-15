from splinter import Browser

browser = Browser()
browser.driver.maximize_window()
browser.visit('http://castalio.info/')

browser.find_link_by_href('http://castalio.info/archives.html').click()

element = browser.find_by_css('#archives p a').first
print(element.text)

browser.quit()
