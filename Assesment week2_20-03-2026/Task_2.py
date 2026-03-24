'''## Task 2

### Automation script for the following

Open signup page `https://automationexercise.com/signup`

Enter name & email

Select Title (Mr/Mrs) → Radio button

Select checkboxes:
`Newsletter`
`Special offers`

Use get_attribute("checked") to verify selection'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Name"]'))).send_keys("Jatin")

wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@placeholder="Email Address"])[2]'))).send_keys("dsr32eddsh@gmail.com")

btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Signup"]')))
btn.click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_gender1"]'))).click()

c_box = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]')))
for c in c_box:
    c.click()

print('Newsletter selected:',c_box[0].get_attribute('checked'))
print('Special offers selected:',c_box[1].get_attribute('checked'))

driver.quit()