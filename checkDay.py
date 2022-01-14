from datetime import date

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to find last day of previous month
def lastDay(inMonth, inYear):
    for i in range(months[inMonth - 1]):
        temp = date(int(inYear), inMonth, (i + 1)).weekday()
        #print("date: ", date(int(inYear), inMonth, (i+1)), ", which is: ", temp)
        if temp < 5:
            friday = i + 1
            #print("Friday: ", friday)
    return friday

# Function to find previous work weekday
def prevDay(inMonth, inDay, inYear):
    for i in range(months[inMonth - 1]):
        temp = date(int(inYear), inMonth, (i + 1)).weekday()
        if temp < 5:
            if (i+1) < inDay:
                day = i + 1
            else:
                break
    return day

def checkYear(inMonth, inDay, inYear):
    if inMonth == 1:
        lastMonth = 12
        lastYear = int(inYear) - 1
        day = lastDay(lastMonth, lastYear)
        retDate = date(lastYear, lastMonth, day)
    else:
        lastMonth = inMonth - 1
        retDate = date(int(inYear), lastMonth, inDay)
    return retDate
