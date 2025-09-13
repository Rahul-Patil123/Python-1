import openpyxl

inv_list = openpyxl.load_workbook("inventory.xlsx")
product_details = inv_list["Sheet1"]

product_per_company = {}
inventory_per_company = {}

for product_row in range(2, product_details.max_row + 1):
    supplier_name = product_details.cell(product_row, 4).value
    
    if supplier_name in product_per_company:
        product_per_company[supplier_name] += 1
    else:
        product_per_company[supplier_name] = 1
        
print("These are total products per company:", product_per_company)

for product_row in range(2, product_details.max_row + 1):
    supplier_name = product_details.cell(product_row, 4).value
    inventory_value = product_details.cell(product_row, 2).value
    if supplier_name in inventory_per_company:
        inventory_per_company[supplier_name] += inventory_value
    else:
        inventory_per_company[supplier_name] = inventory_value

print("These are total inventory per company:", inventory_per_company)