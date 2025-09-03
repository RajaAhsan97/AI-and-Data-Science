# Practice Exersises for Students on CSV file
#
# You have provided a csv file of inventory; with columns PRODUCT, PRICE, QUANTITY
# 1. Read data into Dictionary and display the data
# 2. Append two new products to the file
# 3. print products with quantity > 10  [Filtering]
# 4. Calculate total value of inventory (Price x Quantity)

import csv

## ----------------------------------------------------------------------------
### Step 1: Read data into Dictionary and display it --------------------------
## ----------------------------------------------------------------------------
##with open("products_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##
##    print("Inventory data:")
##    for row in data:
##        print(row)


## ----------------------------------------------------------------------------
### Step 2: Append two new products to the file -------------------------------
## ----------------------------------------------------------------------------
##new_products = [
##    ['Mouse 23', '200', '15'],
##    ['Laptop 1', '100', '5']
##]
##
##with open("products_50_records.csv", mode="a", newline='') as file:
##    writer = csv.writer(file)
##
##    writer.writerows(new_products)

## ----------------------------------------------------------------------------
### Step 3: Filter products with quantity -------------------------------------
## ----------------------------------------------------------------------------
##with open("products_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##
##    print("Products with quantity > 10")
##    for row in data:
##        if int(row['Quantity']) > 10:
##            print(row)


## ----------------------------------------------------------------------------
### Step 4: Calculate total value of inventory (Price x Quantity) -------------
## ----------------------------------------------------------------------------
##with open("products_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##
##    inventory_value = 0
##
##    for row in data:
##        cost = float(row['Price']) * int(row['Quantity'])
##
##        inventory_value += cost
##
##    print("Total inventory value in Rs = ", inventory_value)

