# Structure for an item which stores weight and corresponding profit
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
    # Sorting Items on basis of value-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # Result (value in Knapsack)
    final_value = 0.0

    # Looping through all Items
    for item in arr:
        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        # If we can't add current Item, add fractional part of it
        else:
            final_value += item.profit * W / item.weight
            break

    # Returning final value
    return final_value

# Driver Code
if __name__ == "__main__":
    # Get the maximum weight of knapsack from user
    W = float(input("Enter the maximum weight capacity of the knapsack: "))

    # Get number of items
    n = int(input("Enter the number of items: "))

    # Create a list to store items
    items = []
    for i in range(n):
        profit = float(input(f"Enter profit for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, items)
    print(f"The maximum profit achievable is: {max_val}")
