def get_total(product_units):
    
    total_product_unit = []
    for count in product_units:
        sum_of_units = 0
        for elements in count:
            sum_of_units = sum_of_units + elements
        total_product_unit.append(sum_of_units)
            
    return total_product_unit
  

def get_best_day(product_units):
   
    best_days = []
    for count in product_units:
        sum_of_units = 0
        largest = 0
        day = 0
        for elements in count:
            if (elements > largest):
                largest = elements
                day+=1
        best_days.append(day)
            
    return best_days

def the_best_selling_product_unit(total):
    product_total = get_total(total)
    largest= product_total[0]
    for elements in product_total:
        if(elements > largest):
            largest = elements

    return largest

def the_best_selling_product(total):
    product_total = get_total(total)
    largest= product_total[0]
    product = 1
    for elements in product_total:
        if(elements >= largest):
            largest = elements
            product+=1

    return product   

def the_lowest_selling_product_unit(total):
    product_total = get_total(total)
    smallest = product_total[0]
    for elements in product_total:
        if(elements < smallest):
            smallest = elements

    return smallest

def the_lowest_selling_product(total):
    product_total = get_total(total)
    smallest= product_total[0]
    product = 1
    for elements in product_total:
        if(elements > smallest):
            smallest = elements
            product+=1

    return product

def overall_units_sold(items):
  
    sum_of_units = 0  
    for count in items:
        for elements in count:
            sum_of_units = sum_of_units + elements
            
    return sum_of_units


ii = [[120, 95], [45, 60], [200, 175]]
tt = get_best_day(ii)
print(tt)
