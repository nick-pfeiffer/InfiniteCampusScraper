from config import * 
from get_courses import courses
from get_averages import averages

def format(term): 
    formatted = ''
    for sub in term: 
        formatted += '\n\n\t' + sub
        for cat in term[sub]: 
            percent = float(term[sub][cat].split('/')[0]) / float(term[sub][cat].split('/')[1]) * 100
            formatted += '\n\t\t' + cat + ': ' + term[sub][cat] + ' (' + str(round(percent, 2)) + '%)'
    return formatted


def report(): 
    result = ''
    coursesList = courses(False)

    result += 'Courses'
    for i in coursesList: 
        result += '\n\t- ' + i

    start()
    formatted_first = format(averages(1, True))
    if formatted_first != '': 
        result += '\nTerm 1 Grades\n'
        result += formatted_first

    start()
    formatted_second = format(averages(2, True))
    if formatted_second != '': 
        result += '\n\nTerm 2 Grades\n'
        result += formatted_second
    
    start()
    formatted_third = format(averages(3, True))
    if formatted_third != '': 
        result += '\n\nTerm 3 Grades\n'
        result += formatted_third

    try: 
        start()
        formatted_fourth = format(averages(4, True))
        if formatted_fourth != '': 
            result += '\n\nTerm 4 Grades\n'
            result += formatted_fourth
    except: 
        pass

    return result

print(report())
