from selenium import webdriver

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# binary = FirefoxBinary('path/to/binary')
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get('http://localhost:8080')
assert 'Django' in browser.title
