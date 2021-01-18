from config import *
from login import *
from navigation import * 
from bs4 import BeautifulSoup
import time

# login -> navigate to the 'grades' tab
login()
grades()

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

# get all courses
courses = [a.string for a in soup.find_all('a', href=True) if a.string is not None]

# todo: return 'courses' to the user somehow
