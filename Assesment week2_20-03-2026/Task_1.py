'''## Task 1

### Automation script for amazon.com

Open Amazon

Verify page title and current URL

Locate the category dropdown (next to search bar)

Select "Books" using Select class

Enter "Harry Potter" in search and press Enter

Use explicit wait to wait until results are visible

Get all product titles using find_elements

Print first 5 product names

Click on the first product'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.maximize_window()

driver.get("https://www.amazon.com")

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue shopping"]'))).click()
except:
    pass

dd = Select(wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox"))))
dd.select_by_visible_text("Books")


s_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
s_box.send_keys("Harry Potter", Keys.ENTER)


print("Top 5 Products:")
for i in range(1, 6):
    print(driver.find_element(By.XPATH, f"(//div[@class='a-section a-spacing-small a-spacing-top-small']//a/h2/span)[{i}]").text)

driver.find_element(By.XPATH, f"(//div[@class='a-section a-spacing-small a-spacing-top-small']//a/h2/span)[1]").click()

driver.quit()