#Joshua
name = input("Enter your name: ").strip()
snack = input("what snack are you getting?: ").strip()
price = float(input("what is the price of said snack?: ").strip())
quantity = int(input("how many are you getting?: ").strip())
totalprice = price*quantity

if totalprice >= 10:
    discount = totalprice*0.10
    discount_price = totalprice-discount
    print(f"""
    customer: {name}
    Snack: {snack}
    Quantity: {quantity}
    totalsub: {totalprice}
    discount: {discount:.2}
    final total: {discount_price}
    """)
else:
    print(f"""
    customer: {name}
    Snack: {snack}
    Quantity: {quantity}
    total: {totalprice}
    """)