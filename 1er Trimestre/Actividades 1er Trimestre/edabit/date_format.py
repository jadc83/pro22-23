"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
"""

def format_date(date):
    date = date.split("/")
    print(date[2]+date[1]+date[0])