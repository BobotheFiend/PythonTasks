# naira converter

def naira_conversion(user_money): 
    
    print("""
                    WELCOME TO S.K.Bank
                YOUR SATISFACTION IS OUR PLEASURE
                    Enjoy your Banking with us...
                                                    """
                                                        )

    dollar_converter = float(input('Enter the Amount in Dollar you would like to convert to Naira: '))

    user_money = dollar_converter * 1550
    return user_money

print(f"The your Naira amount is {naira_conversion(100)}N")
print("Thank you for banking with us... Do have a lovely day!")
