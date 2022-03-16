from selenium import webdriver

# Edit the following variables accordingly.
username = "user"
password = "1234"
website = "https://www.example.com"
chromeDriver_path = "../chromedriver.exe"

# Opens the website in Google Chrome.
driver = webdriver.Chrome(executable_path=chromeDriver_path)
driver.maximize_window()
driver.get(website)

# For the following, use inspect element in browser to find Html values and edit accordingly.
# Key in username in username input field.
driver.find_element_by_id("userid").send_keys(username)

# Key in password in password input field.
driver.find_element_by_id("pwd").send_keys(password)

# Click login button.
driver.find_element_by_name("Submit").click()


# Written by: Clarence Seah.
