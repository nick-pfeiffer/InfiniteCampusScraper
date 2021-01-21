from config import *
from login import log
from navigation import grades
from bs4 import BeautifulSoup
from get_courses import courses
import itertools
import re

def averages():
    courseList = courses()

    # more waiting cause IC is slow
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > app-root > ng-component > app-grades > app-portal-page > div.workspace-content.workspace-content--with-toolbar > div > div > div > app-term-picker > div > div.term-picker__header > div > kendo-buttongroup')))

    source = driver.page_source
    all_subjects_soup = BeautifulSoup(source, 'html.parser')

    previous = None

    # what will be returned
    averages = {}

    for sub, cur_course in zip(all_subjects_soup.find_all('div', {'class': 'collapsible-card__content'}), courseList):
        # switch frame to default frame so it can then switch to the proper frame 
        driver.switch_to.default_content()
        wait.until(EC.frame_to_be_available_and_switch_to_it('main-workspace'))

        cur_selector = '#' + str(sub.get('id'))
        arrow_selector = cur_selector + '> app-grading-task-list > table > tbody > tr > a > div > div:nth-child(3)'

        see_grades = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, cur_selector)))

        try: 
            driver.find_element_by_css_selector(arrow_selector)
        except: 
            previous = arrow_selector
            continue

        see_grades.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#k-tabstrip-tabpanel-2 > app-term-picker > div > div.term-picker__header.ng-star-inserted > div > kendo-buttongroup')))

        cur_subject_soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        cat_dict = {}

        previous_total_earned=previous_total_possible = 0
        for cat in cur_subject_soup.find_all('button', {'class': 'divider__item divider__header ng-star-inserted'}):
            category = re.sub(r'Weight: \d*', '', cat.text).strip()
            xpath_search = "//*[contains(text(), '" + re.sub(r'Weight: \d*', '', cat.text).strip() + '\')]'

            cur_cat = driver.find_element_by_xpath(xpath_search)
            cur_cat.click()
            
            wait.until(EC.visibility_of_element_located((By.XPATH, "//i[contains(@class, 'fa divider__icon fa-minus')]")))

            grades_in_category_soup = BeautifulSoup(driver.page_source, 'html.parser')

            total_earned=total_possible=score = 0

            for cur_score in grades_in_category_soup('li', {'class': 'assignment__row break-word clickable flex--space-between ng-star-inserted'}):
                try: 
                    # score: earned/possible  (percentNumber%)
                    score = cur_score.find(class_='pl-1').extract().text

                    total_earned += float(score.split('  ')[0].split('/')[0])
                    total_possible += float(score.split('  ')[0].split('/')[1])
                except: 
                    # exception called if no grade is given in IC (so just skip that)
                    continue

            cat_dict[category] = str(total_earned - previous_total_earned) + ' / ' + str(total_possible - previous_total_possible)

            previous_total_earned += total_earned
            previous_total_possible += total_possible

        averages[cur_course] = cat_dict

        previous = arrow_selector
        driver.back()
    
    return averages
