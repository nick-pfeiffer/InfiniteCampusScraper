from config import *
import time

# each function navigates to a tab on the menu in IC

def calendar(): 
    pass

def assignments(): 
    pass

def grades():
    # nav to menu
    menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-header > header > ic-menu-toggle > button')))
    menu.click()

    # nav to grades tab
    gradesTab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#navigation-top > ic-sidebar > div > ic-tool-list > nav > ul > li:nth-child(4) > a')))
    gradesTab.click()

    # wait for proper url cause IC is slow
    wait.until(lambda d: 'grades' in d.current_url) 

    # switch the frame cause IC uses iframe >:[
    wait.until(EC.frame_to_be_available_and_switch_to_it('main-workspace'))

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
