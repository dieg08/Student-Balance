from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#the website address that we want to open
url = "http://www.wcu.edu/student-life/division-of-student-affairs/departments/campus-services/catcard-office/catcard-balance-inquiry.asp"

#an instance of the firefox webdriver is created
driver = webdriver.Firefox()

#navigates to the given url 
driver.get(url)

#makes sure wcu is in the url title
#assert "wcu" in driver.title

#get the 920 textbox
ID = driver.find_element_by_name("id")

#prompts user for 920 number
print "Enter your 920 Number:"
num = raw_input()

#sends input to webpage
ID.send_keys(num)

#get password textbox
password = driver.find_element_by_name("PIN")

#prompts user for password
print "Enter Password:"
pin = raw_input()

#sends password to webpage
password.send_keys(pin)

#equivalent of hitting submit button
submit = driver.find_element_by_name("submit")
submit.send_keys(Keys.RETURN)

#closes firefox driver
driver.close
