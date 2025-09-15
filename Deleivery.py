HowManyDeleivery = int(input("Enter How Many Deliveries Do U Want:"))
name = input("Enter Your Name:")
deliveries = {}

for Delivery in range(HowManyDeleivery):
    print(f"*********Enter Delivery Number {Delivery+1} **********")
    print(
        """ Choose The Number
        1 Food
        2 Metal
        3 Cosmetics
        4 Electronics
        5 Medicine
        """
    )
    chooseMaterial = int(input("Enter The Material Type:"))
    MaterialName = input("Enter Material Name (Eg Parasitamole etc):")
    howmuchweight = int(input("Enter The Weight In KG (1):"))
    howmuchDistance = int(input("Enter The Distance in KM (1):"))
    isurgent = input("Is The Delivery Urgent ? Y or yes and N for No:").lower()

    deliveries[f"Delivery_{Delivery+1}"] = {
        "Name": name,
        "ChooseMaterial": chooseMaterial,
        "MaterialName": MaterialName,
        "Weight": howmuchweight,
        "Distance": howmuchDistance,
        "IsUrgent": isurgent in ['y', 'yes']
    }

print("\n=== ALL DELIVERIES ===")
print(deliveries)

def CalculateTheTotalPrice(delivery_data):
    distance_cost = 0
    distance = delivery_data['Distance']
    
    if distance > 200:
        distance_cost += (distance - 200) * 10
        distance = 200
    if distance > 50:
        distance_cost += (distance - 50) * 8
        distance = 50
    distance_cost += distance * 5

    material_rates = {1: 10, 2: 20, 3: 15, 4: 25, 5: 30}
    material_cost = delivery_data['Weight'] * material_rates[delivery_data['ChooseMaterial']]

    if delivery_data['Weight'] > 100:
        material_cost *= 0.9  

    fuel_surcharge = 0
    if delivery_data['Distance'] > 300:
        fuel_surcharge = distance_cost * 0.15

    fragile_fee = 0
    if (delivery_data['ChooseMaterial'] == 3 or delivery_data['ChooseMaterial'] == 5) and delivery_data['Weight'] > 50:
        fragile_fee = 200

    subtotal = distance_cost + material_cost + fuel_surcharge + fragile_fee

    if delivery_data['IsUrgent']:
        subtotal *= 1.25  

    if HowManyDeleivery > 5:
        subtotal *= 0.95  

    return subtotal


print("\n=== DELIVERY COSTS ===")
for delivery_key, delivery_data in deliveries.items():
    total_cost = CalculateTheTotalPrice(delivery_data)
    print(f"{delivery_key}: ${total_cost:.2f}")