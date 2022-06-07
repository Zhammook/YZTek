import unittest
import yztek_methods as methods
import yztek_locators as locators
import xlrd


class MoodlePositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        # Access the spreadsheet after installing xlrd library
        workbook = xlrd.open_workbook("DataFile.xls")
        sheet = workbook.sheet_by_name("UserCredentials")  # Read data from Excel sheet named "UserCredentials"
        # Get the number of rows in Excel spreadsheet
        rowCount = sheet.nrows
        for curr_row in range(1, rowCount):
            locators.first_name = sheet.cell_value(curr_row, 0)
            locators.last_name  = sheet.cell_value(curr_row, 1)
            methods.user_info()
            methods.create_new_user()
       # methods.search_user()
        methods.log_out()
        methods.tearDown()