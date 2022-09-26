from openpyxl import load_workbook

data_file = 'sales_data.xlsx'

wb = load_workbook(data_file)

ws = wb['Sheet1']
all_rows = list(ws.rows)

for row in all_rows[1:8]:
    ID = row[0].value
    Last_Name = row[1].value
    searchCriteria = input( "Enter customer ID or last name: " )
    if searchCriteria == 'ID' or searchCriteria == 'Last_Name':
        print(f"{ID, Last_Name}")
    else:
        print( "ERROR:You must enter either 'ID' for invoice or 'Last Name' for customer search" )
        
    
    
    
    


if searchCriteria == 'ID':
    print("{} records found." .format(termfound))

if searchCriteria == 'Last Name':
    print("{} records found." .format(termfound))  


