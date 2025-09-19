# Ask the user for a number
number = int(input("Enter a number: "))

# Print the multiplication table up to 12
print(f"\nMultiplication Table for {number} up to 12:\n")

count = 1
while count <= 12:
    result = number * count
    print(f"{number} x {count} = {result}")
    count += 1  # Increment count to avoid infinite loop
