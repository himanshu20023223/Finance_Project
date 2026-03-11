import pandas as pd

# this function will read the excel workbook and return the first sheet reference as output
def read_excel()-> object:
    excel_file = pd.ExcelFile(r"C:\Users\HP\Desktop\finance_project\spendings-record.xlsx")
    return excel_file
# function to return with which i have made the max amount of payments
def highest_payment_mode(excel_file: object)->None:
    all_data = [] #creating a list object to store all sheets data inside the list
    #accessing all sheets name from the workbook and storing it in all_data list
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(r'C:\Users\HP\Desktop\finance_project\spendings-record.xlsx', sheet_name=sheet_name)
        all_data.append(df)

    # Combine all data
    combined_df = pd.concat(all_data, ignore_index=True)

    # Group by Payment-Mode and sum the amounts
    payment_mode_totals = combined_df.groupby('Payment-Mode')['Amount'].sum().sort_values(ascending=False)

    print('Total Payments by Payment Mode:')
    print(payment_mode_totals)
    print('\
    Highest Payment Mode: ' + str(payment_mode_totals.index[0]) + ' with total amount: ' + str(payment_mode_totals.iloc[0]))
    return None

excel_file=read_excel()
if __name__=="__main__":
    highest_payment_mode(excel_file)