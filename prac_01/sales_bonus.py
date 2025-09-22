"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALE_THRESHOLD=1000
LOW_DISCOUNT_RATE=0.1
HIGH_DISCOUNT_RATE=0.15
sales = float(input("Enter sales: $"))
while sales >=0:
    if sales < SALE_THRESHOLD:
        discount_rate=LOW_DISCOUNT_RATE
    else:
        discount_rate=HIGH_DISCOUNT_RATE
    print(f"Your bonus is $ {sales * discount_rate:.2f}.")
    sales=float(input("Enter sales: $"))
