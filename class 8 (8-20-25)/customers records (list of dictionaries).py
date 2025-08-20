# List of dictionaries practical implementation for customer records


customers = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Doe",
        "address": "302xyz",
        "Discounts": ["standard", "volume", "loyalty"]
    },
    {
        "customer id": 1,
        "first name": "Raja",
        "last name": "Ahsan",
        "address": "301xyz",
        "Discounts": []
    },
    {
        "customer id": 2,
        "first name": "Talat",
        "last name": "Hussain",
        "address": "310xyz",
        "Discounts": ["volume", "loyalty"]
    }
]

# iterating over records in the list
for i in range(len(customers)):
    print(f"customer {customers[i]['customer id']} have {len(customers[i]['Discounts'])}")

# apply discount percentage
for customer in customers:
    discount_percentage = []
    if len(customer['Discounts']) > 0:
        for discount in customer['Discounts']:
            if discount == 'standard':
                discount_per = 5
            elif discount == 'volume':
                discount_per = 10
            elif discount == 'loyalty':
                discount_per = 15
            else:
                discount_per = 'Invalid Voucher'
            discount_percentage.append(discount_per)
    customer.update({'discount percentage': discount_percentage})


# printing the records
# iterating over list of dictionary
for customer in customers:
    print("-------------------------------")
    # iterating over dictionary
    for key, value in customer.items():
        print(f"{key}: {value}")
    print("--------------------------------")
