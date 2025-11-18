i = []
print("Please enter your 5 travel destinations:")
for d in range(1, 6):
    dest = input(f"Destination {d}:")
    i.append(dest)
print("Original Travel Itnerary:")
for x, location in enumerate(i, start=1):
    print(f"{x}, {location}")

print()
print("Let's update your 2nd and 5th destination")
i[1] = input("Enter a new destination for position 2: ")
i[4] = input("Enter a new destination for position 5: ")

print("Updated Travel Itinerary:")
for x, location in enumerate(i, start=1):
    print(f"{x}. {location}")
