from config import *

def calendar(): 
    pass

def assignments(): 
    pass

def grades():
    menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-header > header > ic-menu-toggle > button')))
    menu.click()

    gradesTab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-sidebar > div > ic-tool-list > nav > ul > li:nth-child(4) > a')))
    gradesTab.click()

def gradeBookUpdates():
    pass

def attendance(): 
    pass

def schedule(): 
    pass

def fees(): 
    pass

def documents(): 
    pass

def messageCenter(): 
    pass

def more(): 
    pass
