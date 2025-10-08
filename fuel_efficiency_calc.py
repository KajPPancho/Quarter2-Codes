print("Please enter the distance in kilometers:")
dist = float(input())
print("Kindly enter the fuel consumed in liters:")
fuel = float(input())

def calc_fuel_efficiency():
    global dist
    global fuel
    fuel_efficiency = dist / fuel
    return fuel_efficiency

efficiency = calc_fuel_efficiency()
print(f"Your vehicle's fuel efficiency is" ,efficiency, "km/l.")