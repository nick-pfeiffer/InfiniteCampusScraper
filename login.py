from config import *

def login(): 
    userBox = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    passBox = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    loginBtn = driver.find_element_by_css_selector('#login > input.info.block')

    userBox.send_keys(username)
    passBox.send_keys(password)
    loginBtn.click()
    
    WebDriverWait(driver, 10).until(lambda d: d.current_url == 'https://greatneckny.infinitecampus.org/campus/nav-wrapper/student/portal/student/today')

def navToGrades(): 
    WebDriverWait(driver, 10).until(lambda d: d.current_url == 'https://greatneckny.infinitecampus.org/campus/nav-wrapper/student/portal/student/today')
    menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-header > header > ic-menu-toggle > button')))
    menu.click()

    gradesTab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-sidebar > div > ic-tool-list > nav > ul > li:nth-child(4)')))
    gradesTab.click()

