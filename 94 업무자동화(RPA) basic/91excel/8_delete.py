from openpyxl import load_workbook
wb = load_workbook("sample5.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에 있는 7번 학생 데이타 삭제
# ws.delete_rows(8, 3) # 8번째 줄부터 3줄 삭제
# wb.save("sample8_delete_rows.xlsx")

# ws.delete_cols(2) # 2번째 열 B 삭제
ws.delete_cols(2, 2) # B번째 열부터 2열 우축으로 delete
wb.save("sample8_delete_cols.xlsx")