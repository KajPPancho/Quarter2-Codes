fruits = []
for f in range(1, 5):
    fruit = input(f"Enter fruit {f}: ")
    fruits.append(fruit)
rem_fruit = input("Enter a fruit to remove: ")
fruits.remove(rem_fruit)
print()
print("After remove: " ,fruits)
fruits.pop()
print("After pop: " ,fruits)
