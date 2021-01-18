from config import *
from login import log
from navigation import grades 
from bs4 import BeautifulSoup

# login -> navigate to the 'grades' tab
log()
grades()

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

# get all courses
courses = [a.string for a in soup.find_all('a', href=True) if a.string is not None]

# todo: return 'courses' to the user somehow
