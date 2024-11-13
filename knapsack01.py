from queue import Queue

# Define an Item class to represent each item in the knapsack
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

# Define a Node class to represent each node in the branch and bound tree
class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

# Define a function to calculate the maximum possible profit for a given node
def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    tot_weight = u.weight

    while j < n and tot_weight + arr[j].weight <= W:
        tot_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    if j < n:
        profit_bound += (W - tot_weight) * (arr[j].value / arr[j].weight)

    return profit_bound

# Define the knapsack_solution function that uses the Branch and Bound algorithm to solve the 0-1 Knapsack problem
def knapsack_solution(W, arr, n):
    # Sort the items by value-to-weight ratio in descending order
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    q = Queue()
    u = Node(-1, 0, 0, 0)
    q.put(u)

    max_profit = 0

    while not q.empty():
        u = q.get()

        if u.level == -1:
            v = Node(0, 0, 0, 0)
        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit + arr[u.level + 1].value, 0, u.weight + arr[u.level + 1].weight)

        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v.bound = bound(v, n, W, arr)

        if v.bound > max_profit:
            q.put(v)

        v = Node(u.level + 1, u.profit, 0, u.weight)
        v.bound = bound(v, n, W, arr)

        if v.bound > max_profit:
            q.put(v)

    return max_profit

# Driver Code
if __name__ == '__main__':
    W = 10
    arr = [Item(2, 40), Item(3.14, 50), Item(1.98, 100), Item(5, 95), Item(3, 30)]
    n = len(arr)

    print('Maximum possible profit =', knapsack_solution(W, arr, n))
