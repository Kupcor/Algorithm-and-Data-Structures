# ========= Info ========
# File to contain a function, that will write a data to exel sheets.

# ============ Dictionaries ============#
import openpyxl


# Reading data about player character
# TODO increase elastic of the function
def write_base(file_path, data_base_len, data_base):

    # open file
    wb = openpyxl.Workbook()
    sheet = wb.active

    # additional array variable
    additional_array = []

    # write data to excel sheet using loop
    # iter.row is a method to read a multiple cells in exel file
    for i in range(1,data_base_len+1):
       sheet.cell(row=i, column=1).value = data_base[i-1]

    wb.save(file_path)