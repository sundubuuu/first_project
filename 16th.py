from openpyxl import Workbook

wb = Workbook()  #클래스 변수 생성
ws =wb.active

ws['A1'] ='Data'

wb.save('result.xlsx')
