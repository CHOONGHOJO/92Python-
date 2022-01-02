from openpyxl import load_workbook
wb = load_workbook("sample6_search.xlsx")
ws = wb.active

# ws.insert_rows(8) # 빈 8번째 줄이 insert
# ws.insert_rows(8, 5) # 빈줄이 8번째 줄부터 5줄 아래로 insert
# wb.save("sample7_insert_rows.xlsx")

# ws.insert_cols(2) # 빈열이 B번째 열에  insert
ws.insert_cols(2, 3) # 빈열이 B번째 열부터 3열 우축으로 insert
wb.save("sample7_insert_cols.xlsx")