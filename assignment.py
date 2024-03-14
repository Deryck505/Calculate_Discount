##Solution 1
def calculate_discount(price, discount_percent ):
    final_price = price * (1-discount_percent*0.01)
    return (final_price)

##Testing solution
calculate_discount(100, 20)




##Solution 2
def calculate_discount():
    print("Initial selling Price")
    price= input()
    price = int (price)
    print ("Discount percentage")
    discount_percent = input()
    discount_percent = int (discount_percent)
    final_price = price * (1-discount_percent*0.01)
    print("Final price :", final_price )

##Testing solution 
calculate_discount()
