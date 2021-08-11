import csv
from helper import run_mode as sm

acceptable_length = 16

def get_column_count(filename):
    reader = csv.reader(open(filename))
    no_of_columns = len(next(reader))
    sm.validating()
    if no_of_columns != 2:
        print(f"invalid number of columns: {no_of_columns}, columns should represent the table and the permissions")
    else:
        print(f"Acceptable number of columns in csv file: {no_of_columns}")

def validate_name(filename):
    db_user = filename.split("__")[0]
    if len(db_user) >= acceptable_length:
        print(f"invalid length for db_username {db_user}. Acceptable length is {acceptable_length}")
        exit()
        
def validator(filename):
    get_column_count(filename)
    #validate_name(filename)
    sm.done_validating()
