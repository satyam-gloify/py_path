from googleservices import GsheetService
from analysis_services import MyAnalytics
import keyword

services= GsheetService(
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'],
    sheetName='satyammatch',
    keyAbsolutePath='/media/i/e/setup/doc/pythonwork/2022/googlsheetpython/shreadsheetfromdrive/keys/amplified-lamp-336417-c54d6048d2bc.json'
    )

sheet=services.getWorkSheet(sheetnumber=1)

  
# printing all keywords at once using "kwlist()"
# print("The list of keywords is : ")
# print(keyword.kwlist)
# print(sheet.col_count)
# print(sheet.cell(col=1,row=2))
# print(sheet.get_all_records())

aytcs= MyAnalytics(records=sheet.get_all_records())

print(aytcs.getDataby(operator='Batsman_Name',operand='Runs'))

services.addWorkSheet(maxColumns=10,maxRows=4,workSheetName='mayank')

