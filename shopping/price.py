

def calculate_bill(*prices):
    total = 0
    for price in prices:
        total = total + price
    return total
