# Print numbers 1 to 50
print("Numbers from 1 to 50:")
for i in range(1, 51):
    print(i)

# Print even numbers
print("\nEven numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Handle invalid input
print("\nInput Handling:")
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")