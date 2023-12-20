# Pizza Calculator

#Display information about Pizza sizes & price
print('Welcome to the Pizza Calculator\n')
print('Pizza Base Cost: $10\n')
print('Cost Based on Pizza Size:')
print('Pizza Sizes |\tPrice')
print('   SMALL    |\t +$5 \n   MEDIUM   |\t +$8 \n   LARGE    |\t +$10 \n')

#Display information about toppings
print('Single Topiing Cost is $2\n')

#Calculate Price
def calculate_cost(size, toppings):
    base_cost = 10  # Base cost of the pizza is 10
    topping = 2  # Single topping cost is 2

    # total cost
    total_cost = base_cost + (topping * toppings)

    # cost based on pizza size
    if size == "SMALL":
        total_cost += 5
    elif size == "MEDIUM":
        total_cost += 8
    elif size == "LARGE":
        total_cost += 10
    else:
        print("Invalid size. Please choose small, medium, or large.")
        return None

    return total_cost

def main():
    # Get user input for pizza size
    size = input("Enter the size of the pizza:\n").upper()

    # Get user input for the number of toppings
    toppings = int(input("\nEnter the number of toppings:\n"))

    # Calculate the total cost
    total_cost = calculate_cost(size, toppings)

    # Display the result
    if total_cost is not None:
        print(f"\nThe total cost of your pizza is ${total_cost:.2f}")
        
    # Calling main function
if __name__ == "__main__":
    main()