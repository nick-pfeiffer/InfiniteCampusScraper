from config import *

def log(): 
    # find the username and password box, login button and complete the form
    userBox = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    passBox = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    loginBtn = driver.find_element_by_css_selector('#login > input.info.block')

    userBox.send_keys(username)
    passBox.send_keys(password)
    loginBtn.click()
    
    # wait cause IC is slow
    wait.until(lambda d: 'today' in d.current_url)

