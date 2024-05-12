import gspread
from oauth2client.service_account import ServiceAccountCredentials
# !pip3 install gspread
# !pip3 install --upgrade google-api-python-client oauth2client 

class GsheetService(object):
    def __init__(self,scope,keyAbsolutePath,sheetName):
# define the scope
        self.scope = scope
# add credentials to the account
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(keyAbsolutePath, scope)
# authorize the clientsheet 
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(sheetName)

# create read/update/delete method
    def  getWorkSheet(self, sheetnumber):
        return self.sheet.get_worksheet(sheetnumber-1)

#add new WordPage to you Sheet
    def addWorkSheet(self,maxRows,maxColumns,workSheetName):
        response=False
        try:
            self.sheet.add_worksheet(rows=maxRows,cols=maxColumns,title=workSheetName)
            response=True
        except gspread.exceptions.APIError as error:
            msg = str(error.args[0]['message'])
            print("Something Worng: "+msg)
            respons=False
        return response
    def update():
        print('update')
    def delete():
        print('delete')
    