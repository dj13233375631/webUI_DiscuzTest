import xlrd
from framework.logger import Logger

logger = Logger(logger="Util").getlog()
class Util(object):
    @classmethod
    def read_excel(cls,excel_path,sheetName = "sheet1"):
        workbook = xlrd.open_workbook(excel_path)
        sheet = workbook.sheet_by_name(sheetName)
        keys = sheet.row_values(0)
        rowNum = sheet.nrows
        colNum = sheet.ncols

        if rowNum <= 1:
            logger.error("少于1")
        else:
            r = []
            for i in range()

