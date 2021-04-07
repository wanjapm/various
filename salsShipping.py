def normal_shipping(weight):
    flat_charge = 20
    if weight <= 2:
      return ( 1.5 * weight ) + flat_charge
    elif weight > 2 and weight <= 6:
        return (3 * weight) + flat_charge
    elif weight > 6 and weight <= 10:
        return (4 * weight) + flat_charge
    else:
        return (4.75 * weight) + flat_charge

def drone_shipping(weight):
    if weight <= 2:
      return ( 4.5 * weight ) 
    elif weight > 2 and weight <= 6:
        return (9 * weight) 
    elif weight > 6 and weight <= 10:
        return (12 * weight) 
    else:
        return (14.25 * weight) 

weight = float(input("Please enter the weight of your package:>>"))
normal = normal_shipping(weight)
premium = 125
drone = drone_shipping(weight)

if normal < premium and normal < drone:
    print(f"Cheapest method of shipping is: Ground Shipping at a cost of ${normal}.")
elif premium < normal and premium < drone:
    print(f"Cheapest method of shipping is: Ground Premium Shipping at a cost of ${premium}.")
else:
    print(f"Cheapest method of shipping is: Drone Shipping at a cost of ${drone}.")