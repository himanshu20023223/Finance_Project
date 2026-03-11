import pandas as pd
from find_highest_payment_mode_total import read_excel

excel_files=read_excel()
all_sheets=[]
# function to read sheet data by name and return excel sheet and it's name as a list
def read_sheet(sheet_name:str)-> list:
    excel_sheet = pd.read_excel(r'C:\Users\HP\Desktop\finance_project\spendings-record.xlsx',sheet_name=sheet_name)
    return [excel_sheet,sheet_name]
# fucntion to display all dataframe columns
def display_all_columns()->None:
    # displaying all columns of dataframe
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    return None
sheet=read_sheet(str(excel_files.sheet_names[0]))

# function will iterate over the workbook and will store all available sheets in all_sheets list
def display_all_sheets()->list:
    for sheets in excel_files.sheet_names:
        all_sheets.append(sheets)
    return all_sheets
# accessing only month-wise lists
def month_sheets()->list:
    # storing those worksheets in the list that have monthwise spending records
    work_sheets=[]
    for sheets in all_sheets:
        if "2025" in sheets or "2026" in sheets:
            work_sheets.append(sheets)
    return work_sheets

display_all_sheets()
work_sheets=month_sheets()
# print(read_sheet(str(all_sheets[2]))[1])
display_all_columns()
if __name__=="__main__":
    read_sheet(str(all_sheets[0]))
    month_sheets()
    work_sheets