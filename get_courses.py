from config import *
from login import log
from navigation import grades 
from bs4 import BeautifulSoup

def courses(started): 
    # login -> navigate to the 'grades' tab
    log(started)
    grades(started)

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    # get all courses
    courses = [a.string for a in soup.find_all('a', href=True) if a.string is not None]

    return courses
