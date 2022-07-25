
# importing the modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
  
# using webdriver for chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# using target url
driver.get(
    "https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
  
# printing the content of entire page
print(driver.find_element_by_xpath("/html/body").text)
  
# closing the driver
driver.close()