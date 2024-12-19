1. Python program to check leap year

#Enter the year first
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

-----------------------------------------------------------------------------------------------------------------

2.Python Program to Find the Largest Among Three Numbers

# Input: Three numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

# Find the largest number
#if number1 is largest
if number1 >= number2 and number1 >= number3:
    print("The largest number is:",number1)
#if number2 is largest
elif number2 >= number1 and number2 >= number3:
    print("The largest number is:",number2)
#if number3 is largest
else:
    print("The largest number is:",number3)

-----------------------------------------------------------------------------------------------------------------

3. Python Program to Check if a Number is Positive, Negative or 0

# Input: A number from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero

#if the number is positive:
if number > 0:
    print("The",number,"is positive number")
    
#if the number is negative
elif number < 0:
    print("The",number,"is negative number")
    
#if the number is zero
else:
    print("The",number,"is zero number")

---------------------------------------------------------------------------------------------------------------

4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount.

# Input: Product code and order amount
product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging-based): "))
order_amount = float(input("Enter the order amount: Rs. "))

# Initialize discount
discount = 0

# Apply discount based on product code and order amount
if product_code == 1 and order_amount > 1000:
    discount = 0.10  # 10% discount for Battery-based Toys
elif product_code == 2 and order_amount > 100:
    discount = 0.05  # 5% discount for Key-based Toys
elif product_code == 3 and order_amount > 500:
    discount = 0.10  # 10% discount for Electrical Charging-based Toys

# Calculate the discount amount and the final price
discount_amount = order_amount * discount
net_amount = order_amount - discount_amount

# Output: Final amount to be paid after discount
print(f"The net amount to be paid after discount is: Rs. {net_amount:.2f}")


-------------------------------------------------------------------------------------------------------------------------------

5. A transport company charges the fare according to following table:

# Input: Distance traveled
distance = float(input("Enter the distance traveled (in km): "))

# Fare calculation based on distance
if 1 <= distance <= 50:
    fare = distance * 8  # 8 Rs/km for 1-50 km
elif 51 <= distance <= 100:
    fare = distance * 10  # 10 Rs/km for 51-100 km
elif distance > 100:
    fare = distance * 12  # 12 Rs/km for distance > 100 km
else:
    print("Invalid distance!")
    fare = 0

# Output: Fare to be paid
print(f"The total fare is: Rs. {fare:.2f}")

