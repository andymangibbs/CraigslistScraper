import xlsxwriter


def excel_writer(product_list, keyword):
    # create and excel sheet
    file_name = keyword + ".xlsx"
    print(file_name)

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet(keyword)
    print("Workbook not found, creating workbook.")
    row = 0
    col = 0

    # populates cells in sheet with products
    for product_cur in product_list:
        worksheet.write(row, col, product_cur.date)
        worksheet.write(row, col + 1, product_cur.desc)
        worksheet.write(row, col + 2, product_cur.price)
        worksheet.write(row, col + 3, product_cur.link)
        row += 1

    workbook.close()
