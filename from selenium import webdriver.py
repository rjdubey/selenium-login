from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set the path to the chromedriver executable
driver_path = r"C:\Users\Rahul\Downloads\chromedriver_win32\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Set the timeout duration
timeout = 10

try:
    # Navigate to the LinkedIn website
    driver.get("https://www.linkedin.com")

    # Wait for the login form to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.presence_of_element_located((By.ID, "session_key")))

    # Find the email input field and enter your email
    email = driver.find_element(By.ID, "session_key")
    email.send_keys("rahuldubey@gmail.com")

    # Find the password input field and enter your password
    password = driver.find_element(By.ID, "session_password")
    password.send_keys("123456")

    # Find the Sign In button and click it
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()

    # Wait for the messaging element to appear
    wait.until(EC.presence_of_element_located((By.ID, "messaging-nav-item")))

    # Find the messaging element and click it
    messaging_nav_item = driver.find_element(By.ID, "messaging-nav-item")
    messaging_nav_item.click()

    # Find the recipient input field and enter the recipient's name
    recipient_input = driver.find_element(By.XPATH, "//input[@placeholder='Search for people']")
    recipient_input.send_keys("Recipient Name")

    # Wait for the search results to appear
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'People')]")))

    # Select the first search result
    first_search_result = driver.find_element(By.XPATH, "//span[contains(text(), 'People')]/../following-sibling::div//li[1]")
    first_search_result.click()

    # Find the message input field and enter your message
    message_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
    message_input.send_keys("Hello, I am Rahul Dubey.")

    # Find the Send button and click it
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
    send_button.click()

    # Print a success message
    print("Message sent successfully!")

except TimeoutException:
    print("Timeout occurred while waiting for an element to load.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Quit the driver and close the browser
    driver.quit()
