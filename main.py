from day_imports import *
from Tools import *

if __name__ == '__main__':
    todays_date = get_todays_date()
    insert_data(todays_date)
    day12_1.execution()
    day12_2.execution()
    #exec("day{}_1.execution()".format(todays_date))
    #exec("day{}_2.execution()".format(todays_date))
