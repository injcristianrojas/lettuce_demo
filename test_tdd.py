from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.meetup.com/")
assert "Meetup" in driver.title
elem = driver.find_element_by_id("C_globalSearchInput")
elem.send_keys("Meetup Python")
elem.send_keys(Keys.RETURN)
assert "Pythoneros" in driver.page_source
driver.close()