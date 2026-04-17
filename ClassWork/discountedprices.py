""" Collect the customer(s) total 
    check to see if the customer(s) spendigng total is eligible for a discount
    if the customers total spending matches the discount requirements the customer(s) should be able to get a discount
    the discount requirements are availabe by how high the customer total spending is """ 


customer_total = int(input('Enter customers purchases: '))

discount_one = customer_total * (5/100)
discount_two = customer_total * (10/100)
discount_three = customer_total * (20/100)

new_amount_to_pay_for_five = customer_total - discount_one
new_amount_to_pay_for_ten = customer_total - discount_two
new_amount_to_pay_for_twenty = customer_total - discount_three

if (customer_total >= 1000 and customer_total < 10000):
    print('You recieve a 5% discount')
    print('your discounted price is = ', discount_one)
    print('Total amount to pay is = ', new_amount_to_pay_for_five)
if (customer_total >= 10000 and customer_total < 50000):
    print('You recieve a 10% discount')
    print('Your discounted price is = ',discount_two)
    print('Total amount to pay is = ', new_amount_to_pay_for_ten)
if (customer_total > 50000):
    print('You receive a 20% discount')
    print('Your discounted price is = ', discount_three)
    print('Total amount to pay is = ', new_amount_to_pay_for_twenty)
