print("Hello User...")
print("Kindly enter your age:")
age = int(input())

sum_age = 0
for x in range(1, age + 1):
    sum_age += x
    
print("The sum of one up to your age is" ,sum_age)
