from supermarket_inventory_manager_functions import *
print("-------------------------------------------------------SUPER MARKET INVENTORY MANGER-------------------------------------------------------")


number_of_product = int(input("Enter the number of products: "))
number_of_days_to_track = int(input("Enter the numbers of days to track: "))

stored_units = []

for count in range(0, number_of_product):
    print(f"---- Product {count +1}----")
    store_in_array = []
    for inner_count in range(0, number_of_days_to_track):
        print(f"Enter units sold on Day {inner_count +1}", end="")
        units_sold = int(input("....  "))
        store_in_array.append(units_sold)
    stored_units.append(store_in_array)
                 
#print(stored_units)
product_total = get_total(stored_units)
best_day = get_best_day(stored_units)
best_selling_product =  the_best_selling_product(stored_units)
best_unit_total = the_best_selling_product_unit(stored_units)
lowest_selling_product= the_lowest_selling_product(stored_units)
lowest_unit_total = the_lowest_selling_product_unit(stored_units)
overall_units_sold = overall_units_sold(stored_units)

print("=========================== STORE SALES SUMMARY ===========================", end="\n\n")
print("PRODUCT", end="      ")
for counter in range(0, number_of_days_to_track):
    print(f"DAY{counter+1}", end="     ")
print("TOTAL", end="   ")
print("BEST DAY")
print("----------------------------------------------------------\n")

for product_count in range(0, number_of_product):
    print(f"Product {product_count+1}", end="     ")
    for days_count in range(0, number_of_days_to_track):
        print(f"{stored_units[product_count][days_count]}", end="     ")
    print(f"{product_total[product_count]} ", end="  ")
    print(f"  {Day best_day[product_count]}")

print("\n----------------------------------------------------------\n")

print(f"""
Best-Selling product: Product {best_selling_product} ({best_unit_total})
Lowest-Selling product: Product {lowest_selling_product} ({lowest_unit_total})
Overall units sold: {overall_units_sold}
""")
