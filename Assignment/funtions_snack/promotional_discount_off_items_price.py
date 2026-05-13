#collect the item name
#collect price of the item
#collect promotonial code 
#depending on the type of promotonial code, make chages to the price depending on what discount it has
#return the discount
#test

def promotional_code(items, price, code):
    if code == "SAVE10":
        discount = float(price *0.10)
        discounted_price = price - discount
    elif code == "HALFOFF":
        discount = float(price * 0.50)
        discounted_price = price - discount
    else:
        discounted_price = (f"Invalid Promotional code..\nAll promo CODE must be in upperCase.\nCheck if ALL characters are in upperCase i.e(SAVE10 or HALFOFF)...\nNo discount! you're to pay {price}")
    return discounted_price

#print(promotional_code("Jacket", 70000.34, "HALFFF"))
