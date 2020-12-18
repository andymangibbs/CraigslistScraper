import xlrd
import product


def excel_reader(file_name):
    # open excel sheet
    loc = "C:/Users/andym/PycharmProjects/FacebookScraper/" + file_name
    read_list = []
    temp_list = []

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    rows_total = sheet.nrows
    col_total = sheet.ncols

    # create a list of all of the cells in the sheet
    for i in range(rows_total):
        for r in range(col_total):
            temp_list.append(sheet.cell_value(i, r))

    # create a list of products, from temp_list
    for i in range(rows_total):
        temp_product = product.Product()
        for r in range(col_total):
            if r == 0:
                temp_product.date = sheet.cell_value(i, r)
            elif r == 1:
                temp_product.desc = sheet.cell_value(i, r)
            elif r == 2:
                temp_product.price = sheet.cell_value(i, r)
            elif r == 3:
                temp_product.link = sheet.cell_value(i, r)
            else:
                print("Possible overflow detected in excelRead?")
        read_list.append(temp_product)

    return read_list
