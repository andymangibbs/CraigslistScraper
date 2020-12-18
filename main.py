import dataPull
import excelWrite
import excelRead
import excelUpdate
import product
import dataCompare
import time
import speaker


def main():
    user_selection = input('1 to Search and create new Excel Sheet\n2 to search for updated listings\n'
                            '3 to run autoscript\nEnter Selection: ')
    # Test products
    test_product = product.Product
    test_product.date = "Test Date"
    test_product.desc = "Test DESCRIPTION"
    test_product.price = "$$$$$"
    test_product.link = "Test Link"
    # Runner for pulling data off craigslist
    online_final, keyword = dataPull.data_pull()
    file_name = keyword + ".xlsx"

    if '1' in user_selection:
        try:
            excelRead.excel_reader(file_name)
            sel = input("Warning, this document already exists. Do you want to overwrite? (y/n): ")
            if sel == 'y':
                excelWrite.excel_writer(online_final, keyword)
            else:
                print("Program terminated")
        except:
            excelWrite.excel_writer(online_final, keyword)

    if '2' in user_selection:
        #online_final.append(test_product) # REMOVE FOR FINAL TEST PRODUCT
        read_list = []
        try:
            read_list = excelRead.excel_reader(file_name)
            new_list = dataCompare.data_compare(online_final, read_list)
            if new_list == "empty":
                print("Nothing new to add!")
            else:
                speaker.speak("New Products Added!")
                print("New products added!")
                excelUpdate.excel_update(keyword, new_list)
        except:
            print("Failed to update. Ensure the first search was done.")

    if '3' in user_selection:
        user_runs = input("Enter how many times you'd like the script to run: ")
        user_wait = input("Enter how long to wait between searches(seconds): ")
        iterations = int(user_runs)
        wait_time = int(user_wait)
        while int(iterations) >= 0:
            #online_final.append(test_product) # REMOVE FOR FINAL, TEST PRODUCT
            read_list = []
            try:
                read_list = excelRead.excel_reader(file_name)
                new_list = dataCompare.data_compare(online_final, read_list)
                if new_list == "empty":
                    print("Nothing new.")
                else:
                    print("----------New products added-----------")
                    speaker.speak("New Products Added!")
                    excelUpdate.excel_update(keyword, new_list)
                iterations -= 1
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print("Craigslist results updated for %s at %s" % (keyword, result))
                time.sleep(wait_time)
            except:
                print("Failed to run script. Ensure the first search was done.")


main()
