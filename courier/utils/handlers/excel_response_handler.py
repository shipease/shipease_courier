from openpyxl import Workbook

class ExcelFileResponseHandler:
    
    
    @staticmethod
    def get_workbook():
         # Create a new workbook
        wb = Workbook()
        ws = wb.active
        return ws