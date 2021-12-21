from reader import read, determineMonth
import sys

repeat = True
year = ""
month = 0

try:
    while repeat:
        # Gets the year you are in
        print("What year is it? (eg. 2022)")
        year = input()
        # Gets the month
        print("What month is it? (eg. 11 [is November])")
        month = input()
        # Gets last digits of filename to be opened (Scanned files all have same name)
        filename_add_on = input("What are the last 3 digits of the filename?")
        # def read() call
        read(filename_add_on, year, month)
        # Checks to see if you want to rotate another PDF
        print("Is there another file?")
        resp = input()
        if resp == "yes":
            repeat = True
        else:
            repeat = False
except:
    print("Oops, a ", sys.exc_info()[0], "occurred.")
    print("Please try again, maybe try plugging in the USB this time IDIOT!!")
