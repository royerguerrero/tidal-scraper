from selenium import webdriver
from getpass import getpass
import sys


def get_credentials():
    if sys.argv[1] == '--envs-auth':
        print('[!] You are use environment varibales for auth credentials.')
    
    print('[Tip] You can pass the --envs-auth to user environment variable for authentication.')
    username = input('What is your usermail/email? ')
    password = getpass(prompt='What is your password? ')
    return (username, password)

def login(driver, credentials):
    login_button = driver.find_element_by_xpath('//*[@id="sidebar"]/section[1]/button[1]')
    login_button.click()

    email_input = driver.find_element_by_name('email')
    email_input.send_keys(credentials[0])
    
    error_message = driver.find_element_by_xpath('/div/div[1]')
    print(f'The user {credentials[0]} is not valid')
    
    
def web_scraper(credentials):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://listen.tidal.com/')
    driver.maximize_window()
    
    login(driver, credentials)


if __name__ == '__main__':
    print("""  
         _____________  ___   __           ___  __            __   _     __ 
        /_  __/  _/ _ \/ _ | / /    ____  / _ \/ /__ ___ __  / /  (_)__ / /_
         / / _/ // // / __ |/ /__  /___/ / ___/ / _ `/ // / / /__/ (_-</ __/
        /_/ /___/____/_/ |_/____/       /_/  /_/\_,_/\_, / /____/_/___/\__/ 
                                            /___/                   
                Web scraper to export to CSV or JSON yout tidal playlist 
          """)
    credentials = get_credentials()
    web_scraper(credentials)