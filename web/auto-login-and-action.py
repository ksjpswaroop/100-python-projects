'''
Scheduled Auto Login and Action
Every X seconds logs into Mastodon, post a message and then logs out.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def connect_mastodon():
    url = "https://mastodon.social/auth/sign_in"
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def toot_mastodon(usernameStr, passwordStr, message):
    #connect to mastodon
    browser = connect_mastodon()

    # fill in username and password and hit login
    username = browser.find_element_by_id("user_email")
    username.send_keys(usernameStr)

    password = browser.find_element_by_id("user_password")
    password.send_keys(passwordStr)

    signInButton = browser.find_element_by_name("button")
    signInButton.click()

    # wait for transition then continue to fill items
    textarea = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".compose-form .autosuggest-textarea__textarea")))
    textarea.send_keys(message)
    tootbutton = browser.find_element_by_css_selector(".compose-form__publish-button-wrapper .button.button--block")
    tootbutton.click()

    time.sleep(3)

    #logout
    logout = browser.find_element_by_css_selector(".drawer__tab[title='Logout']")
    logout.click()
    time.sleep(3)
    browser.quit()


username = "username"
password = "password"
message = "test message"

while True:
    toot_mastodon(username, password, message)
    time.sleep(1000)
