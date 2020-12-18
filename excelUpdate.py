import openpyxl


def excel_update(keyword, new_products):
    file_name = keyword + ".xlsx"
    book = openpyxl.load_workbook(file_name)
    sheet = book.active
    product_list = []
    # appends new products to the end of the excel sheet
    for product in new_products:
        temp_list = []
        temp_list.append(product.date)
        temp_list.append(product.desc)
        temp_list.append(product.price)
        temp_list.append(product.link)
        product_list.append(temp_list)
    for item in product_list:
        sheet.append(item)

    book.save(file_name)
