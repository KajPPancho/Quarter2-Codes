print("Kindly enter the disatance in km:")
d = float(input())
print("Kindly the rate per km (₱):")
rdist = float(input())

def deliv_fee_calc():
    global d
    global rdist
    deliv_fee = d * rdist
    return deliv_fee

delivery_fee = deliv_fee_calc()
print("The delivery distance is", d, "km in a rate of ₱", rdist, "per km, therefore the total delivery fee is ₱", delivery_fee)