from calendar import HTMLCalendar, TextCalendar


def semester_calendar(output_type, year, first_month, last_month):
    """
    >>> print( semester_calendar('txt', 2021, 10, 10) )
        October 2021
    Mo Tu We Th Fr Sa Su
                 1  2  3
     4  5  6  7  8  9 10
    11 12 13 14 15 16 17
    18 19 20 21 22 23 24
    25 26 27 28 29 30 31
    <BLANKLINE>
    """
    if output_type == "txt":
        result = ""
        for i in range(first_month, last_month+1):
            txt_calendar = TextCalendar(firstweekday = 0)
            result += txt_calendar.formatmonth(year, i)
        return result
    else :
        result = ""
        for i in range(first_month, last_month+1):
            html_calendar = HTMLCalendar(firstweekday = 0)
            result += html_calendar.formatmonth(year, i)
        return result


if __name__ == "__main__":
   import doctest
   print(doctest.testmod())